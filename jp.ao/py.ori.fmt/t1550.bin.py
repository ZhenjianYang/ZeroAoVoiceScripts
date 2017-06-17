from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "フラン",                 # 1
        "ドノバン警部",           # 2
        "レイモンド捜査官",       # 3
        "イリア",                 # 4
        "シュリ",                 # 5
        "シズク",                 # 6
        "ミハイル",               # 7
        "アリオス",               # 8
        "ダイソン用務員",         # 9
        "セシル",                 # 10
        "看護師シロン",           # 11
        "看護師メイファ",         # 12
        "診察医ベルダイン",       # 13
        "アルバート大公",         # 14
        "ファラ夫人",             # 15
        "セイランド教授",         # 16
        "丸椅子",                 # 17
        "セルゲイ",               # 18
        "SE制御",                 # 19
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
        "Function_13_1B3E",        # 0D, 13
        "Function_14_1CAE",        # 0E, 14
        "Function_15_1D66",        # 0F, 15
        "Function_16_1E8A",        # 10, 16
        "Function_17_1F40",        # 11, 17
        "Function_18_204C",        # 12, 18
        "Function_19_298B",        # 13, 19
        "Function_20_2D1B",        # 14, 20
        "Function_21_3345",        # 15, 21
        "Function_22_3A25",        # 16, 22
        "Function_23_3BB0",        # 17, 23
        "Function_24_4CE5",        # 18, 24
        "Function_25_4EAE",        # 19, 25
        "Function_26_518B",        # 1A, 26
        "Function_27_5F1B",        # 1B, 27
        "Function_28_6393",        # 1C, 28
        "Function_29_69FC",        # 1D, 29
        "Function_30_6D0C",        # 1E, 30
        "Function_31_6E09",        # 1F, 31
        "Function_32_6EEB",        # 20, 32
        "Function_33_7318",        # 21, 33
        "Function_34_73ED",        # 22, 34
        "Function_35_7555",        # 23, 35
        "Function_36_7AA3",        # 24, 36
        "Function_37_8207",        # 25, 37
        "Function_38_820E",        # 26, 38
        "Function_39_8434",        # 27, 39
        "Function_40_849C",        # 28, 40
        "Function_41_9811",        # 29, 41
        "Function_42_9846",        # 2A, 42
        "Function_43_986C",        # 2B, 43
        "Function_44_9898",        # 2C, 44
        "Function_45_98BE",        # 2D, 45
        "Function_46_98F3",        # 2E, 46
        "Function_47_9919",        # 2F, 47
        "Function_48_A256",        # 30, 48
        "Function_49_A260",        # 31, 49
        "Function_50_BBF3",        # 32, 50
        "Function_51_BC12",        # 33, 51
        "Function_52_BC22",        # 34, 52
        "Function_53_BC37",        # 35, 53
        "Function_54_BC53",        # 36, 54
        "Function_55_BC6F",        # 37, 55
        "Function_56_BC8B",        # 38, 56
        "Function_57_BCA7",        # 39, 57
        "Function_58_BCC3",        # 3A, 58
        "Function_59_BCDF",        # 3B, 59
        "Function_60_BD2B",        # 3C, 60
        "Function_61_CBCF",        # 3D, 61
        "Function_62_CFF3",        # 3E, 62
        "Function_63_DE5D",        # 3F, 63
        "Function_64_E581",        # 40, 64
        "Function_65_E5AA",        # 41, 65
        "Function_66_E5D3",        # 42, 66
        "Function_67_E5E6",        # 43, 67
        "Function_68_F2F0",        # 44, 68
        "Function_69_F349",        # 45, 69
        "Function_70_F3A2",        # 46, 70
        "Function_71_F3FB",        # 47, 71
        "Function_72_F454",        # 48, 72
        "Function_73_F4AD",        # 49, 73
        "Function_74_F506",        # 4A, 74
        "Function_75_F519",        # 4B, 75
        "Function_76_FD4C",        # 4C, 76
        "Function_77_FF93",        # 4D, 77
        "Function_78_10C49",       # 4E, 78
        "Function_79_10C86",       # 4F, 79
        "Function_80_10D58",       # 50, 80
        "Function_81_10D88",       # 51, 81
        "Function_82_10DB8",       # 52, 82
        "Function_83_10DE8",       # 53, 83
        "Function_84_10E04",       # 54, 84
        "Function_85_10E20",       # 55, 85
        "Function_86_10E30",       # 56, 86
        "Function_87_11462",       # 57, 87
        "Function_88_1147B",       # 58, 88
        "Function_89_114A6",       # 59, 89
        "Function_90_114D1",       # 5A, 90
        "Function_91_114FC",       # 5B, 91
        "Function_92_11515",       # 5C, 92
        "Function_93_11563",       # 5D, 93
        "Function_94_115F6",       # 5E, 94
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
    Jump("loc_1B3A")

    label("loc_1378")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1389")
    Call(0, 27)
    Jump("loc_1B3A")

    label("loc_1389")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_139A")
    Call(0, 27)
    Jump("loc_1B3A")

    label("loc_139A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_155E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1512")

    #C0001
    ChrTalk(
        0xD,
        (
            "#11205F……あ、そうだ……\x02\x03",

            "#11203F昨日、キーアちゃんが\x01",
            "お見舞いに来てくれたんですけど……\x02\x03",

            "#11210F私の手術の話を聞いて、\x01",
            "とても落ち込んでしまったみたいで。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x101,
        (
            "#00003F……ああ、確かに今日は\x01",
            "朝から元気がなかったみたいだ。\x02\x03",

            "#00000Fでも、大丈夫だよ。\x01",
            "シズクちゃんが前向きなら、\x01",
            "キーアもすぐ元気になるさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xD,
        "#11200Fはい……だといいんですけど。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_1559")

    label("loc_1512")


    #C0004
    ChrTalk(
        0xD,
        (
            "#11200Fキーアちゃん……\x01",
            "早く元気になってくれると\x01",
            "いいんですけど。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1559")

    Jump("loc_1B3A")

    label("loc_155E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_156F")
    Call(0, 13)
    Jump("loc_1B3A")

    label("loc_156F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1B31")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A81")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C6, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1594")
    Call(0, 18)
    Jump("loc_1A7C")

    label("loc_1594")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A7C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15B0")
    Call(0, 17)
    Jump("loc_1A7C")

    label("loc_15B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x150, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19D1")

    #C0005
    ChrTalk(
        0xD,
        (
            "#01505F……あ、そういえば……\x02\x03",

            "#01500Fキーアちゃん、今日はなんだか\x01",
            "様子が変じゃありませんでしたか？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1701")
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
            "#1K◆支援課でぼーっとするキーアと？（テスト用）\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【変更しない】\x01",        # 0
            "【話している】\x01",        # 1
            "【話していない】\x01",      # 2
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
        (0, "loc_16EC"),
        (1, "loc_16F1"),
        (2, "loc_16F9"),
        (SWITCH_DEFAULT, "loc_1701"),
    )


    label("loc_16EC")

    Jump("loc_1701")

    label("loc_16F1")

    SetScenarioFlags(0x151, 6)
    Jump("loc_1701")

    label("loc_16F9")

    ClearScenarioFlags(0x151, 6)
    Jump("loc_1701")

    label("loc_1701")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x151, 6)), scpexpr(EXPR_END)), "loc_1797")

    #C0007
    ChrTalk(
        0x109,
        "#10105Fえ……\x02",
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x101,
        (
            "#00008F……そういえば、さっきはなんだか\x01",
            "ぼーっとしていたような気がするな。\x02\x03",

            "#00001F除幕式でなにかあったのかい？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17F2")

    label("loc_1797")


    #C0009
    ChrTalk(
        0x109,
        (
            "#10105Fえ……？\x01",
            "特にそうは思わなかったけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x101,
        "#00001F除幕式でなにかあったのかい？\x02",
    )

    CloseMessageWindow()

    label("loc_17F2")


    #C0011
    ChrTalk(
        0xD,
        (
            "#01500Fいえ、そんな大したことじゃ\x01",
            "ないとは思うんですけど……\x02\x03",

            "#01508F除幕式を見てたキーアちゃん、\x01",
            "何か呆然としていたような気がして。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x105,
        (
            "#10300Fふむ、オルキスタワーの大きさに\x01",
            "驚いていただけじゃないのかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xD,
        (
            "#01505Fあ……そういうこと\x01",
            "だったんでしょうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x101,
        (
            "#00003Fうーん、よく分からないけど\x01",
            "心に留めておくとするよ。\x02\x03",

            "#00000Fありがとう、シズクちゃん。\x01",
            "キーアのこと心配してくれてさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xD,
        (
            "#01500Fいえ、そんな……\x01",
            "すいません、私ったら\x01",
            "変なことを言ってしまって。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x150, 2)
    Jump("loc_1A7C")

    label("loc_19D1")


    #C0016
    ChrTalk(
        0xD,
        (
            "#01502F今日の除幕式は、\x01",
            "キーアちゃんのおかげで\x01",
            "とっても楽しかったです。\x02\x03",

            "いつか目が見えるようになったら、\x01",
            "またキーアちゃんと一緒に\x01",
            "オルキスタワーを見てみたいですね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A7C")

    Jump("loc_1B2C")

    label("loc_1A81")


    #C0017
    ChrTalk(
        0xD,
        (
            "#01502F今日の除幕式は、\x01",
            "キーアちゃんのおかげで\x01",
            "とっても楽しかったです。\x02\x03",

            "いつか目が見えるようになったら、\x01",
            "またキーアちゃんと一緒に\x01",
            "オルキスタワーを見てみたいですね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B2C")

    Jump("loc_1B3A")

    label("loc_1B31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1B3A")

    label("loc_1B3A")

    TalkEnd(0xD)
    Return()

    # Function_12_1367 end

    def Function_13_1B3E(): pass

    label("Function_13_1B3E")

    OP_4B(0xE, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C1B")

    #C0018
    ChrTalk(
        0xD,
        (
            "#01502Fミハイル君、もうすぐ\x01",
            "退院するんだってね。\x02\x03",

            "ふふ、おめでとう。\x01",
            "ずっと元気でいてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xE,
        (
            "うん……シズクちゃん、\x01",
            "今までありがとう。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xE,
        (
            "僕、ぜったい手紙書くから。\x01",
            "シズクちゃんも元気でね！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_1CA9")

    label("loc_1C1B")


    #C0021
    ChrTalk(
        0xD,
        (
            "#01502Fミハイル君が退院できて、\x01",
            "私も本当にうれしいな。\x02\x03",

            "いつか、お父さんと一緒に\x01",
            "レマンに遊びに行くね。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xE,
        (
            "うん……！\x01",
            "僕、待ってるよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CA9")

    OP_4C(0xE, 0xFF)
    Return()

    # Function_13_1B3E end

    def Function_14_1CAE(): pass

    label("Function_14_1CAE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1CBF")
    Jump("loc_1D62")

    label("loc_1CBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1CD0")
    Call(0, 13)
    Jump("loc_1D62")

    label("loc_1CD0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1CE1")
    Call(0, 29)
    Jump("loc_1D62")

    label("loc_1CE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1D62")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CFC")
    Call(0, 34)
    Jump("loc_1D62")

    label("loc_1CFC")


    #C0023
    ChrTalk(
        0xE,
        (
            "退院……\x01",
            "ほんとにこんな日が来るなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xE,
        (
            "は、はやくレマンの\x01",
            "お母さんたちに連絡しなくちゃ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D62")

    TalkEnd(0xFE)
    Return()

    # Function_14_1CAE end

    def Function_15_1D66(): pass

    label("Function_15_1D66")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1DFA")

    #C0025
    ChrTalk(
        0xF,
        (
            "#01400F《幻獣》の調査のこと、よろしく頼む。\x02\x03",

            "俺も明日には復帰して\x01",
            "加わる予定だが、それまでは\x01",
            "スコットたちを助けてやってくれ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E86")

    label("loc_1DFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E86")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C6, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E16")
    Call(0, 18)
    Jump("loc_1E86")

    label("loc_1E16")


    #C0026
    ChrTalk(
        0xF,
        (
            "#01400F閣下がシズクに会ってみたいと\x01",
            "言い出してな。\x02\x03",

            "#01403F……有り難い話だ。\x01",
            "感謝させてもらわなくてはな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E86")

    TalkEnd(0xFE)
    Return()

    # Function_15_1D66 end

    def Function_16_1E8A(): pass

    label("Function_16_1E8A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F3C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C6, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EA9")
    Call(0, 18)
    Jump("loc_1F3C")

    label("loc_1EA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EBB")
    Call(0, 17)
    Jump("loc_1F3C")

    label("loc_1EBB")


    #C0027
    ChrTalk(
        0x15,
        (
            "おおそうだ、あとで\x01",
            "セイランド君の様子も\x01",
            "是非見にいかなくてはな。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x15,
        (
            "会うのは久しぶりだし、\x01",
            "彼女も達者にしているといいが。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F3C")

    TalkEnd(0xFE)
    Return()

    # Function_16_1E8A end

    def Function_17_1F40(): pass

    label("Function_17_1F40")

    SetChrSubChip(0xD, 0x2)
    OP_4B(0x15, 0xFF)

    #C0029
    ChrTalk(
        0x15,
        (
            "そういえば、シズク君は\x01",
            "目を患っているんだったね。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x15,
        (
            "……不安はあるだろうが、\x01",
            "この病院の医師の腕は\x01",
            "信用に値するはずだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x15,
        (
            "時間はかかるかもしれないが、\x01",
            "完治を信じて根気強く\x01",
            "戦っていくのだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xD,
        (
            "#01505Fあ……\x01",
            "ありがとうございます。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 2)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0x15, 0x10)
    OP_4C(0x15, 0xFF)
    Return()

    # Function_17_1F40 end

    def Function_18_204C(): pass

    label("Function_18_204C")

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
        "#01505Fあ……支援課のみなさん？\x02",
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x15,
        "おや、君たちは……\x02",
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
            "#00005Fレ、レミフェリア公国の\x01",
            "アルバート大公閣下……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x109,
        "#10105Fそれに、アリオスさんまで……\x02",
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xF,
        (
            "#01403Fふむ、奇遇だな。\x02\x03",

            "#01400F閣下、彼らが以前話した\x01",
            "『特務支援課』の者たちです。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0038
    ChrTalk(
        0x15,
        "おお、そうだったのか。\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x15,
        "……はじめまして、支援課の諸君。\x02",
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x15,
        (
            "私の名はアルバート・フォン・バルトロメウス。\x01",
            "レミフェリアの国家元首を務めている者だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x15,
        (
            "これからもクロスベルの為、\x01",
            "一所懸命に頑張ってくれたまえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x101,
        "#00002Fよ、よろしくお願いします。\x02",
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x15,
        (
            "フフ、君たちのことは、\x01",
            "アリオス君から聞いていてね。\x01",
            "是非お会いしたいと思っていたのだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x15,
        "それと、エリィ君の方は久しぶりだね。\x02",
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x102,
        (
            "#00100Fふふ、お久しぶりです。\x01",
            "大公閣下もお元気そうで……\x02\x03",

            "#00103Fでも、ちょうど病院に\x01",
            "お見えになっていたとは\x01",
            "知りませんでした。\x02\x03",

            "#00105F今日は視察にいらっしゃって\x01",
            "いたんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x15,
        (
            "うむ、レミフェリア公国はこの病院の\x01",
            "スポンサーの１つだからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x15,
        (
            "話に聞いていたアリオス君の娘さんにも、\x01",
            "是非挨拶させてもらいたかったからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xD,
        "#01502Fあ、ありがとうございます、大公さま。\x02",
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xF,
        (
            "#01400Fそれに関しては、個人的には\x01",
            "もう少し護衛をつけさせて\x01",
            "頂きたかったところです。\x02\x03",

            "#01403F私とリムジンの運転士だけ、\x01",
            "というのはいかがなものかと……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x15, 0xF, 500)
    Sleep(300)

    #C0050
    ChrTalk(
        0x15,
        (
            "フフ、アリオス君のことを\x01",
            "信用しているからこそだと\x01",
            "思ってくれたまえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x15,
        (
            "それに、私の視察くらいで\x01",
            "ぞろぞろ護衛を連れて、病院の業務を\x01",
            "妨げるわけにもいかないからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x101,
        (
            "#00000F（アルバート大公……\x01",
            "  アリオスさんだけじゃなく、\x01",
            "  エリィとも知り合いだったんだな。）\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x109,
        (
            "#10100F（ええ、エリィさんやアリオスさん……\x01",
            "  それにセイランド教授とも\x01",
            "  以前から知り合いみたいですし。）\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x105,
        (
            "#10300F（フフ、思っていた以上に\x01",
            "  気さくな人物みたいだね。）\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x15, 0xB4, 0x1F4)
    Sleep(300)

    #C0055
    ChrTalk(
        0x15,
        (
            "ともかく、君たちのことは\x01",
            "私も応援させてもらっている。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x15,
        "今後とも頑張ってくれたまえ。\x02",
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x101,
        "#00000Fええ、ありがとうございます。\x02",
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x102,
        (
            "#00100F大公閣下も、今日はお気をつけて\x01",
            "お戻りになってくださいね。\x02\x03",

            "明日の通商会議、\x01",
            "私たちも応援させていただきます。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x15,
        "はは、是非とも頑張らせてもらうよ。\x02",
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

    # Function_18_204C end

    def Function_19_298B(): pass

    label("Function_19_298B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 1)), scpexpr(EXPR_END)), "loc_2A25")

    #C0060
    ChrTalk(
        0x8,
        (
            "#01900F警部には危ない所を\x01",
            "助けていただいて、本当に\x01",
            "感謝しきれませんよ～。\x02\x03",

            "#01909Fまた、折をみてお見舞いに\x01",
            "伺わせていただきますね！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D17")

    label("loc_2A25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_2BE7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B54")

    #C0061
    ChrTalk(
        0x8,
        (
            "#06400Fえっと、手帳とエニグマ、\x01",
            "歯ブラシセットに……\x02\x03",

            "#06405Fあっ、ほかの患者さんや\x01",
            "ナースさんたちにも\x01",
            "挨拶を済ませておかないと～！\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x101,
        (
            "#00000F（フランの身支度は\x01",
            "  もう少しかかりそうだな……）\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x105,
        (
            "#10404F（ま、こっちも先に\x01",
            "  お見舞いを済ませたほうが\x01",
            "  よさそうだね。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2BE2")

    label("loc_2B54")


    #C0064
    ChrTalk(
        0x8,
        (
            "#06405Fああ、ちゃんと制服にも\x01",
            "着替えておかないと……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x0, 500)

    #C0065
    ChrTalk(
        0x8,
        "#06401F……覗かないでくださいね～？\x02",
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x101,
        "#00012Fの、覗かないよ。\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0x5A, 0x0)

    label("loc_2BE2")

    Jump("loc_2D17")

    label("loc_2BE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 7)), scpexpr(EXPR_END)), "loc_2D17")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CFA")

    #C0067
    ChrTalk(
        0x8,
        "#11703Fすう……すう……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CC0")

    #C0068
    ChrTalk(
        0x105,
        "#10300Fフフ、よく眠れてるみたいだね。\x02",
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x136,
        (
            "#01302F大丈夫よ、ノエルさん。\x01",
            "この調子ならすぐ元気になるから。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x109,
        "#10102Fはい……ありがとうございます。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2CF2")

    label("loc_2CC0")


    #C0071
    ChrTalk(
        0x109,
        (
            "#10103F（フラン……\x01",
            "  早く元気になってね。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CF2")

    SetScenarioFlags(0x0, 0)
    Jump("loc_2D17")

    label("loc_2CFA")


    #C0072
    ChrTalk(
        0x8,
        "#11703Fすう……すう……\x02",
    )

    CloseMessageWindow()

    label("loc_2D17")

    TalkEnd(0xFE)
    Return()

    # Function_19_298B end

    def Function_20_2D1B(): pass

    label("Function_20_2D1B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2DD1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AC, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D39")
    Call(0, 21)
    Jump("loc_2DCC")

    label("loc_2D39")


    #C0073
    ChrTalk(
        0x9,
        (
            "これから警察に合流するが……\x01",
            "ま、無理はしない範囲で\x01",
            "なんとか手伝っていくつもりだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x9,
        (
            "お前たちもかなり大変そうだが、\x01",
            "十分に気をつけていけ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DCC")

    Jump("loc_3341")

    label("loc_2DD1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_2F5F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2EBE")

    #C0075
    ChrTalk(
        0x9,
        (
            "独立国の無効宣言か……\x01",
            "まさかお前達が\x01",
            "ここまでやるとはな。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x9,
        (
            "市内にいるセルゲイたちも、\x01",
            "この機に乗じて\x01",
            "動き出してるはずだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x9,
        (
            "こうなっちまったら\x01",
            "俺もしばらくは合流できん。\x01",
            "……後は任せたぞ、お前ら。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2F5A")

    label("loc_2EBE")


    #C0078
    ChrTalk(
        0x9,
        (
            "市内にいるセルゲイたちも、\x01",
            "この機に乗じて動き出してると\x01",
            "みていいだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x9,
        (
            "こうなっちまったら\x01",
            "俺もしばらくは合流できん。\x01",
            "……後は任せたぞ、お前ら。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F5A")

    Jump("loc_3341")

    label("loc_2F5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_3010")

    #C0080
    ChrTalk(
        0x9,
        (
            "ともかく、俺もすぐには\x01",
            "警察に合流できそうもないし\x01",
            "しばらくは体を休めているとしよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x9,
        (
            "それまではレイモンドやセルゲイ達に\x01",
            "なんとか頑張ってもらわないとな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3341")

    label("loc_3010")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 1)), scpexpr(EXPR_END)), "loc_3095")

    #C0082
    ChrTalk(
        0x9,
        (
            "はは、俺も無事だったんだし\x01",
            "気にする事はねえだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x9,
        (
            "お前さんも\x01",
            "病み上がりなんだから、\x01",
            "気をつけて行くんだぞ？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3341")

    label("loc_3095")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_3117")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30B0")
    Call(0, 21)
    Jump("loc_3112")

    label("loc_30B0")


    #C0084
    ChrTalk(
        0x9,
        (
            "まあ、とにかく……\x01",
            "気をつけて行くんだぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x9,
        (
            "セルゲイ達とも近いうちに\x01",
            "合流できるといいな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3112")

    Jump("loc_3341")

    label("loc_3117")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 0)), scpexpr(EXPR_END)), "loc_3341")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3321")

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
            "#10108F……警部が目覚めたら、\x01",
            "フランを庇っていただいたことを\x01",
            "改めてお礼しなくちゃいけません。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32E3")

    #C0088
    ChrTalk(
        0x136,
        (
            "#01303F呼吸器系にかなりの\x01",
            "ダメージを受けてるから、\x01",
            "回復は遅いかもしれない……\x02\x03",

            "#01300Fでも、山は超えてるし\x01",
            "きっと近い内に\x01",
            "目を覚ましてくれるはずよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x102,
        (
            "#00103Fだといいですね……\x02\x03",

            "#00100F……後はレイモンドさんに\x01",
            "任せて大丈夫そうだし、\x01",
            "行きましょう、ロイド。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x101,
        "#00000Fああ、そうしよう。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3319")

    label("loc_32E3")


    #C0091
    ChrTalk(
        0x101,
        (
            "#00003Fそうだな……\x01",
            "早く良くなるといいんだけど。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3319")

    SetScenarioFlags(0x0, 1)
    Jump("loc_3341")

    label("loc_3321")


    #C0092
    ChrTalk(
        0x9,
        "#90W……………………………\x02",
    )

    CloseMessageWindow()

    label("loc_3341")

    TalkEnd(0xFE)
    Return()

    # Function_20_2D1B end

    def Function_21_3345(): pass

    label("Function_21_3345")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3674")
    OP_4B(0x9, 0xFF)
    OP_4B(0x16, 0xFF)

    def lambda_335B():
        TurnDirection(0x0, 0x9, 0)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_335B)
    Sleep(0)

    def lambda_336B():
        TurnDirection(0x1, 0x9, 0)
        ExitThread()

    QueueWorkItem(0x1, 0, lambda_336B)
    Sleep(0)

    def lambda_337B():
        TurnDirection(0x2, 0x9, 0)
        ExitThread()

    QueueWorkItem(0x2, 0, lambda_337B)
    Sleep(0)

    def lambda_338B():
        TurnDirection(0x3, 0x9, 0)
        ExitThread()

    QueueWorkItem(0x3, 0, lambda_338B)
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
        "おう、お前らか。\x02",
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x16,
        "うふふ、こんにちは。\x02",
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x101,
        "#00000Fドノバン警部……！\x02",
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x103,
        "#00200Fもう動いて大丈夫なんですか？\x02",
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x9,
        (
            "おう、さっき退院の手続きを\x01",
            "済ませてきたところだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x9,
        (
            "クロスベル市の解放作戦は\x01",
            "上手くいったみたいだし、\x01",
            "俺も警察に合流しようと思ってな。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x16,
        (
            "本当は退院予定日は何日か\x01",
            "先だったんだけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x16,
        (
            "無理はさせたくないけど、\x01",
            "どうしてもっていうから\x01",
            "折れてあげることにしたの。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x104,
        (
            "#00309Fハハ、レイモンドの奴が\x01",
            "喜びそうだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x102,
        (
            "#00100F警部が合流すれば、\x01",
            "捜査二課もより力を\x01",
            "発揮できそうですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x9,
        (
            "ま、無理はしない範囲で\x01",
            "なんとか手伝っていくつもりだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x9,
        (
            "お前たちもかなり大変そうだが、\x01",
            "十分に気をつけていけ。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x101,
        "#00000Fはい、ありがとうございます！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1AC, 7)
    TurnDirection(0x9, 0x16, 0)
    TurnDirection(0x16, 0x9, 0)
    OP_4C(0x9, 0xFF)
    OP_4C(0x16, 0xFF)
    Jump("loc_3A24")

    label("loc_3674")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_3A24")

    def lambda_3682():
        TurnDirection(0x0, 0x9, 0)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_3682)
    Sleep(0)

    def lambda_3692():
        TurnDirection(0x1, 0x9, 0)
        ExitThread()

    QueueWorkItem(0x1, 0, lambda_3692)
    Sleep(0)

    def lambda_36A2():
        TurnDirection(0x2, 0x9, 0)
        ExitThread()

    QueueWorkItem(0x2, 0, lambda_36A2)
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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_374A")
    Jump("loc_3794")

    label("loc_374A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_376A")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3794")

    label("loc_376A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_378A")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3794")

    label("loc_378A")

    OP_52(0x9, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3794")

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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x16, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x16, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x16, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x16, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_384A")
    Jump("loc_3894")

    label("loc_384A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x16, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_386A")
    OP_52(0x16, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3894")

    label("loc_386A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x16, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_388A")
    OP_52(0x16, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3894")

    label("loc_388A")

    OP_52(0x16, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x16, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3894")

    OP_52(0x16, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x16, 0x10)

    #C0106
    ChrTalk(
        0x9,
        (
            "やれやれ、恥ずかしい所を\x01",
            "見られちまったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x9,
        (
            "ファラには結婚以来、\x01",
            "ペースを掴まれっぱなしでな……\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x101,
        "#00000Fはは、いい奥さんじゃないですか。\x02",
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x105,
        "#10402Fフフ、とっても可愛らしいしね。\x02",
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x16,
        "まあ……♪\x02",
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x16,
        (
            "ふふっ、可愛らしいですって。\x01",
            "聞いたわよね、あなた㈱\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x9,
        (
            "（……こいつらやレイモンドの前でも\x01",
            "  この調子だから困るんだよな……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 0)
    SetChrSubChip(0x9, 0x0)
    SetChrSubChip(0x16, 0x0)
    ClearChrFlags(0x9, 0x10)
    ClearChrFlags(0x16, 0x10)

    label("loc_3A24")

    Return()

    # Function_21_3345 end

    def Function_22_3A25(): pass

    label("Function_22_3A25")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 0)), scpexpr(EXPR_END)), "loc_3BAC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B12")

    #C0113
    ChrTalk(
        0xA,
        (
            "せっかくドノバン警部に\x01",
            "命を助けてもらったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xA,
        (
            "不甲斐ない僕だけど……\x01",
            "これからは、もっとしっかり\x01",
            "しなくちゃいけないな。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0xA,
        (
            "いつか警部の部下として\x01",
            "恥ずかしくない、\x01",
            "立派な捜査官にならなくちゃね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3BAC")

    label("loc_3B12")


    #C0116
    ChrTalk(
        0xA,
        (
            "不甲斐ない僕だけど……\x01",
            "これからは、もっとしっかり\x01",
            "しなくちゃいけないな。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xA,
        (
            "いつか警部の部下として\x01",
            "恥ずかしくない、\x01",
            "立派な捜査官にならなくちゃね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3BAC")

    TalkEnd(0xFE)
    Return()

    # Function_22_3A25 end

    def Function_23_3BB0(): pass

    label("Function_23_3BB0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_426D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AD, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F4A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E7D")

    #C0118
    ChrTalk(
        0xB,
        (
            "#11601F弟君たち……\x01",
            "どうやら大変なことに\x01",
            "なってるみたいね。\x02\x03",

            "#11606F何だか得体の知れない\x01",
            "《大樹》みたいなものが\x01",
            "現れたんですって？\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x101,
        (
            "#00001Fええ……正直言って、\x01",
            "何が起こるか分からない状況です。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x102,
        (
            "#00103F病院も、決して安全とは\x01",
            "言えないかもしれません。\x02\x03",

            "#00101Fイリアさんも気をつけてください。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xB,
        (
            "#11609Fアハハ、ありがと。\x01",
            "あたしもあまり事情には\x01",
            "詳しくないけど……\x02\x03",

            "#11600F弟君たちだったら、\x01",
            "諦めなければきっとやり遂げられる。\x01",
            "必ず大切なモノを掴めるはずよ。\x02\x03",

            "#11604Fあたしも、また舞台に立つまで、\x01",
            "絶対に諦めたりしない……\x02\x03",

            "#11609Fだから、あなたたちも\x01",
            "最後まで頑張ってちょうだい。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x103,
        "#00200Fはい……！\x02",
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x104,
        (
            "#00309Fイリアさんの応援があれば\x01",
            "百人力ッス！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_END)), "loc_3E75")
    Call(0, 77)
    Return()

    label("loc_3E75")

    SetScenarioFlags(0x0, 3)
    Jump("loc_3F45")

    label("loc_3E7D")


    #C0124
    ChrTalk(
        0xB,
        (
            "#11604F弟君たちだったら、\x01",
            "諦めなければきっとやり遂げられる。\x01",
            "必ず大切なモノをつかめるはずよ。\x02\x03",

            "#11609Fあたしも、また舞台に立つまで、\x01",
            "絶対に諦めたりしない……\x01",
            "だから、最後まで頑張ってちょうだい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F45")

    Jump("loc_4268")

    label("loc_3F4A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x6C), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AD, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3F65")
    Call(0, 86)
    Jump("loc_4268")

    label("loc_3F65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_41A0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_END)), "loc_409D")

    #C0125
    ChrTalk(
        0xB,
        (
            "#11600F弟君たちだったら、\x01",
            "諦めなければきっとやり遂げられる。\x01",
            "必ず大切なモノをつかめるはずよ。\x02\x03",

            "#11604Fあたしも、また舞台に立つまで、\x01",
            "絶対に諦めたりしない……\x01",
            "だから、最後まで頑張ってちょうだい。\x02\x03",

            "#11609Fフフ、外に立っているその子#6R㈲　㈲　㈲#のことも、\x01",
            "どうかよろしくたのんだわね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4198")

    label("loc_409D")


    #C0126
    ChrTalk(
        0xB,
        (
            "#11600F弟君たちだったら、\x01",
            "諦めなければきっとやり遂げられる。\x01",
            "必ず大切なモノをつかめるはずよ。\x02\x03",

            "#11604Fあたしも、また舞台に立つまで、\x01",
            "絶対に諦めたりしない……\x01",
            "だから、最後まで頑張ってちょうだい。\x02\x03",

            "#11609Fフフ、あの子#6R㈲　㈲　㈲#にもよろしくね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4198")

    SetScenarioFlags(0x0, 3)
    Jump("loc_4268")

    label("loc_41A0")


    #C0127
    ChrTalk(
        0xB,
        (
            "#11604F弟君たちだったら、\x01",
            "諦めなければきっとやり遂げられる。\x01",
            "必ず大切なモノをつかめるはずよ。\x02\x03",

            "#11609Fあたしも、また舞台に立つまで、\x01",
            "絶対に諦めたりしない……\x01",
            "だから、最後まで頑張ってちょうだい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4268")

    Jump("loc_4CE1")

    label("loc_426D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_45E3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CF, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4537")

    #C0128
    ChrTalk(
        0xB,
        (
            "#11603F弟君、街で大変なことが\x01",
            "起こったって噂だけど……\x02\x03",

            "#11601F数ヶ月前の襲撃事件の真相が、\x01",
            "電撃報道されたんですって？\x02\x03",

            "詳しい情報は規制されて\x01",
            "流れてこなかったみたいだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x101,
        "#00001Fイリアさん……\x02",
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x102,
        (
            "#00108F（イリアさんにとっては、\x01",
            "  大怪我を負った根本的な\x01",
            "  原因になる話だけど……）\x02",
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
            "#11603F……ま、今さらあの事件の\x01",
            "真相になんてキョーミないわ。\x02\x03",

            "#11600Fそんなことより、\x01",
            "次のリハビリはいつかしら？\x02\x03",

            "#11609F舞台に復帰するためにも、\x01",
            "早く体を動かしたくて\x01",
            "ウズウズしてるんだけど♪\x02",
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
        "#00012Fはは、なんというか……\x02",
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x103,
        "#00202Fさすがイリアさんです。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1CF, 2)
    Jump("loc_45DE")

    label("loc_4537")


    #C0134
    ChrTalk(
        0xB,
        (
            "#11602Fガンガンリハビリをこなして\x01",
            "絶対に舞台に復帰するんだから、\x01",
            "他の事になんか興味ナシよ。\x02\x03",

            "#11609Fあ～あ、次のリハビリはまだかしらね。\x01",
            "早く体を動かしたいわ～♪\x02",
        )
    )

    CloseMessageWindow()

    label("loc_45DE")

    Jump("loc_4CE1")

    label("loc_45E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_4966")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48C2")

    #C0135
    ChrTalk(
        0xB,
        (
            "#11600Fセイランド先生によれば\x01",
            "歩けるようになるかどうか\x01",
            "現時点では分からないらしいけど……\x02\x03",

            "#11604F可能性はないわけじゃないし、\x01",
            "諦める理由になんかならないわよね。\x02\x03",

            "#11602Fなんたって、人は大切なモノのためなら\x01",
            "どこまでも頑張れる生き物だから。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_480B")

    #C0136
    ChrTalk(
        0x103,
        (
            "#00200Fイリアさんを見ていると\x01",
            "本当にそう思えてきますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xB,
        (
            "#11604Fフフ、弟君たち。\x01",
            "リーシャに会ったら伝えておいて。\x02\x03",

            "#11600F『その大切なものを前にして\x01",
            "  頑張らずにいられるの？』ってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x101,
        (
            "#00000Fええ、分かりました。\x01",
            "会うことができたら、\x01",
            "必ずその言葉を伝えます。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_48BA")

    label("loc_480B")


    #C0139
    ChrTalk(
        0x101,
        (
            "#00008F（リーシャにイリアさんからの\x01",
            "  メッセージは伝えたけど……\x01",
            "  まだ会える状態じゃなさそうだ。）\x02\x03",

            "#00003F（現時点ではリーシャのこと、\x01",
            "  黙っていた方がよさそうだな。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_48BA")

    SetScenarioFlags(0x0, 3)
    Jump("loc_4961")

    label("loc_48C2")


    #C0140
    ChrTalk(
        0xB,
        (
            "#11604F人は大切なモノのためなら\x01",
            "どこまでも頑張れる生き物よ。\x02\x03",

            "#11600Fまた歩けるようになる可能性は\x01",
            "ないわけじゃないし、\x01",
            "諦める理由になんかならないわよね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4961")

    Jump("loc_4CE1")

    label("loc_4966")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_4BBA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B2B")

    #C0141
    ChrTalk(
        0xB,
        (
            "#11600F街にいるアルカンシェルの\x01",
            "みんなのことも心配なのよね。\x02\x03",

            "#11609Fま、みんなのことだから\x01",
            "こんな状況でも練習してるはずだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x101,
        "#00000Fはは、そういう心配ですか。\x02",
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x103,
        (
            "#00202Fアルカンシェルの人たちなら\x01",
            "きっと練習に打ち込んでそうです。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x105,
        (
            "#10400Fフフ、なんたってみんな\x01",
            "アーティストだもんね。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0xB,
        (
            "#11604Fフフ、シュリなんかも伸び盛りだし……\x02\x03",

            "#11609Fあたしが復帰した時のためにも、\x01",
            "しっかり練習しといてくれないとね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4BB5")

    label("loc_4B2B")


    #C0146
    ChrTalk(
        0xB,
        (
            "#11600F街にいるアルカンシェルの\x01",
            "みんなのことも心配なのよね。\x02\x03",

            "#11609Fあたしが復帰した時のためにも\x01",
            "しっかり練習しといてくれないとね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4BB5")

    Jump("loc_4CE1")

    label("loc_4BBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 1)), scpexpr(EXPR_END)), "loc_4CE1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4CBA")

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
            "#00306F……しかし、イリアさんの\x01",
            "こんな姿を見る事になるとはな。\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x103,
        (
            "#00208Fそうですね……\x01",
            "いまだに現実味が沸きません。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x101,
        (
            "#00003Fイリアさんはきっと戻ってくる。\x01",
            "……今はそう信じよう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4CE1")

    label("loc_4CBA")


    #C0151
    ChrTalk(
        0xB,
        "#11603F#90W……………………………\x02",
    )

    CloseMessageWindow()

    label("loc_4CE1")

    TalkEnd(0xFE)
    Return()

    # Function_23_3BB0 end

    def Function_24_4CE5(): pass

    label("Function_24_4CE5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4EAA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4DE4")

    #C0152
    ChrTalk(
        0xC,
        (
            "#04200Fアンタら……\x01",
            "リーシャ姉のこと、\x01",
            "よろしく頼むな。\x02\x03",

            "#04203Fリーシャ姉が戻ってくれば、\x01",
            "イリアさんも元気になる……\x01",
            "そんな気がするんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x101,
        (
            "#00000F……ああ、待っていてくれ。\x01",
            "きっと俺たちが見つけ出して\x01",
            "みせるからさ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4EAA")

    label("loc_4DE4")


    #C0154
    ChrTalk(
        0xC,
        (
            "#04203Fリーシャ姉が戻ってくれば、\x01",
            "イリアさんも元気になる……\x01",
            "そんな気がするんだ。\x02\x03",

            "#04200Fそれまでは、何とかアルカンシェル#14R　オ　　　レ　　　た　　　ち　#が\x01",
            "イリアさんを支えていかないとな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4EAA")

    TalkEnd(0xFE)
    Return()

    # Function_24_4CE5 end

    def Function_25_4EAE(): pass

    label("Function_25_4EAE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4EBF")
    Jump("loc_5187")

    label("loc_4EBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_5009")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F98")

    #C0155
    ChrTalk(
        0x10,
        (
            "そろそろ足りない物資の支給を\x01",
            "頼まなきゃならないんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x10,
        (
            "独立国の無効宣言を受けて、\x01",
            "国防軍の人たちは部隊に\x01",
            "戻ってしまってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0x10,
        (
            "うーむ、困ったな。\x01",
            "これから交渉はどうすれば……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_5004")

    label("loc_4F98")


    #C0158
    ChrTalk(
        0x10,
        (
            "うーむ、困ったな。\x01",
            "国防軍が帰ってしまった。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x10,
        (
            "これから物資の支給の交渉は\x01",
            "どうすればいいんだろう……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5004")

    Jump("loc_5187")

    label("loc_5009")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_5017")
    Jump("loc_5187")

    label("loc_5017")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_5025")
    Jump("loc_5187")

    label("loc_5025")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5187")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_510A")

    #C0160
    ChrTalk(
        0x10,
        (
            "以前、病院が襲われたとき\x01",
            "このリネン室に隠れた人が\x01",
            "いたらしくてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x10,
        (
            "あの事件の時は、\x01",
            "僕はお腹を銃で撃たれて\x01",
            "しまったんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x10,
        (
            "今思えば、僕も早く\x01",
            "隠れるべきだったな。\x01",
            "うーん、失敗したよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_5187")

    label("loc_510A")


    #C0163
    ChrTalk(
        0x10,
        (
            "以前、病院が襲われたとき\x01",
            "僕は銃で撃たれてしまってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0x10,
        (
            "今思えば、僕も早く\x01",
            "隠れるべきだったな。\x01",
            "うーん、失敗したよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5187")

    TalkEnd(0xFE)
    Return()

    # Function_25_4EAE end

    def Function_26_518B(): pass

    label("Function_26_518B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_519C")
    Jump("loc_5F17")

    label("loc_519C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_51AA")
    Jump("loc_5F17")

    label("loc_51AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_51B8")
    Jump("loc_5F17")

    label("loc_51B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_5766")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AC, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_55BC")
    TurnDirection(0x11, 0x0, 0)

    #C0165
    ChrTalk(
        0x11,
        (
            "#01309Fそれにしても……シズクちゃんも\x01",
            "元気にしているといいけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x103,
        (
            "#00203F……ええ、本当に。\x02\x03",

            "#00200Fキーアもすごく\x01",
            "心配していましたし。\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x101,
        (
            "#00008F普通に考えれば、\x01",
            "今はオルキスタワーに\x01",
            "いるはずなんだよな。\x02\x03",

            "#00003Fシズクちゃんとも\x01",
            "なんとか会えるといいけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0x11,
        (
            "#01302Fロイドたちも……\x01",
            "支援課の皆が、早く全員\x01",
            "揃ってくれればいいわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x105,
        (
            "#10406Fまあ正直、道のりは\x01",
            "かなり厳しいだろうけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x101,
        (
            "#00003F……キーアを取り戻すには\x01",
            "絶対に皆の力が必要になるはずだ。\x02\x03",

            "#00000Fだったらどんなに苦しくても\x01",
            "諦めずに進んでみせるさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x11,
        (
            "#01309Fふふ、ロイドたちならきっとやれるわ。\x02\x03",

            "#01304F私もここで、女神様にお祈りをしてるから。\x01",
            "……どうか、頑張ってちょうだい。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x101,
        (
            "#00000Fありがとう、セシル姉。\x01",
            "そう言ってもらえると百人力だよ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_55AD")

    #C0173
    ChrTalk(
        0x107,
        (
            "#01200F#13C……………………………………\x02\x03",

            "（やはりおぬしの血筋だな……\x01",
            "  ──ウルスラよ。）\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x107, 500)

    #C0174
    ChrTalk(
        0x103,
        (
            "#00205Fツァイト……\x01",
            "どうかしましたか？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x103, 500)

    #C0175
    ChrTalk(
        0x107,
        (
            "#01203F#13C……フフ、気にするな。\x01",
            "私にも物思いに耽ることが\x01",
            "あるということだ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_55AD")

    OP_93(0x11, 0x5A, 0x0)
    SetScenarioFlags(0x1AC, 2)
    Jump("loc_5761")

    label("loc_55BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_56AE")
    SetChrSubChip(0xB, 0x2)

    #C0176
    ChrTalk(
        0x11,
        (
            "#01300Fイリア、そろそろ\x01",
            "リハビリに行きましょうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0xB,
        (
            "#11604Fん、了解。\x02\x03",

            "#11609F今日もよろしく頼むわね、\x01",
            "セシル看護主任サン㈱\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x11,
        (
            "#01309Fふふ、イリアとみんなのためだもの。\x01",
            "しっかりと手伝わせてもらうわ。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x11, 0x10)
    SetChrSubChip(0xB, 0x0)
    SetScenarioFlags(0x0, 7)
    Jump("loc_5761")

    label("loc_56AE")


    #C0179
    ChrTalk(
        0x11,
        (
            "#01302Fロイドたちなら\x01",
            "きっと支援課のみんなを助け出して、\x01",
            "キーアちゃんとの再会を果たせるはずよ。\x02\x03",

            "#01304F私もここで女神様にお祈りをしてるわ。\x01",
            "……どうか、頑張ってちょうだい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5761")

    Jump("loc_5F17")

    label("loc_5766")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_5774")
    Jump("loc_5F17")

    label("loc_5774")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5782")
    Jump("loc_5F17")

    label("loc_5782")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5793")
    Call(0, 27)
    Jump("loc_5F17")

    label("loc_5793")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_57A4")
    Call(0, 27)
    Jump("loc_5F17")

    label("loc_57A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_57B2")
    Jump("loc_5F17")

    label("loc_57B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5B46")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x151, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5ADE")
    OP_63(0x11, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x11, 0x103, 500)

    #C0180
    ChrTalk(
        0x11,
        (
            "#01302Fあら、ティオちゃんじゃない。\x01",
            "支援課に戻ってきてたのね。\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0x103,
        "#00202Fええ、つい昨日戻った所です。\x02",
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0x11,
        (
            "#01309Fふふ、また会えて嬉しいわ。\x02\x03",

            "#01304Fとても忙しかったって\x01",
            "聞いているけど……\x01",
            "うん、今日は顔色はいいわね。\x02\x03",

            "#01300Fまた前みたいに\x01",
            "倒れたりしないように、\x01",
            "体調には気をつけてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x103,
        (
            "#00204Fふふ、その節は\x01",
            "お世話になりました。\x02\x03",

            "#00200Fまあ、またセシルさんの\x01",
            "柔らかいベッドで眠れるのなら、\x01",
            "倒れるのにもやぶさかでないですが。\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0x104,
        "#00309Fうむ、その点には全く同意だな。\x02",
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0x101,
        "#00006Fランディ、あのなあ……\x02",
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0x102,
        "#00106F少しは自重してちょうだい。\x02",
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0x11,
        (
            "#01302Fふふ……\x01",
            "すっかり前の調子が\x01",
            "戻ってきたみたいね。\x02\x03",

            "#01304Fティオちゃんが戻ってきて、\x01",
            "支援課もようやく\x01",
            "完全始動ってところかしら。\x02\x03",

            "#01309Fずっと応援してるから、\x01",
            "これからもがんばってね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x151, 5)
    ClearChrFlags(0x11, 0x10)
    Jump("loc_5B41")

    label("loc_5ADE")


    #C0188
    ChrTalk(
        0x11,
        (
            "#01300Fミハイル君、もうすぐ退院なの。\x02\x03",

            "#01304F少し寂しくなるけど……\x01",
            "ふふ、本当によかったわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5B41")

    Jump("loc_5F17")

    label("loc_5B46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5B57")
    Call(0, 29)
    Jump("loc_5F17")

    label("loc_5B57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5F17")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x150, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E90")

    #C0189
    ChrTalk(
        0x101,
        (
            "#00000Fあ……\x01",
            "セシル姉、ここにいたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0x102,
        (
            "#00100Fここは確か、\x01",
            "シズクちゃんの病室ですよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0x11,
        (
            "#01300Fええ、外出中だから\x01",
            "今のうちにお掃除をね。\x02\x03",

            "#01304F今日はシズクちゃん、\x01",
            "街のほうに遊びに行っているのよね。\x02\x03",

            "#01309F少し前から\x01",
            "『キーアちゃんに会える』って\x01",
            "とっても嬉しそうに話してたのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0x104,
        (
            "#00309Fはは、ほんといい友達に\x01",
            "なったもんッスね。\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0x101,
        (
            "#00000Fまあ、相手がキーアだからな。\x01",
            "当然と言えば当然だよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0x105,
        (
            "#10304Fフフ、確かにキーアには、\x01",
            "人と仲良くなる才能みたいなのが\x01",
            "備わってる気さえするよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0x109,
        "#10102Fクスクス……言えてるかも。\x02",
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x11,
        (
            "#01300Fおかげでシズクちゃんも\x01",
            "以前より明るくなってくれたし……\x01",
            "キーアちゃんには感謝してるわ。\x02\x03",

            "#01302F今度また休みがとれたら、\x01",
            "私のほうから遊びに行きたいわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0x101,
        "#00000Fああ、キーアもきっと喜ぶよ。\x02",
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x11,
        "#01309Fふふ、そのときはよろしくね。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x150, 1)
    Jump("loc_5F17")

    label("loc_5E90")


    #C0199
    ChrTalk(
        0x11,
        (
            "#01300Fシズクちゃん、\x01",
            "今頃はキーアちゃんと\x01",
            "遊んでいる頃かしら。\x02\x03",

            "#01309Fふふ、せっかくの外出日だし\x01",
            "存分に楽しんできてほしいわね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5F17")

    TalkEnd(0xFE)
    Return()

    # Function_26_518B end

    def Function_27_5F1B(): pass

    label("Function_27_5F1B")

    SetChrSubChip(0xD, 0x2)
    OP_4B(0x11, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_619D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_60CC")

    #C0200
    ChrTalk(
        0xD,
        (
            "#11200Fセシルさん……\x01",
            "昨日はたくさん救急車が\x01",
            "動いていたみたいですね。\x02\x03",

            "#11210F大きな事故があったって\x01",
            "耳に挟んだんですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0x11,
        (
            "#01303Fどうも、西クロスベル街道で\x01",
            "列車が脱線したみたいなの。\x02\x03",

            "#01302Fでも、安心して。\x01",
            "先生たちのおかげで犠牲者は\x01",
            "ゼロだったみたいだから。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0xD,
        (
            "#11202Fそうですか……よかったです。\x02\x03",

            "#11208F私のときみたいな\x01",
            "酷い事故だったらと思うと……\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0x11,
        "#01308Fシズクちゃん……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_6198")

    label("loc_60CC")


    #C0204
    ChrTalk(
        0x11,
        (
            "#01300F先生たちががんばったおかげで\x01",
            "列車事故の患者さんたちは\x01",
            "みんな助かったわ。\x02\x03",

            "だから、事故のことは\x01",
            "心配しなくていいから。\x01",
            "今はリハビリに専念しましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0xD,
        "#11202Fはい……よろしくお願いします。\x02",
    )

    CloseMessageWindow()

    label("loc_6198")

    Jump("loc_638A")

    label("loc_619D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_638A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16B, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_61B8")
    Call(0, 28)
    Jump("loc_638A")

    label("loc_61B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_62F3")

    #C0206
    ChrTalk(
        0x11,
        (
            "#01304Fふふ、それじゃあ読んであげるわね。\x01",
            "……コホン。\x02\x03",

            "#01300F『シズクちゃん、おげんきですか。\x01",
            "  ぼくはげんきです。』\x02\x03",

            "『シズクちゃんの目が見えるように\x01",
            "  なるように、毎晩女神様に\x01",
            "  お祈りしています。』\x02\x03",

            "#01309Fふふ、あの子らしいわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0xD,
        (
            "#11202Fミハイル君……\x01",
            "……とっても、うれしいです。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_638A")

    label("loc_62F3")


    #C0208
    ChrTalk(
        0x11,
        (
            "#01304Fそうそう、それに写真が\x01",
            "同封されてたのよ。\x02\x03",

            "#01302Fふふ、ご両親に挟まれて、\x01",
            "とっても楽しそうなんだから。\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0xD,
        "#11209Fクスクス、いいなあ……\x02",
    )

    CloseMessageWindow()

    label("loc_638A")

    SetChrSubChip(0xD, 0x0)
    OP_4C(0x11, 0xFF)
    Return()

    # Function_27_5F1B end

    def Function_28_6393(): pass

    label("Function_28_6393")

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
        "#12P#00000Fやあセシル姉、シズクちゃん。\x02",
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0xD,
        "#11P#11202Fあ……こんにちは、皆さん。\x02",
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0x11,
        (
            "#5P#01300Fあら、ロイドたちじゃない。\x02\x03",

            "#01309Fふふ、シズクちゃんのお見舞いに\x01",
            "来てくれたのかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0x103,
        "#6P#00202Fええ、そんなところですが……\x02",
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0x109,
        (
            "#N#12P#10105Fえっと、もしかして\x01",
            "お邪魔だったでしょうか？\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_93(0x11, 0xB4, 0x1F4)

    #C0215
    ChrTalk(
        0x11,
        (
            "#5P#01302Fふふ、そんなことないわ。\x02\x03",

            "#01304F実は今日、レマン自治州に戻った\x01",
            "ミハイル君から手紙が来ててね。\x02\x03",

            "#01300Fこれからシズクちゃんと\x01",
            "読もうと思っていたところだったの。\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0x102,
        "#6P#00105Fミハイル君っていうと……\x02",
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0x105,
        (
            "#12P#10302Fセイランド先生が手術したっていう\x01",
            "男の子だったかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0xD,
        (
            "#11P#11204Fええ、私とも\x01",
            "とっても仲良くしてくれてた子で……\x02\x03",

            "#11200F退院するときに、お手紙をしようって\x01",
            "約束していたんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0x104,
        "#12P#00302Fハハ、そいつはよかったじゃねえか。\x02",
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0x11,
        (
            "#5P#01300Fウルスラ病院には\x01",
            "こうして退院した患者さんから\x01",
            "お手紙が届くことがあるのよね。\x02\x03",

            "#01304F忙しくてなかなか\x01",
            "お返事を書く時間が作れないけど……\x02\x03",

            "#01300F患者さんのその後も知れるし、\x01",
            "私の活力の源にもなっているわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0x101,
        (
            "#12P#00002Fはは、セシル姉のことだから\x01",
            "本当に一通一通しっかりと\x01",
            "返事を返してるんだろうなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0x103,
        (
            "#6P#00204F……私もマーサ師長にお手紙を\x01",
            "出していればよかったですね。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x11, 0xE1, 0x1F4)

    #C0223
    ChrTalk(
        0x11,
        (
            "#5P#01302Fふふ、師長はティオちゃんと\x01",
            "再会したとき本当に喜んでいたのよ。\x02\x03",

            "#01309F今からでも遅くないし、\x01",
            "機会があったら始めてみたらどうかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0x103,
        (
            "#6P#00202Fふふ、仕事が落ち着いたら\x01",
            "考えさせていただきます。\x02",
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

    # Function_28_6393 end

    def Function_29_69FC(): pass

    label("Function_29_69FC")

    SetChrSubChip(0xE, 0x1)
    OP_4B(0x11, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x150, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6C78")

    #C0225
    ChrTalk(
        0x11,
        "#01300Fミハイル君、調子はどう？\x02",
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0xE,
        (
            "うん、発作も全然出なくなったし、\x01",
            "苦しかったのがウソみたいだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0x11,
        (
            "#01304Fふふ、よかった。\x02\x03",

            "#01300F退院の日も近づいてきたし……\x01",
            "またお母さんたちと一緒に\x01",
            "過ごせるようになるわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0xE,
        (
            "……嬉しいのと寂しいのが\x01",
            "半分半分かな。\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0xE,
        (
            "レマン自治州に帰ったら、\x01",
            "セシルお姉ちゃんやシズクちゃんとも\x01",
            "離れ離れになっちゃうし……\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0x11,
        (
            "#01300F……長い間、\x01",
            "一緒に病気と闘ってきたものね。\x01",
            "確かにとっても寂しいけど……\x02\x03",

            "#01304F遠く離れていても、\x01",
            "この絆は切れることはない。\x01",
            "……私はそう思うわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0xE,
        "……うん、そうだね。\x02",
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0xE,
        (
            "セシルお姉ちゃん、今までありがと。\x01",
            "僕、絶対忘れないからね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x150, 3)
    Jump("loc_6D03")

    label("loc_6C78")


    #C0233
    ChrTalk(
        0x11,
        (
            "#01309Fふふ、退院の日は\x01",
            "きっと笑顔で迎えましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0xE,
        "うん、そうするよ。\x02",
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0xE,
        (
            "……シズクちゃんにも、\x01",
            "ちゃんとお別れを言わないとね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6D03")

    SetChrSubChip(0xE, 0x0)
    OP_4C(0x11, 0xFF)
    Return()

    # Function_29_69FC end

    def Function_30_6D0C(): pass

    label("Function_30_6D0C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_6D1D")
    Jump("loc_6E05")

    label("loc_6D1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_6DC4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6D38")
    Call(0, 31)
    Jump("loc_6DBF")

    label("loc_6D38")

    OP_4B(0x13, 0xFF)

    #C0236
    ChrTalk(
        0x12,
        (
            "うーん、昨日の空の感じじゃ\x01",
            "降らない気がしたんだけどなぁ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0x13,
        (
            "天気予報より\x01",
            "あんたのカンが当たったら\x01",
            "すごすぎるっつの。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x13, 0xFF)

    label("loc_6DBF")

    Jump("loc_6E05")

    label("loc_6DC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_6DD2")
    Jump("loc_6E05")

    label("loc_6DD2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_6DE0")
    Jump("loc_6E05")

    label("loc_6DE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_6DEE")
    Jump("loc_6E05")

    label("loc_6DEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_6DFC")
    Jump("loc_6E05")

    label("loc_6DFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_6E05")

    label("loc_6E05")

    TalkEnd(0xFE)
    Return()

    # Function_30_6D0C end

    def Function_31_6E09(): pass

    label("Function_31_6E09")

    OP_4B(0x12, 0xFF)
    OP_4B(0x13, 0xFF)

    #C0238
    ChrTalk(
        0x13,
        (
            "シロンあんた……\x01",
            "屋上にシーツ干したでしょ！\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0x13,
        (
            "天気予報じゃ雨だって、\x01",
            "事務長さんが言ってたじゃん！\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0x12,
        (
            "案外降らないかな～と思って。\x01",
            "えへへ、賭けてみました。\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x13,
        "何で、賭けてみちゃうのよっ！？\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x13, 0x10)
    SetScenarioFlags(0x1, 7)
    OP_4C(0x12, 0xFF)
    OP_4C(0x13, 0xFF)
    Return()

    # Function_31_6E09 end

    def Function_32_6EEB(): pass

    label("Function_32_6EEB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_6EFC")
    Jump("loc_7314")

    label("loc_6EFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_6F90")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6F17")
    Call(0, 31)
    Jump("loc_6F8B")

    label("loc_6F17")


    #C0242
    ChrTalk(
        0x13,
        (
            "まったく、せっかく洗ったシーツが\x01",
            "全部洗濯しなおしじゃない。\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0x13,
        (
            "って、そんなことより\x01",
            "早く取り込まないとっ！！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6F8B")

    Jump("loc_7314")

    label("loc_6F90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_6F9E")
    Jump("loc_7314")

    label("loc_6F9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_7197")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_70FC")

    #C0244
    ChrTalk(
        0x13,
        (
            "ミハイル君の退院の日、\x01",
            "元気に手を振るあの子を見て\x01",
            "私、感激して泣いちゃったのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0x13,
        (
            "そしたら、シロンが私に\x01",
            "黙ってハンカチを貸してくれてさ。\x01",
            "たまには気が利くなって思ったら……\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0x13,
        (
            "よく見ると、ハンカチじゃなくて\x01",
            "私が前に失くした\x01",
            "お気に入りのスカーフだったのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0x13,
        (
            "……ツッコみ所が多すぎて\x01",
            "感動ぶち壊しだったわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_7192")

    label("loc_70FC")


    #C0248
    ChrTalk(
        0x13,
        (
            "ま、それはおいといて……\x01",
            "ミハイル君、本当に\x01",
            "退院できてよかったわよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x13,
        (
            "今頃、レマン自治州で\x01",
            "お母さんたちと楽しく\x01",
            "暮らしてるんだろーなー……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7192")

    Jump("loc_7314")

    label("loc_7197")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_71A5")
    Jump("loc_7314")

    label("loc_71A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_71B3")
    Jump("loc_7314")

    label("loc_71B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_7314")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7271")

    #C0250
    ChrTalk(
        0x13,
        (
            "ここに入院してたゲバルさんって人、\x01",
            "だいぶ前に退院していったわよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x13,
        (
            "あの人、わがままばっかりで\x01",
            "本当に苦労させられたけど……\x01",
            "今頃どこで何してるのかしらね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_7314")

    label("loc_7271")


    #C0252
    ChrTalk(
        0x13,
        (
            "あー、そういえば今日は\x01",
            "シロンが点滴に行ってるんだっけ。\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x13,
        (
            "あの子、いっつもとんでもないミスを\x01",
            "やらかしちゃうから心配なのよ。\x01",
            "……後で様子を見に行こうかな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7314")

    TalkEnd(0xFE)
    Return()

    # Function_32_6EEB end

    def Function_33_7318(): pass

    label("Function_33_7318")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_7329")
    Jump("loc_73E9")

    label("loc_7329")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_7337")
    Jump("loc_73E9")

    label("loc_7337")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_7345")
    Jump("loc_73E9")

    label("loc_7345")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_7353")
    Jump("loc_73E9")

    label("loc_7353")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_7361")
    Jump("loc_73E9")

    label("loc_7361")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_736F")
    Jump("loc_73E9")

    label("loc_736F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_73E9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_738A")
    Call(0, 34)
    Jump("loc_73E9")

    label("loc_738A")


    #C0254
    ChrTalk(
        0x14,
        (
            "それにしても\x01",
            "セイランド教授……\x01",
            "素晴らしい腕前だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x14,
        (
            "私も彼女から学ぶ事は\x01",
            "多そうだな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_73E9")

    TalkEnd(0xFE)
    Return()

    # Function_33_7318 end

    def Function_34_73ED(): pass

    label("Function_34_73ED")

    SetChrSubChip(0xE, 0x1)
    OP_4B(0x14, 0xFF)

    #C0256
    ChrTalk(
        0x14,
        (
            "ふむ……\x01",
            "術後の経過もいいようだし、\x01",
            "近いうちに退院できるだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0x14,
        (
            "あとでレマン自治州のご両親に\x01",
            "連絡してあげなさい。\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0xE,
        "ほ、ほんとっ？\x02",
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0x14,
        "ああ、本当だとも。\x02",
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0x14,
        (
            "セイランド教授の腕もあるが、\x01",
            "何よりも手術を決断した君の勇気が\x01",
            "病気に打ち勝ったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0x14,
        "……よくがんばったね。\x02",
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0xE,
        (
            "……グスン……\x01",
            "ありがとう、先生……！\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x14, 0x10)
    ClearChrFlags(0xE, 0x10)
    SetScenarioFlags(0x1, 6)
    SetChrSubChip(0xE, 0x0)
    OP_4C(0x14, 0xFF)
    Return()

    # Function_34_73ED end

    def Function_35_7555(): pass

    label("Function_35_7555")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_762C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AC, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7573")
    Call(0, 21)
    Jump("loc_7627")

    label("loc_7573")


    #C0263
    ChrTalk(
        0x16,
        (
            "本当のこというと、退院予定日は\x01",
            "もう何日か先だったんだけど……\x01",
            "この人に頼み込まれちゃって。\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0x16,
        (
            "うふふ、でも本当は嬉しいのよ。\x01",
            "私はこの人が仕事をしている姿が\x01",
            "一番好きだから㈱\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7627")

    Jump("loc_7A9F")

    label("loc_762C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_77A1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x189, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_772F")

    #C0265
    ChrTalk(
        0x16,
        (
            "お見舞いに持ってきていた本、\x01",
            "すっかり読んでしまったわね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0x16,
        (
            "同じ本を何回も読んでも仕方ないし……\x01",
            "うん、あなたたちに\x01",
            "プレゼントしちゃおうかしら♪\x02",
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
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x2FA, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x189, 4)
    Jump("loc_779C")

    label("loc_772F")


    #C0268
    ChrTalk(
        0x16,
        (
            "病院に来ていた国防軍の人たちも、\x01",
            "み～んな帰っちゃったみたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0x16,
        "……何が起ころうとしているのかしら？\x02",
    )

    CloseMessageWindow()

    label("loc_779C")

    Jump("loc_7A9F")

    label("loc_77A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_795A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_78A9")

    #C0270
    ChrTalk(
        0x16,
        (
            "私は独立宣言のときに\x01",
            "お見舞いに来ていて、そのまま\x01",
            "こっちに滞在してたのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0x16,
        (
            "街との行き来に必要な申請が\x01",
            "どうしても面倒になっちゃってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0x16,
        (
            "この人とゆっくり過ごすのも\x01",
            "なかなか無かった機会だし、\x01",
            "この際だから楽しまないと損よね♪\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_7955")

    label("loc_78A9")


    #C0273
    ChrTalk(
        0x16,
        (
            "私は独立宣言のときに\x01",
            "お見舞いに来ていて、そのまま\x01",
            "こっちに滞在してたのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0x16,
        (
            "この人とゆっくり過ごすのも\x01",
            "なかなか無かった機会だし、\x01",
            "この際だから楽しまないと損よね♪\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7955")

    Jump("loc_7A9F")

    label("loc_795A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 1)), scpexpr(EXPR_END)), "loc_7A1C")

    #C0275
    ChrTalk(
        0x16,
        (
            "ふふ、この人ったら\x01",
            "もう若くないのに無茶ばっかりして……\x01",
            "フランさんにも心配をかけたわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0x16,
        (
            "でも、あなたみたいな\x01",
            "可愛い子を守れたんだから、\x01",
            "最高のファインプレーだったわね♪\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7A9F")

    label("loc_7A1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_7A9F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7A37")
    Call(0, 21)
    Jump("loc_7A9F")

    label("loc_7A37")


    #C0277
    ChrTalk(
        0x16,
        (
            "なんだか大変そうなのは\x01",
            "分かったけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0x16,
        (
            "今は無茶をしないように、\x01",
            "私がちゃんと見ていないとね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7A9F")

    TalkEnd(0xFE)
    Return()

    # Function_35_7555 end

    def Function_36_7AA3(): pass

    label("Function_36_7AA3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_7AB4")
    Jump("loc_8203")

    label("loc_7AB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_7AC2")
    Jump("loc_8203")

    label("loc_7AC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_7D28")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7C86")

    #C0279
    ChrTalk(
        0x17,
        (
            "独立国として外交を絶った事の\x01",
            "最大の痛手は、レミフェリアとの\x01",
            "連携がとれなくなったことだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0x17,
        (
            "ある程度の医療物資は、\x01",
            "大統領側に大量の備蓄が\x01",
            "用意されてあるようだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0x17,
        (
            "そもそも薬品というものは、\x01",
            "患者の症状や体質に合わせたものを\x01",
            "綿密に選択し、処方するものだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0x17,
        (
            "大統領が備蓄している程度の\x01",
            "薬品の種類では、全ての患者に\x01",
            "対応するのは難しいだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0x17,
        (
            "これから先どうしていくべきか……\x01",
            "何か方法を考える必要があるな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_7D23")

    label("loc_7C86")


    #C0284
    ChrTalk(
        0x17,
        (
            "大統領が備蓄している程度の\x01",
            "薬品の種類では、全ての患者に\x01",
            "対応するのは難しいだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0x17,
        (
            "これから先どうしていくべきか……\x01",
            "何か方法を考える必要があるな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7D23")

    Jump("loc_8203")

    label("loc_7D28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_8203")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AC, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8073")

    #C0286
    ChrTalk(
        0x17,
        "…………………………\x02",
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0x101,
        "#00005Fセイランド先生……？\x02",
    )

    CloseMessageWindow()
    OP_63(0x17, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x17, 0x0, 500)

    #C0288
    ChrTalk(
        0x17,
        "……君たちか、久しぶりだな。\x02",
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0x103,
        (
            "#00200Fここはシズクちゃんの病室でしたね。\x01",
            "……こんな所でなにを？\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0x17,
        (
            "主治医を担当していた患者なのでな。\x01",
            "少々物思いに耽っていたところだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0x17,
        (
            "……アリオス・マクレインによって\x01",
            "退院させられた後、どうしているかとな。\x02",
        )
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0x105,
        (
            "#10401Fそういえば、あれ以来\x01",
            "彼女とも会ってないね。\x02\x03",

            "#10403F多分、オルキスタワーのどこかで\x01",
            "保護されているんだろうけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0x17,
        (
            "……いくら父親とはいえ、\x01",
            "受け持ちの患者を奪われたのは\x01",
            "屈辱以外の何物でもない。\x02",
        )
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0x17,
        (
            "国防長官に赴任した\x01",
            "あの状況下なら、仕方ないのは\x01",
            "分かってはいるがな。\x02",
        )
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0x17,
        (
            "分かってはいるが……\x01",
            "納得など出来るはずもない。\x02",
        )
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0x101,
        "#00001F先生……\x02",
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0x17,
        (
            "……すまない、\x01",
            "無駄な話をしてしまったようだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0x17,
        (
            "見舞いの最中なのだろう？\x01",
            "……悪いが一人にしてくれないか。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1AC, 6)
    ClearChrFlags(0x17, 0x10)
    Jump("loc_8203")

    label("loc_8073")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_816E")

    #C0299
    ChrTalk(
        0x17,
        (
            "シズク・マクレイン……\x01",
            "彼女の治療方針は向こう１年まで\x01",
            "綿密に計画していたのだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0x17,
        (
            "……いくら父親とはいえ、\x01",
            "受け持ちの患者を奪われたのは\x01",
            "屈辱以外の何物でもない。\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0x17,
        (
            "退院した患者の事を引き摺っても\x01",
            "仕方ないのかもしれないがな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_8203")

    label("loc_816E")


    #C0302
    ChrTalk(
        0x17,
        (
            "……いくら父親とはいえ、\x01",
            "受け持ちの患者を奪われたのは\x01",
            "屈辱以外の何物でもない。\x02",
        )
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0x17,
        (
            "退院した患者の事を引き摺っても\x01",
            "仕方ないのかもしれないがな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8203")

    TalkEnd(0xFE)
    Return()

    # Function_36_7AA3 end

    def Function_37_8207(): pass

    label("Function_37_8207")

    Sound(160, 0, 100, 0)
    Return()

    # Function_37_8207 end

    def Function_38_820E(): pass

    label("Function_38_820E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CE, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_83CF")
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_82C3")
    SetChrPos(0x109, -16360, 0, 29320, 90)

    label("loc_82C3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_82E4")
    SetChrPos(0x105, -16360, 0, 29320, 90)

    label("loc_82E4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8305")
    SetChrPos(0x10A, -16360, 0, 29320, 90)

    label("loc_8305")

    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()

    #C0304
    ChrTalk(
        0x106,
        (
            "#10703F（……皆さん。\x01",
            "  入るなら、私はここで……）\x02",
        )
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0x101,
        "#00000F（……分かった。）\x02",
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0x104,
        "#00300F（ま、いつも通りに振舞うか。）\x02",
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
    Jump("loc_8433")

    label("loc_83CF")

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

    label("loc_8433")

    Return()

    # Function_38_820E end

    def Function_39_8434(): pass

    label("Function_39_8434")

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

    # Function_39_8434 end

    def Function_40_849C(): pass

    label("Function_40_849C")

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
        "#2P#2S──失礼します。\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x136, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Sound(107, 0, 100, 0)
    OP_68(5670, 1000, -47970, 2500)

    def lambda_8674():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8674)
    Sleep(200)

    def lambda_868C():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_868C)
    SetChrSubChip(0x8, 0x1)
    Sleep(100)

    def lambda_86A8():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_86A8)

    def lambda_86BD():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x136, 1, lambda_86BD)
    Sleep(50)

    def lambda_86CD():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_86CD)
    Sleep(50)

    def lambda_86E5():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_86E5)
    Sleep(50)

    def lambda_86FD():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_86FD)

    def lambda_8712():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8712)
    Sleep(200)

    def lambda_8726():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_8726)
    Sleep(500)

    def lambda_873A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_873A)

    def lambda_874B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_874B)
    Sleep(500)

    def lambda_875F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_875F)

    def lambda_8770():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_8770)
    WaitChrThread(0x101, 1)
    BeginChrThread(0x1A, 1, 0, 48)
    OP_C9(0x0, 0x80000000)

    #C0308
    ChrTalk(
        0x8,
        (
            "#11705F#2723V#5P#40Wあ……\x01",
            "お姉ちゃん、皆さん……！\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xAA3)
    OP_C9(0x1, 0x80000000)

    #C0309
    ChrTalk(
        0x136,
        "#01302F#11Pあら、みんな。\x02",
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0x101,
        "#00000F#6Pセシル姉、ここにいたんだ。\x02",
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0x109,
        (
            "#10113F#6P#Nすみません。\x01",
            "今、大丈夫でしょうか？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0312
    ChrTalk(
        0x136,
        (
            "#01309F#11Pふふ、大丈夫よ。\x01",
            "点滴を交換しただけだから。\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    OP_68(5920, 1000, -48010, 2000)

    def lambda_88A6():
        OP_9B(0x1, 0xFE, 0xE1, 0x6D6, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x136, 1, lambda_88A6)
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
            "#30Wえへへ……\x01",
            "ありがとうございますー。\x02\x03",

            "わざわざお見舞いに\x01",
            "来てくれたんですかー…？\x02",
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
            "#00002F#12Pああ、ノエルから\x01",
            "意識が戻ったって聞いてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0x102,
        (
            "#00109F#12Pふふ、思ったよりも\x01",
            "元気そうで安心したわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0x105,
        (
            "#10302F#6Pそうだね。\x01",
            "顔色も良さそうじゃない？\x02",
        )
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0x8,
        (
            "#11704F#5P#30Wえへへ、元気も元気。\x01",
            "もう大丈夫ですよー。\x02\x03",

            "#11700F２、３日で一般病室にも\x01",
            "移れるみたいですし……\x02\x03",

            "#11709Fそうしたら\x01",
            "退院まですぐですからー。\x02",
        )
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0x109,
        (
            "#10106F#12P駄目だよ、フラン。\x02\x03",

            "#10101F体力も落ちてるんだから\x01",
            "しばらく安静にしてないと……\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0x8,
        (
            "#11704F#5P#30Wえへへ……\x01",
            "わたしなんて軽い方だよー。\x02\x03",

            "#11708Fわたしを庇ってくれた\x01",
            "ドノバン警部なんて……\x02\x03",

            "#11706F#40W……………………………………\x02",
        )
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0x103,
        "#00208F#6Pフランさん……\x02",
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0x104,
        (
            "#00306F#6P……フランちゃんが\x01",
            "気に病む必要はねぇだろ。\x02\x03",

            "#00301F悪ぃのはあの連中……\x01",
            "《赤い星座》の猟兵どもだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0x8,
        (
            "#11712F#5P#30Wえへへ……はい。\x02\x03",

            "#11711Fでも、皆さんのサポートとか\x01",
            "バックアップもありますし……\x02\x03",

            "#11706F頑張って回復しないと……\x02",
        )
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0x101,
        (
            "#00004F#12P大丈夫、安心してくれ。\x02\x03",

            "#00000Fフランの声が聞けないのは寂しいけど\x01",
            "何とか報告処理は出来るみたいだし。\x02",
        )
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0x102,
        (
            "#00104F#12P今は回復に専念して\x01",
            "元気一杯になってちょうだい。\x02\x03",

            "#00102Fそうしたら私たちも\x01",
            "遠慮なく貴女に頼れるから。\x02",
        )
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0x8,
        (
            "#11704F#5P#30W……はい。\x01",
            "ありがとうございますー。\x02\x03",

            "#11705Fそういえば……\x01",
            "お姉ちゃん、警備隊の方に\x01",
            "戻っちゃうんだって……？\x02",
        )
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0x109,
        (
            "#10100F#12P母さんから聞いたんだ？\x01",
            "……うん、色々考えたんだけど。\x02\x03",

            "#10112Fフランのサポートが\x01",
            "受けられなくなるのは\x01",
            "ちょっと寂しいかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0x8,
        (
            "#11701F#5P#40Wむー、ちょっとだなんて\x01",
            "薄情なんだから……\x02\x03",

            "#11706F#50W……大体おねえちゃんは……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    def lambda_8F9C():
        OP_A6(0xFE, 0x0, 0x14, 0x12C, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_8F9C)
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
        "#10111F#12Pフラン……！？\x02",
    )

    CloseMessageWindow()
    OP_93(0x136, 0x13B, 0x1F4)
    Sleep(150)

    #C0329
    ChrTalk(
        0x136,
        (
            "#01304F#11P大丈夫、点滴の薬が\x01",
            "効いてきただけだから。\x02\x03",

            "#01302Fお話はこのくらいにして\x01",
            "寝ちゃった方がいいわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0x8,
        (
            "#11706F#11P#40W大丈夫ですよー……\x01",
            "せっかくロイドさんたちが\x01",
            "来てくれたんですし……\x02\x03",

            "#11701Fそれに、警備隊に戻る前に\x01",
            "お姉ちゃんには必勝法を……\x02",
        )
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0x109,
        (
            "#10106F#12Pはあ、何を言ってるんだか。\x02\x03",

            "#10108F……皆さん、すみません。\x01",
            "寝かせちゃっていいですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0x101,
        (
            "#00002F#12Pもちろん。\x01",
            "……フラン、また来るよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0x103,
        (
            "#00204F#6Pゆっくり休んでください。\x02\x03",

            "#00202F体力が戻ったらケーキでも\x01",
            "差し入れに来ますので。\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0x8,
        (
            "#11712F#11P#40Wあはは……\x01",
            "うん、楽しみにしてるねー……\x02\x03",

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
            "#10308F#6P……やっぱり相当、\x01",
            "体力は落ちてるみたいだね？\x02",
        )
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0x136,
        (
            "#01303F#11Pええ、手術の時に\x01",
            "かなりの輸血をしたから……\x02\x03",

            "#01300Fでも、あとは良くなるだけよ。\x02\x03",

            "#01309F大丈夫、すぐに元気になるわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0x109,
        "#10106F#12Pはい……\x02",
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0x101,
        "#00003F#11P……いったん外に出ようか。\x02",
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

    def lambda_9550():
        OP_9B(0x0, 0xFE, 0x0, 0x8CA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x136, 1, lambda_9550)
    Sleep(50)

    def lambda_9568():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x136, 2, lambda_9568)
    WaitChrThread(0x136, 1)
    BeginChrThread(0x1A, 1, 0, 48)
    OP_71(0x1, 0x14, 0x0, 0x0, 0x0)
    Sleep(100)

    #C0339
    ChrTalk(
        0x101,
        (
            "#00005F#6Pそういえば……\x02\x03",

            "#00001Fやっぱりドノバン警部や\x01",
            "イリアさんは面会謝絶なのかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0x136,
        (
            "#01306F#11P……一応ね。\x02\x03",

            "#01308Fでもあなた達は両方とも\x01",
            "関係者みたいなものだし……\x02\x03",

            "#01300F私が付き添うから\x01",
            "２人の様子を覗いていく？\x02",
        )
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0x102,
        "#00105F#6Pい、いいんですか？\x02",
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0x103,
        "#00203F#12Pそれはありがたいです。\x02",
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0x104,
        "#00301F#5Pセシルさん、お願いするッス。\x02",
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0x136,
        (
            "#01304F#11Pふふ……\x01",
            "それじゃあ行きましょう。\x02\x03",

            "#01300Fすぐそこの３０２号室が\x01",
            "ドノバンさんの病室になるわ。\x02\x03",

            "イリアは３０３号室……\x01",
            "シズクちゃんの部屋の向かいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0x101,
        "#00001F#6P分かった、行こうか。\x02",
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

    # Function_40_849C end

    def Function_41_9811(): pass

    label("Function_41_9811")

    OP_9B(0x0, 0xFE, 0x0, 0x6D6, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x14A, 0x3E8, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x14A, 0x2EE, 0x7D0, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_41_9811 end

    def Function_42_9846(): pass

    label("Function_42_9846")

    OP_9B(0x0, 0xFE, 0x0, 0x6D6, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x14A, 0xFA, 0x7D0, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_42_9846 end

    def Function_43_986C(): pass

    label("Function_43_986C")

    OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x7D0, 0x0)
    Sleep(100)
    OP_93(0xFE, 0x2D, 0x1F4)
    Sleep(300)
    OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x1)
    Return()

    # Function_43_986C end

    def Function_44_9898(): pass

    label("Function_44_9898")

    OP_9B(0x0, 0xFE, 0x14A, 0x2EE, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x14A, 0x79E, 0x7D0, 0x1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_44_9898 end

    def Function_45_98BE(): pass

    label("Function_45_98BE")

    OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0x3E8, 0x1)
    OP_9B(0x0, 0xFE, 0x0, 0x2EE, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x14A, 0x5DC, 0x7D0, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_45_98BE end

    def Function_46_98F3(): pass

    label("Function_46_98F3")

    OP_9B(0x0, 0xFE, 0x4, 0x2EE, 0x3E8, 0x1)
    OP_9B(0x0, 0xFE, 0x0, 0xEA6, 0x7D0, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_46_98F3 end

    def Function_47_9919(): pass

    label("Function_47_9919")

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
        "セシルの声",
        (
            "#2S#5Pレイモンドさん？\x01",
            "入りますよ。\x07\x00\x02",
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

    def lambda_9B01():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x136, 1, lambda_9B01)

    def lambda_9B16():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x136, 2, lambda_9B16)
    Sleep(100)
    Sleep(100)

    def lambda_9B2D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9B2D)

    def lambda_9B3E():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9B3E)
    Sleep(100)

    def lambda_9B56():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9B56)
    Sleep(100)

    def lambda_9B6E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_9B6E)

    def lambda_9B7F():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_9B7F)
    Sleep(100)

    def lambda_9B97():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_9B97)

    def lambda_9BA8():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_9BA8)
    Sleep(100)

    def lambda_9BC0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_9BC0)

    def lambda_9BD1():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_9BD1)
    Sleep(100)

    def lambda_9BE9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_9BE9)

    def lambda_9BFA():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_9BFA)
    Sleep(100)

    def lambda_9C12():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_9C12)
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
            "#6Pセシルさん……\x01",
            "それに君たちかぁ……\x02",
        )
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0x101,
        (
            "#00003F#11Pレイモンドさん、\x01",
            "……どうもお疲れ様です。\x02",
        )
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0x102,
        "#00108F#11P看病にいらしてたんですね。\x02",
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0xA,
        (
            "#6Pあはは……たまたま\x01",
            "警部の奥さんの代わりにね。\x02",
        )
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0xA,
        (
            "#6P警部が目を覚ましたら\x01",
            "『なに油売ってやがる！』って\x01",
            "怒鳴られちゃいそうだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0352
    ChrTalk(
        0x104,
        "#00308F#11Pそうか……\x02",
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0x103,
        (
            "#00203F#11P……いかにも\x01",
            "言いそうな感じですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0354
    ChrTalk(
        0x105,
        (
            "#10301F#11Pその装置……\x01",
            "ひょっとして人工呼吸器かい？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0x0)
    Sleep(300)

    #C0355
    ChrTalk(
        0xA,
        (
            "#11Pうん……呼吸器系にかなりの\x01",
            "ダメージを受けたみたいでね。\x02",
        )
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0xA,
        (
            "#11P何とか意識が戻ってくれれば\x01",
            "回復も早まると思うんだけど……\x02",
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
            "#11P……警部はさ。\x01",
            "爆発の時、僕とフランちゃんを\x01",
            "かばってくれたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0xA,
        (
            "#11Pあの大変な時、\x01",
            "オロオロしてるだけだった\x01",
            "不甲斐ない僕なんかを……\x02",
        )
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0xA,
        (
            "#11Pしかもフランちゃんは\x01",
            "手術までする大ケガだったのに\x01",
            "僕はカスリ傷くらいで……\x02",
        )
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0xA,
        (
            "#11P……自分の運の良さと\x01",
            "図々しさが情けなくなるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0x101,
        "#00008F#11Pレイモンドさん……\x02",
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0x104,
        "#00306F#11P……アンタのせいじゃねぇだろ。\x02",
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0x136,
        (
            "#01303F#11P……レイモンドさん。\x01",
            "休憩してきたらどうですか？\x02\x03",

            "#01301F今は容態も安定していますし、\x01",
            "私たちも巡回していますから。\x02\x03",

            "少しは休まないと持ちませんよ？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0x2)
    Sleep(300)

    #C0365
    ChrTalk(
        0xA,
        "#6Pあはは……すいません。\x02",
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0xA,
        (
            "#6Pでも、もうちょっとしたら\x01",
            "警部の奥さんが来るので、\x01",
            "それまでは……\x02",
        )
    )

    CloseMessageWindow()

    #C0367
    ChrTalk(
        0x136,
        "#01306F#11Pふう……分かりました。\x02",
    )

    CloseMessageWindow()

    #C0368
    ChrTalk(
        0x102,
        "#00103F#11P……どうかお大事に。\x02",
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0x103,
        "#00202F#11Pまたお見舞いに来ます。\x02",
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0xA,
        (
            "#6Pうん……\x01",
            "警部も喜ぶと思うよ。\x02",
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

    # Function_47_9919 end

    def Function_48_A256(): pass

    label("Function_48_A256")

    Sleep(600)
    Sound(107, 0, 100, 0)
    Return()

    # Function_48_A256 end

    def Function_49_A260(): pass

    label("Function_49_A260")

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
        "セシルの声",
        (
            "#2S#11Pシュリちゃん？\x01",
            "いいかしら。\x07\x00\x02",
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

    def lambda_A43B():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x136, 1, lambda_A43B)
    Sleep(50)

    def lambda_A453():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A453)

    def lambda_A468():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x136, 2, lambda_A468)
    Sleep(50)

    def lambda_A47C():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A47C)
    Sleep(50)

    def lambda_A494():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A494)
    Sleep(50)

    def lambda_A4AC():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A4AC)
    Sleep(50)

    def lambda_A4C4():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_A4C4)
    Sleep(50)

    def lambda_A4DC():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_A4DC)
    Sleep(50)
    Sleep(100)

    def lambda_A4F7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A4F7)

    def lambda_A508():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_A508)
    Sleep(400)

    def lambda_A51C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_A51C)

    def lambda_A52D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_A52D)
    Sleep(400)

    def lambda_A541():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_A541)

    def lambda_A552():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_A552)
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
        "#00008F#5Pシュリ……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x192, 4)), scpexpr(EXPR_END)), "loc_A5DF")

    #C0374
    ChrTalk(
        0x102,
        "#00108F#5P……………………………\x02",
    )

    CloseMessageWindow()
    Jump("loc_A5FD")

    label("loc_A5DF")


    #C0375
    ChrTalk(
        0x102,
        "#00106F#5P来ていたの……\x02",
    )

    CloseMessageWindow()

    label("loc_A5FD")

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
        "#00208F#6P#Nイリアさん……\x02",
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
            "#04206F#6P#30W静かで……キレイな寝顔だろ？\x02\x03",

            "#04208Fいつもグースカ、\x01",
            "豪快に寝乱れているクセに\x01",
            "こんな時だけ……\x02\x03",

            "#04202Fははっ……\x01",
            "イリア・プラティエらしく\x01",
            "なさすぎるっての……\x02",
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
        "#10301F#5P……容態の方はどんな？\x02",
    )

    CloseMessageWindow()

    #C0382
    ChrTalk(
        0x136,
        (
            "#01303F#5P……全身の骨折と\x01",
            "内臓へのダメージね。\x02\x03",

            "#01308F手術の方は成功したけど\x01",
            "まだ昏睡状態が続いていて……\x02\x03",

            "#01301F今は生命維持装置に\x01",
            "頼らざるを得ない状況ね。\x02",
        )
    )

    CloseMessageWindow()

    #C0383
    ChrTalk(
        0x101,
        "#00006F#5P……そこまで………\x02",
    )

    CloseMessageWindow()

    #C0384
    ChrTalk(
        0x104,
        "#00306F#5P……クソッ……！\x02",
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
            "#04202F#6P#30W……意識を取り戻しても\x01",
            "復帰は絶望的だってさ……\x02\x03",

            "信じられるか？\x01",
            "あのイリアさんがステージに\x01",
            "２度と立てないんだぞ……？\x02\x03",

            "#04208Fそれもオレを……\x01",
            "オレなんかを庇#2Rかば#ったせいで……\x02\x03",

            "#04206F#40W……そんなの……\x01",
            "そんなのってないだろ……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_AA20():
        OP_A6(0xFE, 0x0, 0x14, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_AA20)
    Sleep(800)
    TurnDirection(0x101, 0xC, 500)
    Sleep(150)

    #C0387
    ChrTalk(
        0x101,
        "#00001F#5P……シュリ………\x02",
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
        "#04205F#6P#40W………え……………\x02",
    )

    CloseMessageWindow()

    #C0390
    ChrTalk(
        0x136,
        (
            "#01304F#5P大丈夫……きっと大丈夫よ。\x02\x03",

            "イリアのことは\x01",
            "私が一番良く知っているわ。\x02\x03",

            "#01308Fどんな逆境でも決して諦めないで\x01",
            "ただひたすら上を見続ける……\x02\x03",

            "#01302Fそれがイリア・プラティエよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0391
    ChrTalk(
        0xC,
        "#04212F#6P#40W……で、でも………\x02",
    )

    CloseMessageWindow()

    #C0392
    ChrTalk(
        0x101,
        (
            "#00004F#5P──俺もそう思うよ。\x02\x03",

            "#00002Fそうでなきゃ、\x01",
            "あんな常識外れのステージなんて\x01",
            "生み出せるはずがないと思うし。\x02",
        )
    )

    CloseMessageWindow()

    #C0393
    ChrTalk(
        0x102,
        (
            "#00104F#6P#Nそうね……\x02\x03",

            "#00102Fイリアさんの貪欲さがあって\x01",
            "初めて実現できる空間だと思う。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0394
    ChrTalk(
        0x103,
        (
            "#00204F#6P#Nそこにステージがある限り……\x01",
            "きっとイリアさんは戻ってくる。\x02\x03",

            "#00202F不思議とそう思えてしまいます。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0395
    ChrTalk(
        0xC,
        "#04205F#6P#30W………ぁ……………\x02",
    )

    CloseMessageWindow()

    #C0396
    ChrTalk(
        0x104,
        (
            "#00304F#5Pだな……\x02\x03",

            "#00300F今は女神とイリアさんを信じて\x01",
            "自分に出来ることをやっときな。\x02",
        )
    )

    CloseMessageWindow()

    #C0397
    ChrTalk(
        0x105,
        (
            "#10304F#5P今日はともかく、舞台の練習は\x01",
            "欠かさない方がいいんじゃない？\x02\x03",

            "#10302Fその方が彼女も\x01",
            "釣られて起きて来そうだし。\x02",
        )
    )

    CloseMessageWindow()

    #C0398
    ChrTalk(
        0x109,
        (
            "#10112F#6Pうん……きっとそうだよ！\x02\x03",

            "#10102F楽しそうなステージに釣られて\x01",
            "絶対に目を覚ますから……！\x02",
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
            "#04204F#6P………あんがと。\x01",
            "ちょっと元気出てきた。\x02\x03",

            "#04208Fそうだよな……\x01",
            "オレたちがしっかりしないと……\x02\x03",

            "リーシャ姉も……\x01",
            "いなくなっちゃったんだし……\x02",
        )
    )

    CloseMessageWindow()

    #C0401
    ChrTalk(
        0x102,
        "#00108F#6P#Nあ……\x02",
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
            "#04206F#6P……なあ、アンタら。\x02\x03",

            "出来ればリーシャ姉のこと、\x01",
            "見つけてあげてくれないか……？\x02\x03",

            "#04208Fどんな事情があったとしても\x01",
            "リーシャ姉はリーシャ姉だから……\x02\x03",

            "#04201Fそれに、リーシャ姉が戻ってくれば、\x01",
            "イリアさんも元気になると思うんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0404
    ChrTalk(
        0x101,
        (
            "#00003F#5P───分かった。\x02\x03",

            "#00000F特務支援課の名に賭けて\x01",
            "必ず見つけて出してみせるよ。\x02",
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
            "#01302F#12P……みんな、ありがとう。\x02\x03",

            "これでシュリちゃんも\x01",
            "元気を取り戻せると思うわ。\x02\x03",

            "#01304F私も……\x01",
            "少し勇気付けられちゃった。\x02",
        )
    )

    CloseMessageWindow()

    #C0406
    ChrTalk(
        0x101,
        "#00008F#5Pセシル姉……\x02",
    )

    CloseMessageWindow()

    #C0407
    ChrTalk(
        0x102,
        (
            "#00106F#5Pやっぱり相当、\x01",
            "深刻な容態なんですね……\x02",
        )
    )

    CloseMessageWindow()

    #C0408
    ChrTalk(
        0x136,
        (
            "#01306F#12Pええ……\x01",
            "正直、安心はできないわ。\x02\x03",

            "#01308F……それでもやっぱり、\x01",
            "私はイリアを信じてるから。\x02\x03",

            "#01302Fそれに信じる人が多ければ多いほど\x01",
            "彼女はそれに応えてくれると思うの。\x02",
        )
    )

    CloseMessageWindow()

    #C0409
    ChrTalk(
        0x104,
        "#00302F#5Pそうッスね……\x02",
    )

    CloseMessageWindow()

    #C0410
    ChrTalk(
        0x103,
        (
            "#00204F#5P確かにそれが\x01",
            "イリアさんかもしれません。\x02",
        )
    )

    CloseMessageWindow()

    #C0411
    ChrTalk(
        0x105,
        (
            "#10303F#5Pしかしそうなると……\x01",
            "鍵はやっぱり“彼女#4Rリーシャ#”か。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B423():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_B423)
    WaitChrThread(0x105, 2)
    Sleep(150)

    #C0412
    ChrTalk(
        0x105,
        "#10300F#5Pロイド、見つけられるのかい？\x02",
    )

    CloseMessageWindow()

    def lambda_B463():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_B463)
    Sleep(150)

    def lambda_B473():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_B473)
    Sleep(50)

    def lambda_B483():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_B483)
    Sleep(50)

    def lambda_B493():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_B493)
    Sleep(50)

    def lambda_B4A3():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_B4A3)
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
            "#00003F#6P……正直、分からない。\x02\x03",

            "#00008F本気で身を隠したんだったら\x01",
            "見つけるのはかなり困難だろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0414
    ChrTalk(
        0x109,
        (
            "#10106F#5Pそうですね……\x02\x03",

            "#10108F行方不明の《黒月》同様、\x01",
            "自治州に居るのか居ないのかも\x01",
            "はっきりしませんし……\x02",
        )
    )

    CloseMessageWindow()

    #C0415
    ChrTalk(
        0x104,
        (
            "#00303F#11Pカルバード方面に戻っちまった\x01",
            "可能性もあるしな……\x02\x03",

            "#00300Fだが、シュリぞうに\x01",
            "あんな風に頼まれちまったら\x01",
            "諦めるわけにもいかねぇよな？\x02",
        )
    )

    CloseMessageWindow()

    #C0416
    ChrTalk(
        0x101,
        "#00000F#6Pああ──勿論だ。\x02",
    )

    CloseMessageWindow()

    #C0417
    ChrTalk(
        0x102,
        (
            "#00100F#11P《黒月》の行方と合わせて\x01",
            "気を配った方がいいわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0418
    ChrTalk(
        0x103,
        (
            "#00202F#6Pわたしも導力ネット方面を\x01",
            "常にチェックしておきます。\x02",
        )
    )

    CloseMessageWindow()

    #C0419
    ChrTalk(
        0x136,
        (
            "#01304F#12Pふふ……本当にありがとう。\x02\x03",

            "#01300F私はナースステーションに戻るけど\x01",
            "ロイドたちはどうするの？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B749():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_B749)
    Sleep(150)

    def lambda_B759():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_B759)
    Sleep(50)

    def lambda_B769():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_B769)
    Sleep(50)

    def lambda_B779():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_B779)
    Sleep(50)

    def lambda_B789():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_B789)
    Sleep(50)

    def lambda_B799():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_B799)
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
            "#00002F#5Pああ、仕事も残っているし\x01",
            "そろそろお暇#2Rいとま#するよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0421
    ChrTalk(
        0x102,
        (
            "#00104F#5P案内していただいて\x01",
            "ありがとうございました。\x02",
        )
    )

    CloseMessageWindow()

    #C0422
    ChrTalk(
        0x136,
        (
            "#01309F#12Pふふ、こちらこそ。\x02\x03",

            "#01302F大変な状況だけど……\x01",
            "お互い頑張りましょう。\x02\x03",

            "ただし無理はしすぎないでね？\x02",
        )
    )

    CloseMessageWindow()

    #C0423
    ChrTalk(
        0x104,
        "#00309F#5P了解ッス。\x02",
    )

    CloseMessageWindow()

    #C0424
    ChrTalk(
        0x103,
        "#00204F#5Pお疲れさまでした。\x02",
    )

    CloseMessageWindow()
    OP_68(-14130, 1200, 29280, 3000)
    BeginChrThread(0x136, 1, 0, 59)
    Sleep(400)

    def lambda_B90B():
        TurnDirection(0xFE, 0x136, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_B90B)
    Sleep(350)

    def lambda_B91B():
        TurnDirection(0xFE, 0x136, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_B91B)
    Sleep(150)

    def lambda_B92B():
        TurnDirection(0xFE, 0x136, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_B92B)
    Sleep(250)

    def lambda_B93B():
        TurnDirection(0xFE, 0x136, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_B93B)
    Sleep(150)

    def lambda_B94B():
        TurnDirection(0xFE, 0x136, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_B94B)
    Sleep(150)

    def lambda_B95B():
        TurnDirection(0xFE, 0x136, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_B95B)
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

    def lambda_BA1A():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_BA1A)
    Sleep(150)

    def lambda_BA2A():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_BA2A)
    Sleep(50)

    def lambda_BA3A():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_BA3A)
    Sleep(50)

    def lambda_BA4A():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_BA4A)
    Sleep(50)

    def lambda_BA5A():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_BA5A)
    Sleep(50)

    def lambda_BA6A():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_BA6A)
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
            "#00006F#6P本当に……\x01",
            "ここが踏ん張りどころだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0426
    ChrTalk(
        0x102,
        (
            "#00103F#11Pええ……そうね。\x02\x03",

            "#00108F心と身体を傷つけられた人たちに\x01",
            "笑顔を取り戻してもらうためにも。\x02",
        )
    )

    CloseMessageWindow()

    #C0427
    ChrTalk(
        0x109,
        (
            "#10108F#5P…………………………\x01",
            "（踏ん張りどころ、か。）\x02",
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

    # Function_49_A260 end

    def Function_50_BBF3(): pass

    label("Function_50_BBF3")

    OP_9B(0x0, 0xFE, 0x5, 0xFA, 0x3E8, 0x1)
    OP_9B(0x1, 0xFE, 0x5, 0xC8, 0x1F4, 0x0)
    Return()

    # Function_50_BBF3 end

    def Function_51_BC12(): pass

    label("Function_51_BC12")

    OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF06, 0x1F4, 0x0)
    Return()

    # Function_51_BC12 end

    def Function_52_BC22(): pass

    label("Function_52_BC22")

    OP_96(0x136, 0xFFFE7C08, 0x0, 0xFFFFED7C, 0x4B0, 0x0)
    Return()

    # Function_52_BC22 end

    def Function_53_BC37(): pass

    label("Function_53_BC37")

    OP_95(0xFE, -97730, 0, -3800, 1500, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_53_BC37 end

    def Function_54_BC53(): pass

    label("Function_54_BC53")

    OP_95(0xFE, -100440, 0, -7000, 1500, 0x0)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_54_BC53 end

    def Function_55_BC6F(): pass

    label("Function_55_BC6F")

    OP_95(0xFE, -101020, 0, -6010, 1500, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_55_BC6F end

    def Function_56_BC8B(): pass

    label("Function_56_BC8B")

    OP_95(0xFE, -98500, 0, -3400, 1500, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_56_BC8B end

    def Function_57_BCA7(): pass

    label("Function_57_BCA7")

    OP_95(0xFE, -99600, 0, -3350, 1500, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_57_BCA7 end

    def Function_58_BCC3(): pass

    label("Function_58_BCC3")

    OP_95(0xFE, -100570, 0, -4650, 1500, 0x0)
    OP_93(0xFE, 0x87, 0x1F4)
    Return()

    # Function_58_BCC3 end

    def Function_59_BCDF(): pass

    label("Function_59_BCDF")

    OP_9B(0x0, 0xFE, 0x2D, 0x384, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0x1194, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0x384, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0xFA0, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x14A, 0xBB8, 0x7D0, 0x1)
    Return()

    # Function_59_BCDF end

    def Function_60_BD2B(): pass

    label("Function_60_BD2B")

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
            "#11Pあら……？\x02\x03",

            "どちらさま？\x01",
            "入っちゃっていいわよ。\x02",
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
        "#00204F#6P……失礼します。\x02",
    )

    CloseMessageWindow()
    OP_68(-97660, 1000, -3500, 3000)
    MoveCamera(45, 19, 0, 3000)
    OP_6E(440, 3000)
    SetCameraDistance(22000, 3000)

    def lambda_BF2F():
        OP_9B(0x0, 0xFE, 0x0, 0xEA6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_BF2F)

    def lambda_BF44():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_BF44)
    Sleep(100)

    def lambda_BF58():
        OP_9B(0x0, 0xFE, 0x0, 0xEA6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BF58)

    def lambda_BF6D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_BF6D)
    Sleep(100)

    def lambda_BF81():
        OP_9B(0x0, 0xFE, 0x0, 0xEA6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_BF81)

    def lambda_BF96():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_BF96)
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
        "#11602F#11Pあら、ティオちゃんと……\x02",
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0431
    ChrTalk(
        0xB,
        (
            "#11605F#11Pええっ、弟君じゃない！？\x02\x03",

            "#11602Fそれにあなたは……\x01",
            "たしかワジ君だったかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0432
    ChrTalk(
        0x105,
        "#10404F#5Pああ、ご無沙汰してるね。\x02",
    )

    CloseMessageWindow()

    #C0433
    ChrTalk(
        0x101,
        (
            "#00002F#5Pイリアさん……\x01",
            "本当にお久しぶりです。\x02\x03",

            "#00006Fすみません、お見舞いなのに\x01",
            "手ぶらで来てしまって……\x02",
        )
    )

    CloseMessageWindow()

    #C0434
    ChrTalk(
        0xB,
        (
            "#11609F#11Pああもう！\x01",
            "そんなの気にしないでってば！\x02\x03",

            "#11602Fホラホラ、３人とも。\x01",
            "こっちにいらっしゃいな。\x02\x03",

            "#11605Fあ、ファンからのお菓子とか\x01",
            "勝手に食べちゃってもいーわよ？\x02\x03",

            "#11609Fクッキーとかだったら\x01",
            "まだ賞味期限内だと思うし。\x02",
        )
    )

    CloseMessageWindow()

    #C0435
    ChrTalk(
        0x101,
        "#00012F#5Pはは……\x02",
    )

    CloseMessageWindow()

    #C0436
    ChrTalk(
        0x103,
        "#00204F#5Pそれでは失礼します。\x02",
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
            "#11603F#11Pそっか……\x01",
            "君たちも色々大変そうね。\x02\x03",

            "#11601Fクロスベルそのものが\x01",
            "とんでもない事になってるのは\x01",
            "色々聞いてはいるんだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0438
    ChrTalk(
        0x101,
        "#00003F#6Pはい……\x02",
    )

    CloseMessageWindow()

    #C0439
    ChrTalk(
        0x105,
        (
            "#10406F#6Pま、確かにとんでもないとしか\x01",
            "表現できない事態だよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0440
    ChrTalk(
        0xB,
        (
            "#11606F#11Pうーん、足が動かないのが\x01",
            "もどかしくて仕方ないわね……\x02\x03",

            "#11608Fアルカンシェルの様子とか\x01",
            "この目で確かめたいんだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0441
    ChrTalk(
        0x101,
        (
            "#00006F#6P#30Wその、イリアさん。\x02\x03",

            "#00008F身体の方は、えっと……\x02",
        )
    )

    CloseMessageWindow()

    #C0442
    ChrTalk(
        0xB,
        (
            "#11605F#11Pああ、うん。\x02\x03",

            "#11603Fセイランド先生は、\x01",
            "歩けるようになるかどうかも\x01",
            "現時点では判らないだって。\x02\x03",

            "#11600Fまあ、１００％無理って\x01",
            "断言されたわけじゃないけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0443
    ChrTalk(
        0x101,
        "#00006F#6P#40W……そう……ですか。\x02",
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
            "#11606F#11Pああもう、そんな顔をされたら\x01",
            "こっちまで暗くなるじゃないの。\x02\x03",

            "#11601Fあのね──駄目って思い込んだら\x01",
            "それだけで可能性は無くなるのよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0446
    ChrTalk(
        0x101,
        "#00005F#6P#30Wえ……\x02",
    )

    CloseMessageWindow()

    #C0447
    ChrTalk(
        0xB,
        (
            "#11604F#11P舞台にしてもそうだけど……\x01",
            "どこかに必ず“答え”はあるの。\x02\x03",

            "#11600Fどんなに苦しくても、絶望的でも、\x01",
            "一筋の光明は絶対#4R㈲　㈲#にあるわ。\x02\x03",

            "#11609F諦めない限り、きっとね。\x02",
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
        "#00204F#12Pふふっ……\x02",
    )

    CloseMessageWindow()

    #C0450
    ChrTalk(
        0x105,
        "#10402F#6P……凄いね、貴女は。\x02",
    )

    CloseMessageWindow()

    #C0451
    ChrTalk(
        0xB,
        (
            "#11606F#11Pうーん、別に凄いとか\x01",
            "言われるほどのものかしら。\x02\x03",

            "#11601F第一ねぇ、話を聞く限り、\x01",
            "あなた達の方が大変じゃないの？\x02",
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
        "#00011F#6Pそれは……\x02",
    )

    CloseMessageWindow()

    #C0453
    ChrTalk(
        0x103,
        (
            "#00206F#12P……確かに、普通に考えれば\x01",
            "恐ろしく困難な道のりかと。\x02",
        )
    )

    CloseMessageWindow()

    #C0454
    ChrTalk(
        0xB,
        (
            "#11604F#11P同じよ、同じ。\x02\x03",

            "#11600F人って大切なモノのためなら\x01",
            "どこまでも頑張れる生き物だしね。\x02\x03",

            "程度の差あれ……\x01",
            "それが人の強さなんだと思う。\x02",
        )
    )

    CloseMessageWindow()

    #C0455
    ChrTalk(
        0x101,
        "#00002F#6P人という生き物の強さ……\x02",
    )

    CloseMessageWindow()

    #C0456
    ChrTalk(
        0x105,
        "#10404F#6P……なるほど。\x02",
    )

    CloseMessageWindow()

    #C0457
    ChrTalk(
        0xB,
        (
            "#11602F#11Pまあ、あたしはその中でも\x01",
            "かなり欲張りな方だと思うけど。\x02\x03",

            "それでも本質的なところは\x01",
            "他の人たちだって同じだと思うわ。\x02\x03",

            "#11604Fうちの劇団員たちも……\x02\x01",

            "#11600F──もちろんリーシャもね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0458
    ChrTalk(
        0x101,
        "#00001F#6Pイリアさん……\x02",
    )

    CloseMessageWindow()

    #C0459
    ChrTalk(
        0xB,
        (
            "#11602F#11Pフフ、あの子に会えたら\x01",
            "伝えておいてもらえない？\x02\x03",

            "#11604F『──あんたにとって、\x01",
            "  一番大切なものはなに？』\x02\x03",

            "『その大切なものを前にして\x01",
            "  頑張らずにいられるの？』って。\x02",
        )
    )

    CloseMessageWindow()

    #C0460
    ChrTalk(
        0x101,
        (
            "#00004F#6P……分かりました。\x02\x03",

            "#00000Fリーシャに会うことが出来たら\x01",
            "必ずその言葉を伝えます。\x02",
        )
    )

    CloseMessageWindow()

    #C0461
    ChrTalk(
        0xB,
        "#11609F#11Pええ、頼んだわよ！\x02",
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

    # Function_60_BD2B end

    def Function_61_CBCF(): pass

    label("Function_61_CBCF")

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

    def lambda_CC6B():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_CC6B)

    def lambda_CC80():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_CC80)
    Sleep(50)

    def lambda_CC98():
        OP_9B(0x0, 0xFE, 0x0, 0x109A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_CC98)
    Sleep(50)
    Sleep(50)
    Sleep(100)

    def lambda_CCB6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_CCB6)

    def lambda_CCC7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_CCC7)
    Sleep(400)

    def lambda_CCDB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_CCDB)
    Sleep(800)
    Sound(107, 0, 100, 0)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x105, 1)
    OP_0D()

    def lambda_CD02():
        OP_93(0x101, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_CD02)
    Sleep(50)

    def lambda_CD12():
        OP_93(0x103, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_CD12)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x103, 0)

    #C0462
    ChrTalk(
        0x105,
        (
            "#10404F#12Pはは……\x01",
            "ホント、とんでもないね。\x02\x03",

            "#10402Fさすが《炎の舞姫》なんて\x01",
            "呼ばれてるだけはあるな。\x02",
        )
    )

    CloseMessageWindow()

    #C0463
    ChrTalk(
        0x103,
        (
            "#00204F#5P……むしろ舞台の\x01",
            "《太陽の姫》そのものかと。\x02\x03",

            "#00208Fわたしもここに連れて来られて、\x01",
            "何度か話しているんですけど……\x02\x03",

            "#00202Fセシルさん共々、\x01",
            "すごく元気付けてもらいました。\x02",
        )
    )

    CloseMessageWindow()

    #C0464
    ChrTalk(
        0x101,
        (
            "#00004F#6Pそっか……\x02\x03",

            "#00008F……本当に、何とかリーシャも\x01",
            "見つけられればいいんだけどな。\x02",
        )
    )

    CloseMessageWindow()

    #C0465
    ChrTalk(
        0x105,
        (
            "#10406F#12Pまあ、そればっかりは\x01",
            "女神の巡り合わせだろうね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1A0, 7)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 1)), scpexpr(EXPR_END)), "loc_CF71")

    #C0466
    ChrTalk(
        0x103,
        (
            "#00202F#5Pフランさんに声をかけて\x01",
            "そろそろ戻りましょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0467
    ChrTalk(
        0x101,
        "#00000F#6Pああ、そうしよう。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 3)
    NewScene("t1500", 0, 0, 0)
    IdleLoop()
    Jump("loc_CFF2")

    label("loc_CF71")


    #C0468
    ChrTalk(
        0x103,
        (
            "#00202F#5Pドノバン警部の方も\x01",
            "お見舞いに行きましょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0469
    ChrTalk(
        0x101,
        "#00000F#6Pああ、そうしよう。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -16500, 0, 30000, 0)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)

    label("loc_CFF2")

    Return()

    # Function_61_CBCF end

    def Function_62_CFF3(): pass

    label("Function_62_CFF3")

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
        "#6Pあら、検温の時間かしら。\x02",
    )

    CloseMessageWindow()

    #C0471
    ChrTalk(
        0x9,
        "どうぞ、入ってくれ。\x02",
    )

    CloseMessageWindow()

    #C0472
    ChrTalk(
        0x101,
        "#6P……失礼します。\x02",
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

    def lambda_D166():
        OP_95(0x101, -53180, 0, -49830, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D166)

    def lambda_D180():
        OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_D180)
    Sleep(500)

    def lambda_D194():
        OP_95(0x105, -53100, 0, -50830, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_D194)

    def lambda_D1AE():
        OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_D1AE)
    Sleep(600)

    def lambda_D1C2():
        OP_95(0x103, -51840, 50, -50110, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_D1C2)

    def lambda_D1DC():
        OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_D1DC)
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
            "おお、お前ら……\x01",
            "支援課じゃねえか！\x02",
        )
    )

    CloseMessageWindow()

    #C0474
    ChrTalk(
        0x101,
        (
            "#00000F#11Pはは、お久しぶりです\x01",
            "ドノバン警部。\x02",
        )
    )

    CloseMessageWindow()

    #C0475
    ChrTalk(
        0x105,
        (
            "#10405F#12Pあれ、そちらの美人はどなただい？\x02\x03",

            "#10409Fフフ、もしかして\x01",
            "逢引きのお邪魔をしちゃったかな。\x02",
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
            "再会していきなり、\x01",
            "何を言いだしやがる……\x02",
        )
    )

    CloseMessageWindow()

    #C0477
    ChrTalk(
        0x101,
        "#00006F#11Pワジ、お前な……\x02",
    )

    CloseMessageWindow()

    #C0478
    ChrTalk(
        0x103,
        (
            "#00202F#2Pこちらは警部の奥さんの\x01",
            "ファラさんです。\x02\x03",

            "少し前にお見舞いに来てから\x01",
            "しばらく滞在しています。\x02",
        )
    )

    CloseMessageWindow()

    #C0479
    ChrTalk(
        0x16,
        (
            "#6Pうふふ、始めまして。\x01",
            "いつも主人がお世話になっています。\x02",
        )
    )

    CloseMessageWindow()

    #C0480
    ChrTalk(
        0x16,
        (
            "#6P主人やティオさんから\x01",
            "ときどき話に聞いていたけど、\x01",
            "とても面白い人たちみたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0481
    ChrTalk(
        0x105,
        "#10402F#12Pフフ、お褒めいただき光栄だよ。\x02",
    )

    CloseMessageWindow()

    #C0482
    ChrTalk(
        0x101,
        (
            "#00006F#11P（多分褒めてるんじゃ\x01",
            "  ないと思うけど……）\x02",
        )
    )

    CloseMessageWindow()

    #C0483
    ChrTalk(
        0x9,
        (
            "ま、積もる話もあるだろうが……\x01",
            "一度事情を説明しちゃくれねえか？\x02",
        )
    )

    CloseMessageWindow()

    #C0484
    ChrTalk(
        0x101,
        "#00000F#11Pええ、分かりました。\x02",
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
            "#1Pふむ……思った以上に\x01",
            "大変なことが起きてやがるな。\x02",
        )
    )

    CloseMessageWindow()

    #C0486
    ChrTalk(
        0x9,
        (
            "#1Pそれに、聞いた限りじゃ\x01",
            "ここで会ったことも本部には\x01",
            "報告しない方がよさそうだな？\x02",
        )
    )

    CloseMessageWindow()

    #C0487
    ChrTalk(
        0x101,
        "#00000F#12Pはい、そうして頂けると助かります。\x02",
    )

    CloseMessageWindow()

    #C0488
    ChrTalk(
        0x105,
        (
            "#10406F#12Pまあ、僕はどっちでもいいけど\x01",
            "ロイドは指名手配されてるだろうからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0489
    ChrTalk(
        0x16,
        "#6Pまあ……\x02",
    )

    CloseMessageWindow()

    #C0490
    ChrTalk(
        0x101,
        (
            "#00001F#12Pと、とにかく。\x01",
            "……警部、クロスベル市内の\x01",
            "状況はどうなっていますか？\x02",
        )
    )

    CloseMessageWindow()

    #C0491
    ChrTalk(
        0x9,
        (
            "#1Pああ、俺も見舞いに来た\x01",
            "レイモンドから聞いただけだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0492
    ChrTalk(
        0x9,
        (
            "#1Pクロスベル警察は、\x01",
            "国防軍の下部組織として\x01",
            "完全に取り込まれたそうだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0493
    ChrTalk(
        0x9,
        (
            "#1P業務内容は変わっちゃいないが、\x01",
            "今は市内での雑用ばかりに\x01",
            "駆りだされているらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0494
    ChrTalk(
        0x103,
        "#00203Fやはり、そうですか……\x02",
    )

    CloseMessageWindow()

    #C0495
    ChrTalk(
        0x105,
        (
            "#10406F#12Pまあ、現状を考えると\x01",
            "仕方ないだろうけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0496
    ChrTalk(
        0x101,
        (
            "#00001F#12Pでも……そんな体制、\x01",
            "さすがに反発があったのでは？\x02\x03",

            "#00003Fピエール副局長はともかく、\x01",
            "セルゲイ課長やダドリーさんが\x01",
            "黙って従っているとは……\x02",
        )
    )

    CloseMessageWindow()

    #C0497
    ChrTalk(
        0x9,
        "#1Pああ、ここだけの話だが……\x02",
    )

    CloseMessageWindow()

    #C0498
    ChrTalk(
        0x9,
        (
            "#1Pどうやらセルゲイやダドリー、\x01",
            "レイモンドも含む警官たちが\x01",
            "密かに動いてるらしい。\x02",
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
        "#00205F課長たちが……？\x02",
    )

    CloseMessageWindow()

    #C0500
    ChrTalk(
        0x9,
        "#1Pあくまで極秘裏にだがな。\x02",
    )

    CloseMessageWindow()

    #C0501
    ChrTalk(
        0x9,
        (
            "#1P機を窺いつつ、\x01",
            "なんとか現状を打開する方法を\x01",
            "探しているって所なんだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0502
    ChrTalk(
        0x105,
        (
            "#10402F#12P誰も彼もが黙っている\x01",
            "タマじゃないってことか。\x02\x03",

            "#10404Fフフ、希望が見えてきたかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0503
    ChrTalk(
        0x101,
        (
            "#00000F#12Pああ、今のところコンタクトを\x01",
            "とるのは難しそうだけど……\x01",
            "市内の方は任せてよさそうだ。\x02\x03",

            "#00003F俺たちは俺たちなりに、\x01",
            "現状を打開する術を\x01",
            "探っていったほうがいいだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0504
    ChrTalk(
        0x9,
        "#1Pそれでこそお前らだ。\x02",
    )

    CloseMessageWindow()

    #C0505
    ChrTalk(
        0x9,
        (
            "#1P実際かなり厳しいだろうが、\x01",
            "なんとか気張ってみてくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0506
    ChrTalk(
        0x9,
        (
            "#1P俺も復帰したら、すぐにでも\x01",
            "セルゲイたちに合流して……\x02",
        )
    )

    CloseMessageWindow()

    #C0507
    ChrTalk(
        0x16,
        (
            "#6Pまあ、あなたったら……\x01",
            "今は彼らやレイモンド君たちに任せて、\x01",
            "ゆっくりと身体を治しなさいな。\x02",
        )
    )

    CloseMessageWindow()

    #C0508
    ChrTalk(
        0x16,
        (
            "#6P完治するまでは、私が絶対に\x01",
            "無理なんかさせませんからね？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0509
    ChrTalk(
        0x9,
        "#1Pう、うむ……分かった。\x02",
    )

    CloseMessageWindow()

    #C0510
    ChrTalk(
        0x101,
        (
            "#00000F#12P（はは……\x01",
            "  言いたい事を言われちゃったか。）\x02",
        )
    )

    CloseMessageWindow()

    #C0511
    ChrTalk(
        0x103,
        (
            "#00200F（警部もこの奥さんには\x01",
            "  頭が上がらないみたいですね。）\x02",
        )
    )

    CloseMessageWindow()

    #C0512
    ChrTalk(
        0x105,
        (
            "#10404F#12P（フフ、いい奥さんに恵まれて\x01",
            "  警部も幸せ者だねえ。）\x02",
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

    # Function_62_CFF3 end

    def Function_63_DE5D(): pass

    label("Function_63_DE5D")

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

    def lambda_DF4A():
        OP_95(0x101, -15360, 0, 8900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DF4A)

    def lambda_DF64():
        OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_DF64)
    Sleep(600)

    def lambda_DF78():
        OP_95(0x103, -14800, 0, 7940, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_DF78)

    def lambda_DF92():
        OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_DF92)
    Sleep(600)

    def lambda_DFA6():
        OP_95(0x105, -14980, 0, 10240, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_DFA6)

    def lambda_DFC0():
        OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_DFC0)
    Sleep(1200)
    Sound(107, 0, 100, 0)

    #C0513
    ChrTalk(
        0x8,
        "あ、みなさ～ん。\x02",
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

    def lambda_E036():

        label("loc_E036")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_E036")

    QueueWorkItem2(0x101, 2, lambda_E036)

    def lambda_E048():

        label("loc_E048")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_E048")

    QueueWorkItem2(0x105, 2, lambda_E048)

    def lambda_E05A():

        label("loc_E05A")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_E05A")

    QueueWorkItem2(0x103, 2, lambda_E05A)
    OP_95(0x8, -13480, 0, 9000, 3000, 0x0)
    SetChrSubChip(0x8, 0x0)

    #C0514
    ChrTalk(
        0x101,
        (
            "#00000F#6Pああ、フラン……\x01",
            "荷物はまとめ終わったのか？\x02",
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
        "ええ、この通りです！\x02",
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
            "#00202F#6Pフランさんの制服姿も\x01",
            "久しぶりですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0517
    ChrTalk(
        0x8,
        (
            "#01909F#11Pふふ、わたしもだよ～。\x02\x03",

            "#01900Fみなさんはドノバン警部の\x01",
            "お見舞いをしてたんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0518
    ChrTalk(
        0x101,
        (
            "#00004F#6Pああ、今終わった所だ。\x02\x03",

            "#00000Fフランも警部の見舞いに？\x02",
        )
    )

    CloseMessageWindow()

    #C0519
    ChrTalk(
        0x8,
        (
            "#01904F#11Pええ、退院する前に\x01",
            "一通り挨拶しておこうと\x01",
            "思いまして。\x02\x03",

            "#01902F特に警部には危ない所を\x01",
            "助けてもらいましたし、\x01",
            "改めてお礼を言わないと。\x02",
        )
    )

    CloseMessageWindow()

    #C0520
    ChrTalk(
        0x101,
        (
            "#00002F#6Pはは、そっか。\x01",
            "それじゃあまた後でな。\x02",
        )
    )

    CloseMessageWindow()

    #C0521
    ChrTalk(
        0x8,
        "#01909F#11Pはい、また後で～！\x02",
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

    def lambda_E3BA():
        OP_95(0xFE, -19090, 0, 8900, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_E3BA)

    def lambda_E3D4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_E3D4)
    WaitChrThread(0x8, 2)
    Sleep(1000)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x105, 0x1)
    EndChrThread(0x105, 0x2)
    EndChrThread(0x103, 0x2)

    def lambda_E400():
        OP_95(0xFE, -16200, 0, 8800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E400)
    Sleep(50)

    def lambda_E41D():
        OP_95(0xFE, -14800, 0, 10000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_E41D)
    Sleep(50)

    def lambda_E43A():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_E43A)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0x5A, 0x1F4)
    SetScenarioFlags(0x1A1, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 7)), scpexpr(EXPR_END)), "loc_E4DC")

    #C0522
    ChrTalk(
        0x105,
        (
            "#10402F#5Pさて、彼女の挨拶が終わったら\x01",
            "メルカバに戻るとしようか？\x02",
        )
    )

    CloseMessageWindow()

    #C0523
    ChrTalk(
        0x101,
        "#00000F#6Pああ、そうだな。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 3)
    NewScene("t1500", 0, 0, 0)
    IdleLoop()
    Jump("loc_E580")

    label("loc_E4DC")


    #C0524
    ChrTalk(
        0x105,
        (
            "#10402F#5Pさて、それじゃあ僕たちは\x01",
            "イリアさんの方の\x01",
            "お見舞いに行くとしようか？\x02",
        )
    )

    CloseMessageWindow()

    #C0525
    ChrTalk(
        0x101,
        "#00000F#6Pああ、そうだな。\x02",
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

    label("loc_E580")

    Return()

    # Function_63_DE5D end

    def Function_64_E581(): pass

    label("Function_64_E581")

    OP_93(0xFE, 0xB4, 0x1F4)
    OP_9B(0x1, 0xFE, 0xE1, 0x320, 0x3E8, 0x0)

    def lambda_E59C():

        label("loc_E59C")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_E59C")

    QueueWorkItem2(0xFE, 2, lambda_E59C)
    Return()

    # Function_64_E581 end

    def Function_65_E5AA(): pass

    label("Function_65_E5AA")

    OP_93(0xFE, 0xB4, 0x1F4)
    OP_9B(0x1, 0xFE, 0xA0, 0x5DC, 0x3E8, 0x0)

    def lambda_E5C5():

        label("loc_E5C5")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_E5C5")

    QueueWorkItem2(0xFE, 2, lambda_E5C5)
    Return()

    # Function_65_E5AA end

    def Function_66_E5D3(): pass

    label("Function_66_E5D3")

    Sleep(1850)
    Sound(107, 0, 100, 0)
    Sleep(1000)
    Sound(107, 0, 100, 0)
    Return()

    # Function_66_E5D3 end

    def Function_67_E5E6(): pass

    label("Function_67_E5E6")

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
            "#01400F……セルゲイさん、《幻獣》の件を\x01",
            "引き受けてくれたそうですね。\x02\x03",

            "#01403F本来ならば俺も遊撃士として、\x01",
            "調査と退治に行くべきなのでしょうが……\x02",
        )
    )

    CloseMessageWindow()

    #C0527
    ChrTalk(
        0x19,
        (
            "#12P#01000Fお前が気に病む必要はない。\x02\x03",

            "#01003F幻獣に関しては、分担して\x01",
            "対応する手筈が整っているしな。\x02\x03",

            "#01000Fまあ、今日のところは\x01",
            "あいつらに任せておくといい。\x02",
        )
    )

    CloseMessageWindow()

    #C0528
    ChrTalk(
        0xF,
        "#01408Fですが……\x02",
    )

    CloseMessageWindow()

    #C0529
    ChrTalk(
        0x19,
        (
            "#12P#01002Fま、あいつらも成長してるし、\x01",
            "そこまで心配することもあるまい。\x02\x03",

            "#01004Fそれに、普段はなかなか\x01",
            "見舞いに来れてないんだろう。\x02\x03",

            "#01002Fこんな時くらい\x01",
            "娘のそばにいてやるのが\x01",
            "オヤジの務めってもんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0530
    ChrTalk(
        0xF,
        "#01403F……恩に着ます。\x02",
    )

    CloseMessageWindow()

    #C0531
    ChrTalk(
        0xD,
        (
            "#11P#11209Fふふ……\x01",
            "ありがとうございます、課長さん。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(300, 160, -1, -1)
    SetChrName("ロイドの声")

    #A0532
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "……失礼します。\x07\x00\x02",
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

    def lambda_EA1B():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_EA1B)
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
        "#01405Fお前たち……\x02",
    )

    CloseMessageWindow()

    #C0534
    ChrTalk(
        0x19,
        (
            "#01005Fなんだ、来やがったのか？\x02\x03",

            "#01006Fったく、忙しいんだから\x01",
            "見舞いは俺一人でいいって\x01",
            "言っておいたんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0535
    ChrTalk(
        0x101,
        (
            "#12P#00012Fす、すみません、課長。\x02\x03",

            "#00000Fどうしても\x01",
            "シズクちゃんの様子が\x01",
            "気になってしまって……\x02",
        )
    )

    CloseMessageWindow()

    #C0536
    ChrTalk(
        0xD,
        (
            "#5P#11202Fふふ、みなさん……\x01",
            "わざわざありがとうございます。\x02",
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
        "#6P#00105Fシズクちゃん、目が開いて……\x02",
    )

    CloseMessageWindow()

    #C0538
    ChrTalk(
        0x109,
        (
            "#12P#10105Fその、もしかして、\x01",
            "見えてるの……？\x02",
        )
    )

    CloseMessageWindow()

    #C0539
    ChrTalk(
        0xD,
        "#5P#11208F……いえ、残念ですけど。\x02",
    )

    CloseMessageWindow()

    #C0540
    ChrTalk(
        0xF,
        (
            "#01403F……今回の手術では、\x01",
            "セイランド医師が執刀医として\x01",
            "最善を尽くしてくれた。\x02\x03",

            "#01400F手術はひとまず成功したが……\x01",
            "完治までには至らなくてな。\x02\x03",

            "#01408F周囲の光を感じられる程度に\x01",
            "回復するのがやっとだったそうだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0541
    ChrTalk(
        0x104,
        "#12P#00303Fそう、か……\x02",
    )

    CloseMessageWindow()

    #C0542
    ChrTalk(
        0x103,
        "#12P#00208F何と言っていいか……\x02",
    )

    CloseMessageWindow()

    #C0543
    ChrTalk(
        0xD,
        (
            "#5P#11200Fふふ、気にしないで下さい。\x01",
            "私は大丈夫ですから。\x02\x03",

            "#11202Fそれよりお父さん……\x01",
            "私、みんなで屋上に行きたいな。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x19, 0xD, 500)

    #C0544
    ChrTalk(
        0x19,
        (
            "#6P#01002Fああ、いいかもしれねえな。\x02\x03",

            "#01004F病室にこれだけの人数が\x01",
            "集まってるのも何だし、\x01",
            "新鮮な空気を吸いたいとこだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0545
    ChrTalk(
        0x101,
        (
            "#12P#00005Fで、でもシズクちゃん、\x01",
            "手術して間もないんだし\x01",
            "無理しないほうが……\x02",
        )
    )

    CloseMessageWindow()

    #C0546
    ChrTalk(
        0xF,
        (
            "#01403F……いや、医師によれば\x01",
            "強い光に長時間晒さなければ\x01",
            "そこまで悪影響はないらしい。\x02\x03",

            "#01400F今日くらいの天気なら、\x01",
            "多少の外出も問題ないはずだ。\x02\x03",

            "#01403F……許可をもらってくる。\x01",
            "すまないがシズクの準備を\x01",
            "手伝ってやってくれ。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_F044():
        OP_95(0xFE, -100000, 50, 49000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_F044)

    def lambda_F05E():

        label("loc_F05E")

        TurnDirection(0xFE, 0xF, 500)
        Yield()
        Jump("loc_F05E")

    QueueWorkItem2(0x19, 2, lambda_F05E)

    def lambda_F070():

        label("loc_F070")

        TurnDirection(0xFE, 0xF, 500)
        Yield()
        Jump("loc_F070")

    QueueWorkItem2(0x101, 2, lambda_F070)

    def lambda_F082():

        label("loc_F082")

        TurnDirection(0xFE, 0xF, 500)
        Yield()
        Jump("loc_F082")

    QueueWorkItem2(0x102, 2, lambda_F082)

    def lambda_F094():

        label("loc_F094")

        TurnDirection(0xFE, 0xF, 500)
        Yield()
        Jump("loc_F094")

    QueueWorkItem2(0x103, 2, lambda_F094)

    def lambda_F0A6():

        label("loc_F0A6")

        TurnDirection(0xFE, 0xF, 500)
        Yield()
        Jump("loc_F0A6")

    QueueWorkItem2(0x104, 2, lambda_F0A6)

    def lambda_F0B8():

        label("loc_F0B8")

        TurnDirection(0xFE, 0xF, 500)
        Yield()
        Jump("loc_F0B8")

    QueueWorkItem2(0x109, 2, lambda_F0B8)

    def lambda_F0CA():

        label("loc_F0CA")

        TurnDirection(0xFE, 0xF, 500)
        Yield()
        Jump("loc_F0CA")

    QueueWorkItem2(0x105, 2, lambda_F0CA)
    BeginChrThread(0x1A, 1, 0, 74)
    WaitChrThread(0xF, 1)

    def lambda_F0E6():
        OP_95(0xFE, -100000, 50, 47000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_F0E6)

    def lambda_F100():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_F100)
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
        "#00105Fあ……\x02",
    )

    CloseMessageWindow()

    #C0548
    ChrTalk(
        0x105,
        (
            "#12P#10304Fやれやれ、あの《風の剣聖》も\x01",
            "娘にはとことん甘いみたいだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0549
    ChrTalk(
        0xD,
        (
            "#5P#11209Fお父さんは普段から\x01",
            "とっても優しいんですよ。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_F1D4():
        TurnDirection(0x101, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_F1D4)
    Sleep(50)

    def lambda_F1E4():
        TurnDirection(0x102, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_F1E4)
    Sleep(50)

    def lambda_F1F4():
        TurnDirection(0x104, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_F1F4)
    Sleep(50)

    def lambda_F204():
        TurnDirection(0x103, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_F204)
    Sleep(50)

    def lambda_F214():
        TurnDirection(0x105, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_F214)
    Sleep(50)

    def lambda_F224():
        TurnDirection(0x109, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_F224)
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
            "#01004Fま、そういう話なら\x01",
            "せっかくだし付き合ってくか。\x02",
        )
    )

    CloseMessageWindow()

    #C0551
    ChrTalk(
        0x101,
        "#12P#00000Fええ……そうですね。\x02",
    )

    CloseMessageWindow()

    #C0552
    ChrTalk(
        0xD,
        "#5P#11202Fふふ、よろしくお願いします。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 1)
    NewScene("t1600", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_67_E5E6 end

    def Function_68_F2F0(): pass

    label("Function_68_F2F0")


    def lambda_F2F5():
        OP_95(0xFE, -100000, 50, 50000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F2F5)

    def lambda_F30F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_F30F)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_F328():
        OP_95(0xFE, -99000, 50, 53000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F328)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_68_F2F0 end

    def Function_69_F349(): pass

    label("Function_69_F349")


    def lambda_F34E():
        OP_95(0xFE, -100000, 50, 50000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F34E)

    def lambda_F368():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_F368)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_F381():
        OP_95(0xFE, -100940, 50, 53000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F381)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_69_F349 end

    def Function_70_F3A2(): pass

    label("Function_70_F3A2")


    def lambda_F3A7():
        OP_95(0xFE, -100000, 50, 50000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F3A7)

    def lambda_F3C1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_F3C1)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_F3DA():
        OP_95(0xFE, -98340, 0, 52200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F3DA)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_70_F3A2 end

    def Function_71_F3FB(): pass

    label("Function_71_F3FB")


    def lambda_F400():
        OP_95(0xFE, -100000, 50, 50000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F400)

    def lambda_F41A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_F41A)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_F433():
        OP_95(0xFE, -100740, 0, 51800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F433)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_71_F3FB end

    def Function_72_F454(): pass

    label("Function_72_F454")


    def lambda_F459():
        OP_95(0xFE, -100000, 50, 50000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F459)

    def lambda_F473():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_F473)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_F48C():
        OP_95(0xFE, -99240, 0, 50800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F48C)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_72_F454 end

    def Function_73_F4AD(): pass

    label("Function_73_F4AD")


    def lambda_F4B2():
        OP_95(0xFE, -100000, 50, 50000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F4B2)

    def lambda_F4CC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_F4CC)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_F4E5():
        OP_95(0xFE, -100740, 0, 50600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F4E5)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_73_F4AD end

    def Function_74_F506(): pass

    label("Function_74_F506")

    Sleep(2600)
    Sound(107, 0, 100, 0)
    Sleep(1100)
    Sound(107, 0, 100, 0)
    Return()

    # Function_74_F506 end

    def Function_75_F519(): pass

    label("Function_75_F519")

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
            "#12P#01002F……それじゃあ俺は、\x01",
            "そろそろ支援課に戻らせて\x01",
            "もらうとしよう。\x02\x03",

            "#01004Fアリオス、今日はしっかりと\x01",
            "シズクちゃんのそばにいてやれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0554
    ChrTalk(
        0xF,
        "#01403F……ええ、そうさせて頂きます。\x02",
    )

    CloseMessageWindow()

    #C0555
    ChrTalk(
        0x101,
        "#12P#00000Fお疲れ様です、課長。\x02",
    )

    CloseMessageWindow()
    OP_93(0x19, 0xB4, 0x1F4)

    #C0556
    ChrTalk(
        0x19,
        (
            "#01005Fああ、お前らの方は引き続き、\x01",
            "《幻獣》の調査を進めとけ。\x02\x03",

            "#01002F《風の剣聖》が動けないうちに\x01",
            "せいぜい実績を上げるんだな。\x02",
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
        "#6P#00106Fか、課長……\x02",
    )

    CloseMessageWindow()

    #C0558
    ChrTalk(
        0x19,
        "#01004Fクク、それじゃあな。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xD, 0x2)

    #C0559
    ChrTalk(
        0xD,
        (
            "#5P#11202Fあ……\x01",
            "ありがとうございました。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x19, 0xD, 500)
    Sleep(500)
    OP_93(0x19, 0xB4, 0x1F4)

    def lambda_F8AB():
        OP_95(0xFE, -99820, 0, 54000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_F8AB)
    WaitChrThread(0x19, 1)

    def lambda_F8C9():
        OP_95(0xFE, -100000, 50, 49000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_F8C9)

    def lambda_F8E3():

        label("loc_F8E3")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_F8E3")

    QueueWorkItem2(0xF, 2, lambda_F8E3)

    def lambda_F8F5():

        label("loc_F8F5")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_F8F5")

    QueueWorkItem2(0x101, 2, lambda_F8F5)

    def lambda_F907():

        label("loc_F907")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_F907")

    QueueWorkItem2(0x102, 2, lambda_F907)

    def lambda_F919():

        label("loc_F919")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_F919")

    QueueWorkItem2(0x103, 2, lambda_F919)

    def lambda_F92B():

        label("loc_F92B")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_F92B")

    QueueWorkItem2(0x104, 2, lambda_F92B)

    def lambda_F93D():

        label("loc_F93D")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_F93D")

    QueueWorkItem2(0x109, 2, lambda_F93D)

    def lambda_F94F():

        label("loc_F94F")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_F94F")

    QueueWorkItem2(0x105, 2, lambda_F94F)
    Sleep(1500)
    Sound(107, 0, 100, 0)
    WaitChrThread(0x19, 1)

    def lambda_F96E():
        OP_95(0xFE, -100000, 50, 47000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_F96E)

    def lambda_F988():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_F988)
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
            "#5P#00306Fやれやれ、当の《風の剣聖》を\x01",
            "目の前に言う事かっつーの。\x02",
        )
    )

    CloseMessageWindow()

    #C0561
    ChrTalk(
        0x105,
        "#11P#10300Fフフ、相変わらずだよね。\x02",
    )

    CloseMessageWindow()

    #C0562
    ChrTalk(
        0xF,
        (
            "#01402Fフフ、俺の警察時代から\x01",
            "優秀な上司であることは\x01",
            "間違いないのだがな。\x02\x03",

            "#01403F……《幻獣》の調査のことは、\x01",
            "俺の方からもよろしく頼む。\x02\x03",

            "#01400F俺も明日には復帰して\x01",
            "加わる予定だが、それまでは\x01",
            "スコットたちを助けてやってくれ。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_FB23():
        TurnDirection(0x101, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_FB23)
    Sleep(50)

    def lambda_FB33():
        TurnDirection(0x102, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_FB33)
    Sleep(50)

    def lambda_FB43():
        TurnDirection(0x104, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_FB43)
    Sleep(50)

    def lambda_FB53():
        TurnDirection(0x103, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_FB53)
    Sleep(50)

    def lambda_FB63():
        TurnDirection(0x105, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_FB63)
    Sleep(50)

    def lambda_FB73():
        TurnDirection(0x109, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_FB73)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)

    #C0563
    ChrTalk(
        0x103,
        "#12P#00200Fはい、善処させて頂きます。\x02",
    )

    CloseMessageWindow()

    #C0564
    ChrTalk(
        0xD,
        (
            "#5P#11202F皆さんも本当に\x01",
            "ありがとうございました。\x02\x03",

            "#11209F色々お話できてよかったです。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_FC1F():
        TurnDirection(0x101, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_FC1F)
    Sleep(50)

    def lambda_FC2F():
        TurnDirection(0x102, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_FC2F)
    Sleep(50)

    def lambda_FC3F():
        TurnDirection(0x104, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_FC3F)
    Sleep(50)

    def lambda_FC4F():
        TurnDirection(0x103, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_FC4F)
    Sleep(50)

    def lambda_FC5F():
        TurnDirection(0x105, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_FC5F)
    Sleep(50)

    def lambda_FC6F():
        TurnDirection(0x109, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_FC6F)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)

    #C0565
    ChrTalk(
        0x109,
        "#12P#10100Fううん、私たちもすごく楽しかったよ。\x02",
    )

    CloseMessageWindow()

    #C0566
    ChrTalk(
        0x101,
        "#12P#00000Fまた来るから、元気にしていてくれ。\x02",
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

    # Function_75_F519 end

    def Function_76_FD4C(): pass

    label("Function_76_FD4C")

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
            "#00005Fあれ、ここはシズクちゃんの\x01",
            "病室のハズだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0568
    ChrTalk(
        0x102,
        "#6P#00100F今は外出中なのかもしれないわ。\x02",
    )

    CloseMessageWindow()

    #C0569
    ChrTalk(
        0x103,
        (
            "#6P#00200Fでも、この病棟では\x01",
            "見かけませんでしたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0570
    ChrTalk(
        0x104,
        "#12P#00300Fま、気が向いたら探してみるか？\x02",
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

    # Function_76_FD4C end

    def Function_77_FF93(): pass

    label("Function_77_FF93")

    StopBGM(0xBB8)

    #C0571
    ChrTalk(
        0xB,
        "#11603Fところで───\x02",
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
            "#11602F……そこにいる誰かさんは\x01",
            "まだその気になってくれないみたいね？\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10145")
    SetChrPos(0x109, -100670, 0, -7660, 90)
    Jump("loc_1018C")

    label("loc_10145")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1016B")
    SetChrPos(0x105, -100670, 0, -7660, 90)
    Jump("loc_1018C")

    label("loc_1016B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1018C")
    SetChrPos(0x10A, -100670, 0, -7660, 90)

    label("loc_1018C")

    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_0D()

    #C0573
    ChrTalk(
        0x101,
        "#6P#00005Fイ、イリアさん……？\x02",
    )

    CloseMessageWindow()

    #C0574
    ChrTalk(
        0x102,
        "#12P#00105Fいったい何を……\x02",
    )

    CloseMessageWindow()

    #C0575
    ChrTalk(
        0xB,
        (
            "#11P#11604Fフフ、誰だか知らないけど#18R㈲　㈲　㈲　㈲　㈲　㈲　㈲　㈲　㈲#\x01",
            "よっぽど恥ずかしがり屋みたいね。\x02\x03",

            "#11609F多分、控えめな性格の割には\x01",
            "ワガママでけしからんボディの\x01",
            "持ち主なんでしょうけど㈱\x02",
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
        "#12P#00306F（こりゃあ……）\x02",
    )

    CloseMessageWindow()

    #C0577
    ChrTalk(
        0x103,
        "#6P#00206F（完璧に気付かれてますね。）\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(0, 0, -1, -1)
    SetChrName("リーシャ")

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
            "#11P#11603F──誰だか知らないけど\x01",
            "あたしはもうリハビリを始めてるわ。\x02\x03",

            "#11601Fあんまり稽古をサボってると\x01",
            "すぐに追いついて引き離すわよ？\x02\x03",

            "#11604F置いてけぼりになりたくなければ\x01",
            "とっととケリを付けてきなさい。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(0, 0, -1, -1)
    SetChrName("リーシャ")

    #A0580
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#10717F#3C#40W#2S……………っっ…………………\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0581
    ChrTalk(
        0xB,
        (
            "#11P#11604Fそれと、くれぐれも気を付けて。\x02\x03",

            "#11600Fどれだけ強かろうと、\x01",
            "自分が女であるのを意識しなさい。\x02\x03",

            "#11603Fあたしたちの舞台#5R ステージ#と同じく、\x01",
            "女にしか見せられない強さもある……\x02\x03",

            "#11600Fそれがきっとあんたを守ってくれるわ。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(0, 0, -1, -1)
    SetChrName("リーシャ")

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
        "#12P#00102Fイリアさん……\x02",
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
            "#5P#11604Fフフ、余計な手間を取らせたわね。\x02\x03",

            "#11600F──弟君たちも気を付けて。\x01",
            "セシルを哀しませるんじゃないわよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0586
    ChrTalk(
        0x101,
        "#6P#00000F……はい！\x02",
    )

    CloseMessageWindow()

    #C0587
    ChrTalk(
        0x104,
        "#12P#00300F了解ッス！\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1082A")
    BeginChrThread(0x109, 1, 0, 79)
    WaitChrThread(0x109, 1)
    Jump("loc_10863")

    label("loc_1082A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10849")
    BeginChrThread(0x105, 1, 0, 79)
    WaitChrThread(0x105, 1)
    Jump("loc_10863")

    label("loc_10849")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10863")
    BeginChrThread(0x10A, 1, 0, 79)
    WaitChrThread(0x10A, 1)

    label("loc_10863")

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
            "#6P#00006Fその……すまない。\x02\x03",

            "#00008Fまさか気付かれるとは\x01",
            "思ってなくて……\x02",
        )
    )

    CloseMessageWindow()

    #C0590
    ChrTalk(
        0x104,
        (
            "#6P#00302Fリーシャちゃん、一応気配を\x01",
            "消してたハズなのになぁ？\x02",
        )
    )

    CloseMessageWindow()

    #C0591
    ChrTalk(
        0x106,
        (
            "#10710F#30Wふふ……\x01",
            "イリアさんは天才ですから……\x02\x03",

            "#10704F#30W多分、わずかな呼吸と足音で\x01",
            "すぐに分かったんだと思います……\x02\x03",

            "舞台で呼吸を合わせる時には\x01",
            "いつもしている事ですし……\x02\x03",

            "#10716F#30W本当に……舞台以外のことだと\x01",
            "めんどくさがり屋でいい加減なのに……\x02",
        )
    )

    CloseMessageWindow()

    #C0592
    ChrTalk(
        0x101,
        "#6P#00002Fそっか……\x02",
    )

    CloseMessageWindow()

    #C0593
    ChrTalk(
        0x103,
        (
            "#6P#00204F本当に……\x01",
            "イリアさんはイリアさんですね。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10AC8")

    #C0594
    ChrTalk(
        0x109,
        (
            "#6P#10109Fぐすっ……\x01",
            "でも……良かったです。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10B5B")

    label("loc_10AC8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10B14")

    #C0595
    ChrTalk(
        0x105,
        (
            "#6P#10409Fフフ……\x01",
            "つくづく彼女には驚かされるね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10B5B")

    label("loc_10B14")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10B5B")

    #C0596
    ChrTalk(
        0x10A,
        (
            "#6P#00602Fフッ……\x01",
            "さすがはイリア嬢と言うべきか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10B5B")

    OP_63(0x106, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x106)
    OP_93(0x106, 0x10E, 0x1F4)

    #C0597
    ChrTalk(
        0x106,
        (
            "#10704Fこれで──\x01",
            "私の覚悟も固まりました。\x02\x03",

            "#10702F行きましょう、皆さん……！\x02",
        )
    )

    CloseMessageWindow()

    #C0598
    ChrTalk(
        0x101,
        "#6P#00000Fああ……！\x02",
    )

    CloseMessageWindow()

    #C0599
    ChrTalk(
        0x102,
        "#6P#00100Fええ……！\x02",
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

    # Function_77_FF93 end

    def Function_78_10C49(): pass

    label("Function_78_10C49")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_10C85")
    OP_A6(0x106, 0x0, 0x1E, 0x190, 0x7D0)
    Sleep(500)
    OP_A6(0x106, 0x0, 0x1E, 0x190, 0x7D0)
    Sleep(800)
    Jump("Function_78_10C49")

    label("loc_10C85")

    Return()

    # Function_78_10C49 end

    def Function_79_10C86(): pass

    label("Function_79_10C86")

    SetChrPos(0xFE, -16470, 0, 25770, 0)

    def lambda_10C9C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_10C9C)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10CCC")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 2, 0, 80)
    Jump("loc_10D57")

    label("loc_10CCC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10CF0")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 2, 0, 81)
    Jump("loc_10D57")

    label("loc_10CF0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10D14")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 2, 0, 82)
    Jump("loc_10D57")

    label("loc_10D14")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10D38")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 2, 0, 83)
    Jump("loc_10D57")

    label("loc_10D38")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10D57")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 2, 0, 84)

    label("loc_10D57")

    Return()

    # Function_79_10C86 end

    def Function_80_10D58(): pass

    label("Function_80_10D58")

    OP_95(0xFE, -16340, 0, 28470, 2000, 0x0)
    OP_95(0xFE, -15140, 0, 29900, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_80_10D58 end

    def Function_81_10D88(): pass

    label("Function_81_10D88")

    OP_95(0xFE, -16360, 0, 29870, 2000, 0x0)
    OP_95(0xFE, -15140, 0, 31030, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_81_10D88 end

    def Function_82_10DB8(): pass

    label("Function_82_10DB8")

    OP_95(0xFE, -16400, 0, 27970, 2000, 0x0)
    OP_95(0xFE, -15140, 0, 28800, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_82_10DB8 end

    def Function_83_10DE8(): pass

    label("Function_83_10DE8")

    OP_95(0xFE, -16360, 0, 30550, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_83_10DE8 end

    def Function_84_10E04(): pass

    label("Function_84_10E04")

    OP_95(0xFE, -16360, 0, 29320, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_84_10E04 end

    def Function_85_10E20(): pass

    label("Function_85_10E20")

    StopBGM(0x7D0)
    Sleep(2000)
    Sleep(10)
    PlayBGM("ed7563", 0)
    Return()

    # Function_85_10E20 end

    def Function_86_10E30(): pass

    label("Function_86_10E30")

    EventBegin(0x0)
    Fade(500)
    SetChrSubChip(0xB, 0x2)
    OP_68(-98530, 900, -5100, 0)
    MoveCamera(44, 25, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(19850, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_END)), "loc_10F32")
    SetChrPos(0x101, -99960, 0, -5280, 90)
    SetChrPos(0x102, -99960, 0, -6600, 90)
    SetChrPos(0x103, -100870, 0, -4700, 90)
    SetChrPos(0x104, -100870, 0, -6000, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10EDC")
    SetChrPos(0x109, -100670, 0, -7360, 90)
    Jump("loc_10F23")

    label("loc_10EDC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10F02")
    SetChrPos(0x105, -100670, 0, -7360, 90)
    Jump("loc_10F23")

    label("loc_10F02")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10F23")
    SetChrPos(0x10A, -100670, 0, -7360, 90)

    label("loc_10F23")

    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    Jump("loc_110AF")

    label("loc_10F32")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x101, -99960, 0, -6000, 90)
    SetChrPos(0x102, -99960, 0, -4700, 90)
    SetChrPos(0x103, -99960, 0, -7360, 90)
    SetChrPos(0x104, -100870, 0, -4700, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10FAB")
    SetChrPos(0x109, -100870, 0, -6000, 90)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_10FAB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10FFB")
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10FEA")
    SetChrPos(0x105, -100870, 0, -6000, 90)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_10FFB")

    label("loc_10FEA")

    SetChrPos(0x105, -100670, 0, -7360, 90)

    label("loc_10FFB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1104B")
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1103A")
    SetChrPos(0x106, -100870, 0, -6000, 90)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1104B")

    label("loc_1103A")

    SetChrPos(0x106, -100670, 0, -7360, 90)

    label("loc_1104B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1109B")
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1108A")
    SetChrPos(0x10A, -100870, 0, -6000, 90)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1109B")

    label("loc_1108A")

    SetChrPos(0x10A, -100670, 0, -7360, 90)

    label("loc_1109B")

    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)

    label("loc_110AF")

    OP_0D()

    #C0600
    ChrTalk(
        0xB,
        (
            "#11P#11600Fそうだ、弟君……\x01",
            "これを持っていってくれる？\x02",
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
            "を手に入れた。\x02",
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
        "#6P#00000Fこれは……？\x02",
    )

    CloseMessageWindow()

    #C0603
    ChrTalk(
        0xB,
        (
            "#11P#11600Fあたしが初めて\x01",
            "主役として舞台に立ったときに\x01",
            "つけていた髪飾りでね。\x02\x03",

            "#11604F初心を忘れないように\x01",
            "肌身離さず持っていたのよね。\x02\x03",

            "#11609Fフフ、マニア垂涎の\x01",
            "レアな一品だと思わない？\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_112B0")
    OP_63(0x5, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_112B0")

    Sleep(1000)

    #C0604
    ChrTalk(
        0x104,
        (
            "#6P#00303F（確かに、どんな大金を積んでも\x01",
            "  欲しがりそうな奴はいそうだな……）\x02",
        )
    )

    CloseMessageWindow()

    #C0605
    ChrTalk(
        0x101,
        (
            "#6P#00005Fで、でも……\x01",
            "そんな大切な物を\x01",
            "もらってしまっていいんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0606
    ChrTalk(
        0xB,
        (
            "#11P#11604Fフフ、いいのいいの。\x01",
            "今までのお礼だから。\x02\x03",

            "#11600F良かったらお守りとして\x01",
            "持っていっちゃって。\x02",
        )
    )

    CloseMessageWindow()

    #C0607
    ChrTalk(
        0x101,
        (
            "#6P#00002F……ありがとうございます。\x01",
            "大事にさせてもらいます。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_END)), "loc_1141B")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    Jump("loc_1142F")

    label("loc_1141B")

    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)

    label("loc_1142F")

    SetChrPos(0x0, -100140, 0, -6120, 90)
    SetScenarioFlags(0x1AD, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AD, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BC, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DE, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D9, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DE, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1145F")
    OP_E0(0x34, 0x0)

    label("loc_1145F")

    EventEnd(0x5)
    Return()

    # Function_86_10E30 end

    def Function_87_11462(): pass

    label("Function_87_11462")

    EventBegin(0x1)
    Call(0, 92)
    SetChrPos(0x0, -13440, 0, 8760, 89)
    EventEnd(0x4)
    Return()

    # Function_87_11462 end

    def Function_88_1147B(): pass

    label("Function_88_1147B")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1148F")
    Call(0, 92)
    Jump("loc_11492")

    label("loc_1148F")

    Call(0, 94)

    label("loc_11492")

    SetChrPos(0x0, -9210, 0, 13390, 180)
    EventEnd(0x4)
    Return()

    # Function_88_1147B end

    def Function_89_114A6(): pass

    label("Function_89_114A6")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_114BA")
    Call(0, 94)
    Jump("loc_114BD")

    label("loc_114BA")

    Call(0, 93)

    label("loc_114BD")

    SetChrPos(0x0, 1350, 0, 80, 89)
    EventEnd(0x4)
    Return()

    # Function_89_114A6 end

    def Function_90_114D1(): pass

    label("Function_90_114D1")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_114E5")
    Call(0, 94)
    Jump("loc_114E8")

    label("loc_114E5")

    Call(0, 93)

    label("loc_114E8")

    SetChrPos(0x0, -5500, 0, 12500, 225)
    EventEnd(0x4)
    Return()

    # Function_90_114D1 end

    def Function_91_114FC(): pass

    label("Function_91_114FC")

    EventBegin(0x1)
    Call(0, 93)
    SetChrPos(0x0, -19350, 0, 29820, 89)
    EventEnd(0x4)
    Return()

    # Function_91_114FC end

    def Function_92_11515(): pass

    label("Function_92_11515")


    #C0608
    ChrTalk(
        0x101,
        (
            "#00000Fフランの病室は３０１号室だったな。\x01",
            "早いところ様子を見に行こう。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Return()

    # Function_92_11515 end

    def Function_93_11563(): pass

    label("Function_93_11563")


    #C0609
    ChrTalk(
        0x136,
        (
            "#01300Fイリアの病室は３０３号室よ。\x02\x03",

            "あまり時間は取れないと思うから、\x01",
            "すぐに向かってもらっていいかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0610
    ChrTalk(
        0x101,
        "#00001Fそうだね、了解したよ。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Return()

    # Function_93_11563 end

    def Function_94_115F6(): pass

    label("Function_94_115F6")


    #C0611
    ChrTalk(
        0x136,
        (
            "#01300Fドノバンさんの病室は３０２号室よ。\x02\x03",

            "あまり時間は取れないと思うから、\x01",
            "すぐに向かってもらっていいかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0612
    ChrTalk(
        0x101,
        "#00000Fそうだね、了解したよ。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Return()

    # Function_94_115F6 end

    SaveToFile()

Try(main)
