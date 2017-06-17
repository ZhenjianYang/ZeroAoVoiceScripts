from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t2510.bin",                # FileName
        "t2510",                    # MapName
        "t2510",                    # Location
        0x005A,                     # MapIndex
        "ed7126",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 90, 0, 2, 0, 3],
    )

    BuildStringList((
        "t2510",                  # 0
        "オリバー隊員",           # 1
        "ジャック隊員",           # 2
        "アレクセイ隊員",         # 3
        "ティマス",               # 4
        "ラグ",                   # 5
        "観光客",                 # 6
        "商人",                   # 7
        "男の子",                 # 8
        "観光客",                 # 9
        "観光客",                 # 10
        "観光客",                 # 11
        "観光客",                 # 12
        "商人",                   # 13
        "観光客",                 # 14
        "観光客",                 # 15
        "観光客",                 # 16
        "観光客",                 # 17
        "観光客",                 # 18
        "観光客",                 # 19
        "観光客",                 # 20
        "観光客",                 # 21
        "商人",                   # 22
        "観光客",                 # 23
        "観光客",                 # 24
        "観光客",                 # 25
        "観光客",                 # 26
        "ハロルド",               # 27
        "チルル",                 # 28
        "遊撃士スコット",         # 29
        "遊撃士ヴェンツェル",     # 30
        "遊撃士リン",             # 31
        "遊撃士エオリア",         # 32
        "車１",                   # 33
        "ノエル曹長",             # 34
        "黒髪の女性",             # 35
        "お婆さん",               # 36
        "老人",                   # 37
        "貿易商",                 # 38
        "女性",                   # 39
        "兄",                     # 40
        "妹",                     # 41
        "父親",                   # 42
        "男の子",                 # 43
        "バス",                   # 44
    ))

    AddCharChip((
        "chr/ch31200.itc",                   # 00
        "chr/ch31302.itc",                   # 01
        "chr/ch25000.itc",                   # 02
        "chr/ch31300.itc",                   # 03
        "chr/ch23400.itc",                   # 04
        "chr/ch21202.itc",                   # 05
        "chr/ch21000.itc",                   # 06
        "chr/ch21402.itc",                   # 07
        "chr/ch21900.itc",                   # 08
        "chr/ch21200.itc",                   # 09
        "chr/ch21100.itc",                   # 0A
        "chr/ch20500.itc",                   # 0B
        "chr/ch20802.itc",                   # 0C
        "chr/ch21002.itc",                   # 0D
        "chr/ch21102.itc",                   # 0E
        "chr/ch21800.itc",                   # 0F
        "chr/ch21602.itc",                   # 10
        "chr/ch09300.itc",                   # 11
        "chr/ch21600.itc",                   # 12
        "chr/ch27202.itc",                   # 13
        "chr/ch27302.itc",                   # 14
        "chr/ch32002.itc",                   # 15
        "chr/ch32102.itc",                   # 16
        "chr/ch00800.itc",                   # 17
        "chr/ch07300.itc",                   # 18
        "chr/ch24100.itc",                   # 19
        "chr/ch20800.itc",                   # 1A
        "chr/ch33000.itc",                   # 1B
        "chr/ch24500.itc",                   # 1C
        "chr/ch21300.itc",                   # 1D
        "chr/ch21400.itc",                   # 1E
        "chr/ch07302.itc",                   # 1F
        "chr/ch24102.itc",                   # 20
        "chr/ch21302.itc",                   # 21
        "chr/ch21402.itc",                   # 22
    ))

    DeclNpc(7780,    0,       6809,    180,  257,  0x0, 0,   3,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(-4280,   0,       5130,    180,  257,  0x0, 0,   0,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(95629,   150,     2380,    270,  341,  0x0, 0,   1,   0,   255, 255, 0,   7,   255,  0)
    DeclNpc(106529,  0,       1980,    270,  257,  0x0, 0,   2,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(163020,  0,       -2410,   270,  257,  0x0, 0,   4,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(102949,  150,     3920,    270,  469,  0x0, 0,   5,   0,   255, 255, 0,   13,  255,  0)
    DeclNpc(7519,    0,       5110,    0,    401,  0x0, 0,   6,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(98620,   150,     -2180,   90,   469,  0x0, 0,   7,   0,   255, 255, 0,   14,  255,  0)
    DeclNpc(7519,    0,       5110,    0,    401,  0x0, 0,   8,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(-660,    0,       6809,    180,  385,  0x0, 0,   9,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(100970,  150,     -3950,   270,  469,  0x0, 0,   5,   0,   255, 255, 0,   16,  255,  0)
    DeclNpc(-4150,   0,       3960,    0,    401,  0x0, 0,   10,  0,   0,   0,   0,   17,  255,  0)
    DeclNpc(6650,    0,       -2170,   0,    385,  0x0, 0,   6,   0,   0,   0,   0,   18,  255,  0)
    DeclNpc(7519,    0,       5110,    0,    401,  0x0, 0,   18,  0,   0,   0,   0,   5,   255,  0)
    DeclNpc(98620,   150,     -3950,   90,   469,  0x0, 0,   5,   0,   255, 255, 0,   19,  255,  0)
    DeclNpc(8100,    0,       -3130,   0,    401,  0x0, 0,   6,   0,   0,   0,   0,   20,  255,  0)
    DeclNpc(1539,    0,       2160,    180,  401,  0x0, 0,   9,   0,   0,   0,   0,   21,  255,  0)
    DeclNpc(100569,  150,     2150,    90,   469,  0x0, 0,   12,  0,   255, 255, 0,   22,  255,  0)
    DeclNpc(-8500,   0,       3460,    180,  385,  0x0, 0,   15,  0,   0,   0,   0,   23,  255,  0)
    DeclNpc(100569,  150,     2150,    90,   469,  0x0, 0,   13,  0,   255, 255, 0,   24,  255,  0)
    DeclNpc(102949,  150,     2150,    270,  469,  0x0, 0,   14,  0,   255, 255, 0,   25,  255,  0)
    DeclNpc(6960,    0,       2359,    180,  385,  0x0, 0,   15,  0,   0,   0,   0,   26,  255,  0)
    DeclNpc(98620,   150,     -2180,   90,   469,  0x0, 0,   16,  0,   255, 255, 0,   27,  255,  0)
    DeclNpc(7489,    0,       2099,    180,  385,  0x0, 0,   15,  0,   0,   0,   0,   28,  255,  0)
    DeclNpc(6349,    0,       2099,    180,  385,  0x0, 0,   8,   0,   0,   0,   0,   29,  255,  0)
    DeclNpc(98620,   150,     -3950,   90,   469,  0x0, 0,   5,   0,   255, 255, 0,   30,  255,  0)
    DeclNpc(-16989,  0,       -6710,   135,  389,  0x0, 0,   17,  0,   0,   0,   0,   31,  255,  0)
    DeclNpc(156389,  0,       -3119,   270,  389,  0x0, 0,   11,  0,   0,   0,   0,   32,  255,  0)
    DeclNpc(102900,  150,     4030,    270,  469,  0x0, 0,   19,  0,   255, 255, 0,   33,  255,  0)
    DeclNpc(100569,  150,     3920,    90,   469,  0x0, 0,   20,  0,   255, 255, 0,   34,  255,  0)
    DeclNpc(100599,  109,     4019,    90,   469,  0x0, 0,   21,  0,   255, 255, 0,   35,  255,  0)
    DeclNpc(102900,  150,     4030,    270,  469,  0x0, 0,   22,  0,   255, 255, 0,   36,  255,  0)
    DeclNpc(7000,    0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(-59,     0,       -5000,   0,    389,  0x0, 0,   23,  0,   0,   0,   0,   37,  255,  0)
    DeclNpc(-2309,   0,       6309,    180,  469,  0x0, 0,   24,  0,   255, 255, 0,   38,  255,  0)
    DeclNpc(-2309,   0,       6309,    180,  405,  0x0, 0,   25,  0,   255, 255, 0,   39,  255,  0)
    DeclNpc(-2309,   0,       6309,    180,  389,  0x0, 0,   26,  0,   255, 255, 0,   40,  255,  0)
    DeclNpc(-2309,   0,       6309,    180,  389,  0x0, 0,   27,  0,   255, 255, 0,   41,  255,  0)
    DeclNpc(-2309,   0,       6309,    180,  389,  0x0, 0,   28,  0,   255, 255, 0,   42,  255,  0)
    DeclNpc(-2309,   0,       6309,    180,  469,  0x0, 0,   9,   0,   255, 255, 0,   43,  255,  0)
    DeclNpc(-2309,   0,       6309,    180,  469,  0x0, 0,   29,  0,   255, 255, 0,   44,  255,  0)
    DeclNpc(-2309,   0,       6309,    180,  469,  0x0, 0,   6,   0,   255, 255, 0,   45,  255,  0)
    DeclNpc(-2309,   0,       6309,    180,  469,  0x0, 0,   30,  0,   255, 255, 0,   46,  255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 71,  95.81999969482422,     -8.289999961853027,    0.0,                   4.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   0.0,                   -47.90999984741211,    4.144999980926514,     -0.0,                  1.0])
    DeclEvent(0x0000, 0, 72,  89.77999877929688,     -0.11999999731779099,  0.0,                   4.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   0.0,                   -44.88999938964844,    0.05999999865889549,   -0.0,                  1.0])
    DeclEvent(0x0000, 0, 73,  -8.050000190734863,    10.380000114440918,    0.0,                   4.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   0.0,                   4.025000095367432,     -5.190000057220459,    -0.0,                  1.0])
    DeclEvent(0x0000, 0, 74,  -0.05000000074505806,  10.520000457763672,    0.0,                   4.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   0.0,                   0.02500000037252903,   -5.260000228881836,    -0.0,                  1.0])

    DeclActor(7580,    0,       5630,    1000,    7780,    1500,    6810,    0x007E, 0,  4,  0x0000)
    DeclActor(105420,  0,       1980,    1000,    106530,  1500,    1980,    0x007E, 0,  8,  0x0000)
    DeclActor(161990,  0,       -2450,   1000,    163020,  1500,    -2410,   0x007E, 0,  11, 0x0000)
    DeclActor(-1750,   0,       -12300,  1000,    -1750,   1000,    -12300,  0x007C, 0,  75, 0x0000)

    ScpFunction((
        "Function_0_930",          # 00, 0
        "Function_1_9E8",          # 01, 1
        "Function_2_A13",          # 02, 2
        "Function_3_C39",          # 03, 3
        "Function_4_E46",          # 04, 4
        "Function_5_E4A",          # 05, 5
        "Function_6_195F",         # 06, 6
        "Function_7_1D80",         # 07, 7
        "Function_8_26A8",         # 08, 8
        "Function_9_26AC",         # 09, 9
        "Function_10_304A",        # 0A, 10
        "Function_11_319C",        # 0B, 11
        "Function_12_31A0",        # 0C, 12
        "Function_13_3837",        # 0D, 13
        "Function_14_3997",        # 0E, 14
        "Function_15_3AE3",        # 0F, 15
        "Function_16_3B67",        # 10, 16
        "Function_17_3CF8",        # 11, 17
        "Function_18_3D45",        # 12, 18
        "Function_19_3E06",        # 13, 19
        "Function_20_3F87",        # 14, 20
        "Function_21_3FC1",        # 15, 21
        "Function_22_3FE6",        # 16, 22
        "Function_23_4134",        # 17, 23
        "Function_24_41B5",        # 18, 24
        "Function_25_4347",        # 19, 25
        "Function_26_4372",        # 1A, 26
        "Function_27_43F3",        # 1B, 27
        "Function_28_4647",        # 1C, 28
        "Function_29_46EB",        # 1D, 29
        "Function_30_4773",        # 1E, 30
        "Function_31_48BE",        # 1F, 31
        "Function_32_49E3",        # 20, 32
        "Function_33_4A93",        # 21, 33
        "Function_34_4DF8",        # 22, 34
        "Function_35_4F6E",        # 23, 35
        "Function_36_52CA",        # 24, 36
        "Function_37_5572",        # 25, 37
        "Function_38_55FD",        # 26, 38
        "Function_39_5B10",        # 27, 39
        "Function_40_5F43",        # 28, 40
        "Function_41_6338",        # 29, 41
        "Function_42_661A",        # 2A, 42
        "Function_43_6A0C",        # 2B, 43
        "Function_44_6E4C",        # 2C, 44
        "Function_45_6FCA",        # 2D, 45
        "Function_46_7309",        # 2E, 46
        "Function_47_750F",        # 2F, 47
        "Function_48_8227",        # 30, 48
        "Function_49_8246",        # 31, 49
        "Function_50_8265",        # 32, 50
        "Function_51_8284",        # 33, 51
        "Function_52_82A3",        # 34, 52
        "Function_53_8358",        # 35, 53
        "Function_54_8422",        # 36, 54
        "Function_55_84C0",        # 37, 55
        "Function_56_8530",        # 38, 56
        "Function_57_8639",        # 39, 57
        "Function_58_863A",        # 3A, 58
        "Function_59_8F08",        # 3B, 59
        "Function_60_8F27",        # 3C, 60
        "Function_61_8F46",        # 3D, 61
        "Function_62_8F65",        # 3E, 62
        "Function_63_8F84",        # 3F, 63
        "Function_64_8FB4",        # 40, 64
        "Function_65_9020",        # 41, 65
        "Function_66_9071",        # 42, 66
        "Function_67_90E0",        # 43, 67
        "Function_68_9131",        # 44, 68
        "Function_69_91B1",        # 45, 69
        "Function_70_920C",        # 46, 70
        "Function_71_9236",        # 47, 71
        "Function_72_92EE",        # 48, 72
        "Function_73_93A6",        # 49, 73
        "Function_74_9405",        # 4A, 74
        "Function_75_9464",        # 4B, 75
    ))


    def Function_0_930(): pass

    label("Function_0_930")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_970"),
        (1, "loc_97C"),
        (2, "loc_988"),
        (3, "loc_994"),
        (4, "loc_9A0"),
        (5, "loc_9AC"),
        (6, "loc_9B8"),
        (SWITCH_DEFAULT, "loc_9C4"),
    )


    label("loc_970")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_9D0")

    label("loc_97C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_9D0")

    label("loc_988")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_9D0")

    label("loc_994")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_9D0")

    label("loc_9A0")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_9D0")

    label("loc_9AC")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_9D0")

    label("loc_9B8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_9D0")

    label("loc_9C4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_9D0")

    label("loc_9D0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9E7")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_9D0")

    label("loc_9E7")

    Return()

    # Function_0_930 end

    def Function_1_9E8(): pass

    label("Function_1_9E8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A12")
    OP_94(0xFE, 0xFFFFF178, 0x1360, 0x8C0, 0x1EDC, 0x3E8)
    Sleep(450)
    Jump("Function_1_9E8")

    label("loc_A12")

    Return()

    # Function_1_9E8 end

    def Function_2_A13(): pass

    label("Function_2_A13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_A30")
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    Jump("loc_BDE")

    label("loc_A30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_A4D")
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x22, 0x80)
    Jump("loc_BDE")

    label("loc_A4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_A74")
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    Jump("loc_BDE")

    label("loc_A74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_AA2")
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x9, 7150, 0, -1840, 0)
    Jump("loc_BDE")

    label("loc_AA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_ABA")
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    Jump("loc_BDE")

    label("loc_ABA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_B6B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_AD2")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 47)

    label("loc_AD2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_AFE")
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x9, -4280, 0, 5130, 180)
    Jump("loc_B66")

    label("loc_AFE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0xD)"), scpexpr(EXPR_END)), "loc_B30")
    ClearChrFlags(0x29, 0x80)
    SetChrPos(0x29, 1720, 0, 7110, 270)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    Jump("loc_B66")

    label("loc_B30")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_B4A")
    SetChrFlags(0xA, 0x80)
    Call(0, 56)
    Jump("loc_B66")

    label("loc_B4A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0x3)"), scpexpr(EXPR_END)), "loc_B66")
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0x29, 0x80)

    label("loc_B66")

    Jump("loc_BDE")

    label("loc_B6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_B98")
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    BeginChrThread(0x11, 0, 0, 1)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x24, 0x80)
    ClearChrFlags(0x25, 0x80)
    Jump("loc_BDE")

    label("loc_B98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_BD0")
    SetChrPos(0x9, 7150, 0, -1840, 0)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0x26, 0x80)
    ClearChrFlags(0x27, 0x80)
    Jump("loc_BDE")

    label("loc_BD0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_BDE")
    ClearChrFlags(0xD, 0x80)

    label("loc_BDE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6D), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0x5)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0x6)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0x7)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0x9)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0xA)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0xB)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0xC)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0xD)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C38")
    Event(0, 58)

    label("loc_C38")

    Return()

    # Function_2_A13 end

    def Function_3_C39(): pass

    label("Function_3_C39")

    OP_70(0x6, 0x8C)
    OP_78(0x4, 0x28)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFrame(0x4, "light", 0x0, 0x1)
    SetMapObjFrame(0x4, "chukin", 0x0, 0x1)
    SetMapObjFrame(0x5, "light", 0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_CA2")
    ClearMapObjFlags(0x4, 0x4)
    OP_D3(0x28, 0x0, 0x15F90, 0x0, 0x0)
    Jump("loc_DB7")

    label("loc_CA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_CC9")
    ClearMapObjFlags(0x4, 0x4)
    OP_D3(0x28, 0x0, 0x41EB0, 0x0, 0x0)
    Jump("loc_DB7")

    label("loc_CC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_D0B")
    ClearMapObjFlags(0x4, 0x4)
    SetChrPos(0x28, -8690, 0, 220, 0)
    OP_D3(0x28, 0x0, 0x15F90, 0x0, 0x0)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    Jump("loc_DB7")

    label("loc_D0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_D38")
    ClearMapObjFlags(0x4, 0x4)
    OP_D3(0x28, 0x0, 0x15F90, 0x0, 0x0)
    ClearMapObjFlags(0x5, 0x4)
    Jump("loc_DB7")

    label("loc_D38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_D46")
    Jump("loc_DB7")

    label("loc_D46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_D79")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_D74")
    ClearMapObjFlags(0x4, 0x4)
    OP_D3(0x28, 0x0, 0x41EB0, 0x0, 0x0)

    label("loc_D74")

    Jump("loc_DB7")

    label("loc_D79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_D87")
    Jump("loc_DB7")

    label("loc_D87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_DAE")
    ClearMapObjFlags(0x4, 0x4)
    OP_D3(0x28, 0x0, 0x41EB0, 0x0, 0x0)
    Jump("loc_DB7")

    label("loc_DAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_DB7")

    label("loc_DB7")

    SetMapObjFlags(0x8, 0x4)
    SetMapObjFrame(0x8, "light", 0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_DD8")
    Jump("loc_DE7")

    label("loc_DD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_DE7")
    ClearMapObjFlags(0x8, 0x4)

    label("loc_DE7")

    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    ModifyEventFlags(0, 2, 0x80)
    ModifyEventFlags(0, 3, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_E0C")
    Jump("loc_E45")

    label("loc_E0C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0xD)"), scpexpr(EXPR_END)), "loc_E2E")
    SetMapObjFlags(0x4, 0x4)
    ModifyEventFlags(1, 2, 0x80)
    ModifyEventFlags(1, 3, 0x80)
    Jump("loc_E45")

    label("loc_E2E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_E45")
    ModifyEventFlags(1, 0, 0x80)
    ModifyEventFlags(1, 1, 0x80)

    label("loc_E45")

    Return()

    # Function_3_C39 end

    def Function_4_E46(): pass

    label("Function_4_E46")

    Call(0, 5)
    Return()

    # Function_4_E46 end

    def Function_5_E4A(): pass

    label("Function_5_E4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E60")
    TalkBegin(0x15)
    Jump("loc_E8F")

    label("loc_E60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E76")
    TalkBegin(0x10)
    Jump("loc_E8F")

    label("loc_E76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E8C")
    TalkBegin(0xE)
    Jump("loc_E8F")

    label("loc_E8C")

    TalkBegin(0x8)

    label("loc_E8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1012")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F72")

    #C0001
    ChrTalk(
        0x8,
        (
            "さて、今日も検問の仕事を\x01",
            "がんばらないとな。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        (
            "上層部が腐ってる以上、\x01",
            "今はどれだけ取り締まっても\x01",
            "捕まえられない連中はいるけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x8,
        (
            "俺たちのやってることは\x01",
            "きっと無意味じゃないはずだからね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_100D")

    label("loc_F72")


    #C0004
    ChrTalk(
        0x8,
        (
            "司令が賄賂をもらったりしているせいで\x01",
            "どれだけ取り締まっても\x01",
            "捕まえられない連中がいる。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x8,
        (
            "だけど、俺たちが諦めなければ\x01",
            "きっと無意味じゃないはずさ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_100D")

    Jump("loc_1919")

    label("loc_1012")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_10DF")

    #C0006
    ChrTalk(
        0x8,
        (
            "この検問で何度か\x01",
            "密輸入の品を見つけたことがあるが……\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x8,
        (
            "そういう奴らは大抵、\x01",
            "賄賂を支払って通り抜けちまうんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x8,
        (
            "ミラがあれば悪事もまかりとおる……\x01",
            "そんな仕組みは間違っているよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1919")

    label("loc_10DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_12CA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_129D")

    #C0009
    ChrTalk(
        0x8,
        (
            "ノエル曹長……\x01",
            "そちらが、例の？\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x109,
        (
            "#0500Fお世話になっている\x01",
            "特務支援課の方たちです。\x02\x03",

            "遺跡の調査に\x01",
            "協力をいただけることになりました。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x8,
        (
            "そうですか……すみません、\x01",
            "自分たちが不甲斐ないばかりに……\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x101,
        (
            "#0000Fいえ、お気になさらず。\x01",
            "こういう仕事は馴れてますからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x104,
        (
            "#0304Fハハッ、違いねえ。\x02\x03",

            "#0300Fま、調査は俺らにまかせて\x01",
            "お前らは門の警備を頑張ってくれや。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x8,
        (
            "ああ……\x01",
            "ノエル曹長のこと、よろしく頼むよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_12C5")

    label("loc_129D")


    #C0015
    ChrTalk(
        0x8,
        "ノエル曹長のこと、よろしく頼むよ。\x02",
    )

    CloseMessageWindow()

    label("loc_12C5")

    Jump("loc_1919")

    label("loc_12CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1344")

    #C0016
    ChrTalk(
        0x8,
        (
            "うーん、導力車の検分は\x01",
            "どうしてもてこずるな。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x8,
        (
            "ジャックも相当忙しそうだし……\x01",
            "応援がほしいとこだ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1919")

    label("loc_1344")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1480")
    OP_4B(0x8, 0xFF)
    OP_4B(0x15, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13F3")

    #C0018
    ChrTalk(
        0x8,
        "……はい、オーケーです。\x02",
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x8,
        (
            "共和国への定期バスは\x01",
            "あと４０分ほどで到着するので\x01",
            "それまで休んでいてください。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x15,
        "うむ、ありがとうよ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1473")

    label("loc_13F3")


    #C0021
    ChrTalk(
        0x8,
        (
            "よかったら、そちらの食堂で\x01",
            "食事でもとられてはいかがでしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x15,
        (
            "うむ、丁度腹が減っとったんじゃ。\x01",
            "利用させてもらうかの。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1473")

    OP_4C(0x8, 0xFF)
    OP_4C(0x15, 0xFF)
    Jump("loc_1919")

    label("loc_1480")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1602")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1522")

    #C0023
    ChrTalk(
        0x8,
        (
            "ジャックの奴、昼はクロスベル市の\x01",
            "貨物チェックに行っていたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x8,
        (
            "偽ブランド商の相手なんて大役、\x01",
            "しなくて済んでラッキーだよな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15FD")

    label("loc_1522")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0xD)"), scpexpr(EXPR_END)), "loc_15AF")

    #C0025
    ChrTalk(
        0x8,
        (
            "偽ブランド商か……\x01",
            "見た目じゃ見分けがつかなかったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x8,
        (
            "悪人ってやつは\x01",
            "善人のフリをするのが上手い。\x01",
            "気を付けろよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15FD")

    label("loc_15AF")


    #C0027
    ChrTalk(
        0x8,
        (
            "昼過ぎに共和国からの\x01",
            "バスが来る予定でね。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x8,
        (
            "んー……\x01",
            "忙しくなるぞー。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15FD")

    Jump("loc_1919")

    label("loc_1602")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_174F")
    OP_4B(0x8, 0xFF)
    OP_4B(0x10, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16B8")

    #C0029
    ChrTalk(
        0x8,
        (
            "それでは、こちらの入国証に\x01",
            "一応サインを……\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x10,
        (
            "さらさら……\x01",
            "これでいいかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x8,
        (
            "……はい、オーケーです。\x01",
            "記念祭、楽しんできてください。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1742")

    label("loc_16B8")


    #C0032
    ChrTalk(
        0x8,
        (
            "門を出て街道を\x01",
            "真っ直ぐ進んでいただけると\x01",
            "クロスベル市に着きます。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x8,
        "記念祭、楽しんできてください。\x02",
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x10,
        "うふふ、ご親切にどうも。\x02",
    )

    CloseMessageWindow()

    label("loc_1742")

    OP_4C(0x8, 0xFF)
    OP_4C(0x10, 0xFF)
    Jump("loc_1919")

    label("loc_174F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1881")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1836")
    OP_4B(0x8, 0xFF)
    OP_4B(0xE, 0xFF)

    #C0035
    ChrTalk(
        0x8,
        (
            "じゃ、念の為\x01",
            "積荷を検めさせていただきます。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x8,
        (
            "これも規則なので\x01",
            "しばらくお待ちください。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xE,
        (
            "色々と面倒だな……\x01",
            "まぁ、仕方ないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xE,
        (
            "息子を待たせてるんだ、\x01",
            "手短にお願いするよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    OP_4C(0x8, 0xFF)
    OP_4C(0xE, 0xFF)
    Jump("loc_187C")

    label("loc_1836")


    #C0039
    ChrTalk(
        0xE,
        (
            "やれやれ、面倒なもんだ。\x01",
            "子供が食堂で待ってんだ、\x01",
            "手短に頼むぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_187C")

    Jump("loc_1919")

    label("loc_1881")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1919")

    #C0040
    ChrTalk(
        0x8,
        (
            "ここである程度、\x01",
            "共和国と行き来する車両なんかを\x01",
            "検分するんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x8,
        (
            "でも、こんなちゃちなゲートじゃ\x01",
            "無理矢理通ろうと思えば通れちゃうよね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1919")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_192F")
    TalkEnd(0x15)
    Jump("loc_195E")

    label("loc_192F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1945")
    TalkEnd(0x10)
    Jump("loc_195E")

    label("loc_1945")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_195B")
    TalkEnd(0xE)
    Jump("loc_195E")

    label("loc_195B")

    TalkEnd(0x8)

    label("loc_195E")

    Return()

    # Function_5_E4A end

    def Function_6_195F(): pass

    label("Function_6_195F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_19C5")

    #C0042
    ChrTalk(
        0xFE,
        "異常・ナシ！\x02",
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xFE,
        (
            "自分は信頼できる上官のもと、\x01",
            "任務を遂行するのみ、であります！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D7C")

    label("loc_19C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1A30")

    #C0044
    ChrTalk(
        0xFE,
        "積み荷、異常・ナシ！\x02",
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xFE,
        (
            "受付でサインをしていただければ\x01",
            "あとはお通りできるであります！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D7C")

    label("loc_1A30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1A7D")

    #C0046
    ChrTalk(
        0xFE,
        "異常・ナシ！\x02",
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xFE,
        (
            "ノエル曹長！\x01",
            "任務、ご苦労様であります！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D7C")

    label("loc_1A7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1AD8")

    #C0048
    ChrTalk(
        0xFE,
        (
            "異常・ナシ！\x01",
            "……自分の体力以外は！\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xFE,
        "さすがに忙しすぎるであります！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1D7C")

    label("loc_1AD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1B1E")

    #C0050
    ChrTalk(
        0xFE,
        "異常・ナシ！\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xFE,
        "また忙しくなってきたであります！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1D7C")

    label("loc_1B1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1CA0")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1C1A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BD7")
    TurnDirection(0x9, 0x13, 0)

    #C0052
    ChrTalk(
        0xFE,
        (
            "クロスベル市への定期バスは\x01",
            "門を出て右手の乗り場から\x01",
            "出ているであります。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xFE,
        (
            "今日の街道は異常・ナシです！\x01",
            "気をつけて行くであります！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1C15")

    label("loc_1BD7")


    #C0054
    ChrTalk(
        0xFE,
        (
            "ふぅ……\x01",
            "初めて来る観光客も多くて\x01",
            "案内が大変であります。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C15")

    Jump("loc_1C9B")

    label("loc_1C1A")


    #C0055
    ChrTalk(
        0xFE,
        (
            "後でクロスベル市の駅に\x01",
            "出張するであります。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xFE,
        (
            "いつも駅に行っている\x01",
            "ベルガード門のロメオ隊員とは\x01",
            "仕事仲間なのであります。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C9B")

    Jump("loc_1D7C")

    label("loc_1CA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1CF7")

    #C0057
    ChrTalk(
        0xFE,
        (
            "異常・ナシ！\x01",
            "……今のところは！\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xFE,
        "忙しすぎて目が回るであります！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1D7C")

    label("loc_1CF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1D3B")

    #C0059
    ChrTalk(
        0xFE,
        "積荷、異常・ナシ！\x02",
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xFE,
        "入念に調べるであります！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1D7C")

    label("loc_1D3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1D7C")

    #C0061
    ChrTalk(
        0xFE,
        "異常・ナシ！\x02",
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xFE,
        "引き続き警備にあたるであります！\x02",
    )

    CloseMessageWindow()

    label("loc_1D7C")

    TalkEnd(0xFE)
    Return()

    # Function_6_195F end

    def Function_7_1D80(): pass

    label("Function_7_1D80")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1E14")
    Jump("loc_1E5E")

    label("loc_1E14")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1E34")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1E5E")

    label("loc_1E34")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1E54")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1E5E")

    label("loc_1E54")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1E5E")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1F19")

    #C0063
    ChrTalk(
        0xFE,
        (
            "バスの行き来が結構あるから、\x01",
            "駐車場はまめに整備しておかないとな。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xFE,
        (
            "……それにしても腹が減った。\x01",
            "はやく昼休憩にならないかな……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26A0")

    label("loc_1F19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_2042")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FEE")

    #C0065
    ChrTalk(
        0xFE,
        (
            "バレルのやつはすっかり元気に\x01",
            "なったみたいでな。\x01",
            "警備配置も元に戻ったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xFE,
        (
            "いやぁ、なれない場所の担当は\x01",
            "ホント疲れるな。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xFE,
        (
            "……とにかく俺も腹ごしらえして\x01",
            "仕事に戻るとするか。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_203D")

    label("loc_1FEE")


    #C0068
    ChrTalk(
        0xFE,
        (
            "俺も腹ごしらえして\x01",
            "仕事に戻るとしよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xFE,
        "もぐもぐ……うーん、ウマイ！\x02",
    )

    CloseMessageWindow()

    label("loc_203D")

    Jump("loc_26A0")

    label("loc_2042")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2050")
    Jump("loc_26A0")

    label("loc_2050")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_20D9")

    #C0070
    ChrTalk(
        0xFE,
        (
            "はぁ、忙しい忙しい。\x01",
            "こりゃ、さっさと食っちまわないと。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xFE,
        (
            "……でも急いで食べると\x01",
            "体に悪いんだよな。\x01",
            "ジレンマだ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26A0")

    label("loc_20D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_21DA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2155")

    #C0072
    ChrTalk(
        0xFE,
        (
            "こりゃ、明日は忙しくなるな。\x01",
            "今のうちにスタミナをつけておこう！\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)

    #C0073
    ChrTalk(
        0xFE,
        "がつがつがつがつ！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_21D5")

    label("loc_2155")

    SetChrSubChip(0xFE, 0x0)

    #C0074
    ChrTalk(
        0xFE,
        "がつがつがつがつ！\x02",
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xFE,
        (
            "っぐ！……………………\x01",
            "……………………ごくん。\x01",
            "ぷはぁ………………\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xFE,
        "……がつがつがつがつ！\x02",
    )

    CloseMessageWindow()

    label("loc_21D5")

    Jump("loc_26A0")

    label("loc_21DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2386")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2328")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22B3")

    #C0077
    ChrTalk(
        0xFE,
        (
            "観光客をいっぱい見てて\x01",
            "思い出したんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xFE,
        (
            "一度、リベール王国に\x01",
            "行ってみたいんだよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xFE,
        (
            "空気も水も美味しいらしいから\x01",
            "それはそれはウマい料理に\x01",
            "出会えるだろうよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2323")

    label("loc_22B3")


    #C0080
    ChrTalk(
        0xFE,
        (
            "個人的にはアルモリカの\x01",
            "作物も充分に美味いと思うけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xFE,
        (
            "やっぱり、リベールには\x01",
            "一度行ってみたいなぁ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2323")

    Jump("loc_2381")

    label("loc_2328")


    #C0082
    ChrTalk(
        0xFE,
        (
            "まだ昼前だってのに\x01",
            "腹が減って仕方ないよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xFE,
        "……だれか差し入れしてくれないかな。\x02",
    )

    CloseMessageWindow()

    label("loc_2381")

    Jump("loc_26A0")

    label("loc_2386")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_24CC")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_246E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_241D")

    #C0084
    ChrTalk(
        0xFE,
        (
            "この食堂はお客さんも隊員も\x01",
            "共用なんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0xFE,
        (
            "とはいえ、制服のヤツがいたら\x01",
            "お客さんは食べづらいだろうな……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2469")

    label("loc_241D")


    #C0086
    ChrTalk(
        0xFE,
        (
            "今日は人も多いし……\x01",
            "仕方ない、さっさと食って\x01",
            "持ち場に戻るとするかな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2469")

    Jump("loc_24C7")

    label("loc_246E")


    #C0087
    ChrTalk(
        0xFE,
        (
            "まだ昼前だってのに\x01",
            "腹が減って仕方ないよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xFE,
        "……だれか差し入れしてくれないかな。\x02",
    )

    CloseMessageWindow()

    label("loc_24C7")

    Jump("loc_26A0")

    label("loc_24CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2585")

    #C0089
    ChrTalk(
        0xFE,
        (
            "食堂のメシは\x01",
            "そこそこ美味いんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0xFE,
        (
            "警備隊に配給される携帯食糧#8Rレ ー シ ョ ン#は\x01",
            "ホント、食えたもんじゃないよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xFE,
        (
            "自称美食家としては\x01",
            "由々しき問題だね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26A0")

    label("loc_2585")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_26A0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_262A")

    #C0092
    ChrTalk(
        0xFE,
        (
            "もぐもぐ……\x01",
            "ウマいウマい……\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xFE,
        "食堂のメシはなかなかウマいよ。\x02",
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xFE,
        (
            "ただ、クロスベル市にある\x01",
            "龍老飯店も味ではなかなかだと思うよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_26A0")

    label("loc_262A")


    #C0095
    ChrTalk(
        0xFE,
        (
            "非番の日にクロスベル市の\x01",
            "龍老飯店でメシを食うんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xFE,
        (
            "食堂のメシもうまいけど、\x01",
            "あそこのメシも捨てがたいよね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26A0")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_7_1D80 end

    def Function_8_26A8(): pass

    label("Function_8_26A8")

    Call(0, 9)
    Return()

    # Function_8_26A8 end

    def Function_9_26AC(): pass

    label("Function_9_26AC")

    TalkBegin(0xB)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_26B9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3046")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",          # 0
            "買い物をする\x01",      # 1
            "やめる\x01",            # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2717")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_2717")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2737")
    OP_AF(0x6E)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3041")

    label("loc_2737")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_274B")
    Jump("loc_3041")

    label("loc_274B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3041")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2809")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x7)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2780")
    Call(0, 10)
    Jump("loc_2804")

    label("loc_2780")


    #C0097
    ChrTalk(
        0xB,
        (
            "昼を過ぎたら警備隊の人も\x01",
            "食べに来るから忙しくなるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0xB,
        (
            "よっと……まだお客も少ないし、\x01",
            "今のうちに仕込みを済ませておこう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2804")

    Jump("loc_3041")

    label("loc_2809")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_28BA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x7)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2825")
    Call(0, 10)
    Jump("loc_28B5")

    label("loc_2825")


    #C0099
    ChrTalk(
        0xB,
        (
            "最近たまに、うちに食べに来るために\x01",
            "タングラム門に来る人がいるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xB,
        (
            "また食べたいと思ってもらえるのは\x01",
            "料理人冥利に尽きるというものさ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28B5")

    Jump("loc_3041")

    label("loc_28BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2A72")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x7)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28D6")
    Call(0, 10)
    Jump("loc_2A6D")

    label("loc_28D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29F9")

    #C0101
    ChrTalk(
        0xB,
        (
            "おや、ノエル曹長……\x01",
            "これから任務に出かけるんだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x109,
        (
            "#0500Fええ。\x02\x03",

            "#0509Fティマスさん、せっかくなので\x01",
            "何か精のつくものを\x01",
            "ご馳走してくださいよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xB,
        (
            "はっはっは、いくら曹長の頼みでも\x01",
            "奢ることはできないな。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xB,
        (
            "何か食べていくなら\x01",
            "きっちりと、ミラを払ってもらうよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2A6D")

    label("loc_29F9")


    #C0105
    ChrTalk(
        0xB,
        (
            "いくら曹長の頼みでも\x01",
            "料理を奢るなんてできないね。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xB,
        (
            "精を付けたいなら\x01",
            "きちんとミラを払って食べていってくれ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A6D")

    Jump("loc_3041")

    label("loc_2A72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2AEE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x7)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A8E")
    Call(0, 10)
    Jump("loc_2AE9")

    label("loc_2A8E")


    #C0107
    ChrTalk(
        0xB,
        "今日は結構な頻度でお客さんが来るよ。\x02",
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0xB,
        (
            "一人で切り盛りするのは\x01",
            "やっぱ大変だなぁ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AE9")

    Jump("loc_3041")

    label("loc_2AEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2C49")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x7)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B0A")
    Call(0, 10)
    Jump("loc_2C44")

    label("loc_2B0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BF2")

    #C0109
    ChrTalk(
        0xB,
        (
            "ソーニャ副司令は、\x01",
            "昼休憩を他の隊員とずらして\x01",
            "一番最後に昼食をとるんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xB,
        (
            "一緒に食べて親睦を深めるよりも、\x01",
            "部下とはきちんと一線を引いてるのさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0xB,
        (
            "上官としてのあり方をよく分かっている\x01",
            "聡明なお方だよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2C44")

    label("loc_2BF2")


    #C0112
    ChrTalk(
        0xB,
        (
            "……なんでソーニャ副司令が\x01",
            "警備隊の司令じゃないのか……\x01",
            "不思議でならないよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C44")

    Jump("loc_3041")

    label("loc_2C49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2E0A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x7)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C65")
    Call(0, 10)
    Jump("loc_2E05")

    label("loc_2C65")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2D19")

    #C0113
    ChrTalk(
        0xB,
        (
            "実は、一般のお客に出すメニューと\x01",
            "警備隊員に出すメニューは違うんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xB,
        (
            "警備隊員には一日中\x01",
            "頑張ってもらわないといけないから\x01",
            "スタミナのつく料理が多いんだよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E05")

    label("loc_2D19")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_2DA6")

    #C0115
    ChrTalk(
        0xB,
        (
            "くぅ～……\x01",
            "昼時はやっぱり混むねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0xB,
        (
            "それに、共和国の人の口に合う\x01",
            "味付けをしないといけないから\x01",
            "なかなか大変だよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E05")

    label("loc_2DA6")


    #C0117
    ChrTalk(
        0xB,
        "今のうちに仕込みをしとかないとな。\x02",
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xB,
        (
            "共和国からのバスが着いたら\x01",
            "そりゃあ忙しくなるぞ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E05")

    Jump("loc_3041")

    label("loc_2E0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2EB7")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x7)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E26")
    Call(0, 10)
    Jump("loc_2EB2")

    label("loc_2E26")


    #C0119
    ChrTalk(
        0xB,
        (
            "列車以外にも、\x01",
            "徒歩でこっちに来る人も\x01",
            "それなりにいるみたいだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xB,
        (
            "まぁ、基本的に\x01",
            "共和国からは一本道だし……\x01",
            "分からなくはないかな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EB2")

    Jump("loc_3041")

    label("loc_2EB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2F49")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x7)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2ED3")
    Call(0, 10)
    Jump("loc_2F44")

    label("loc_2ED3")


    #C0121
    ChrTalk(
        0xB,
        (
            "タングラム門勤務になってから\x01",
            "はや一年……\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0xB,
        (
            "外国の人に\x01",
            "俺の料理を食べてもらえるのは\x01",
            "なかなかうれしいね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F44")

    Jump("loc_3041")

    label("loc_2F49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_3041")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FC9")

    #C0123
    ChrTalk(
        0xB,
        (
            "ここで足止め食っちまう旅行者の為に\x01",
            "一通りの施設は揃ってるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xB,
        "アンタも何か食べてくかい？\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3041")

    label("loc_2FC9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x7)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FDC")
    Call(0, 10)
    Jump("loc_3041")

    label("loc_2FDC")


    #C0125
    ChrTalk(
        0xB,
        (
            "ここで足止め食っちまう旅行者の為に\x01",
            "一通りの施設は揃ってるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0xB,
        "アンタも何か食べてくかい？\x02",
    )

    CloseMessageWindow()

    label("loc_3041")

    Jump("loc_26B9")

    label("loc_3046")

    TalkEnd(0xB)
    Return()

    # Function_9_26AC end

    def Function_10_304A(): pass

    label("Function_10_304A")


    #C0127
    ChrTalk(
        0xB,
        (
            "こないだ釣公師団だか\x01",
            "なんだかっていう人たちから\x01",
            "美味しい魚鍋のレシピを教わったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0xB,
        (
            "魚は体にいいからね。　\x01",
            "今度隊員さん達に振舞ってやろうかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xB,
        (
            "そうだ、君らにも教えてあげるよ。\x01",
            "みんなで楽しく食べてくれ。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0130
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1A3),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "のレシピを教えてもらった。\x02",
        )
    )

    CloseMessageWindow()

    #A0131
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1A3),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "のレシピを覚えた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    OP_B0(0x7)
    Return()

    # Function_10_304A end

    def Function_11_319C(): pass

    label("Function_11_319C")

    Call(0, 12)
    Return()

    # Function_11_319C end

    def Function_12_31A0(): pass

    label("Function_12_31A0")

    TalkBegin(0xC)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_31AD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3833")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",        # 0
            "休憩をする\x01",      # 1
            "やめる\x01",          # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3209")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_3209")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3229")
    OP_AF(0x6F)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_382E")

    label("loc_3229")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_323D")
    Jump("loc_382E")

    label("loc_323D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_382E")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_32D0")

    #C0132
    ChrTalk(
        0xC,
        (
            "このような早くから\x01",
            "宿に来るとは変わった奴だな。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xC,
        (
            "……まぁいい。\x01",
            "休んでいくなら好きにするがいいさ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_382E")

    label("loc_32D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_3439")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33C5")

    #C0134
    ChrTalk(
        0xC,
        (
            "ソーニャ副司令は\x01",
            "隊員に過度の負担をかけないよう\x01",
            "上手く仕事を配分しているようだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xC,
        (
            "いざというときに疲れていては\x01",
            "緊急度の高い事件に対応できないからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xC,
        (
            "お前たちも体調だけは\x01",
            "いつでも万全に整えておくんだな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3434")

    label("loc_33C5")


    #C0137
    ChrTalk(
        0xC,
        (
            "いつ何が起こっても対応できるよう、\x01",
            "休息はとれるときにとっておけ。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xC,
        "何ならこの施設で休んでも構わんぞ。\x02",
    )

    CloseMessageWindow()

    label("loc_3434")

    Jump("loc_382E")

    label("loc_3439")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_34F3")

    #C0139
    ChrTalk(
        0xC,
        (
            "何でも、化け物が出たとかで\x01",
            "タングラム門の警備隊員は\x01",
            "任務に尻込みしてしまっているらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xC,
        (
            "肝っ玉の小さい奴らだ。\x01",
            "化け物と言っても、魔獣なら\x01",
            "散々戦ってきたろうに。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_382E")

    label("loc_34F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_3556")

    #C0141
    ChrTalk(
        0xC,
        "……皆、忙しそうだな。\x02",
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xC,
        (
            "俺は暇だし、あとで\x01",
            "ティマスの方を手伝ってやるか……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_382E")

    label("loc_3556")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_35E7")

    #C0143
    ChrTalk(
        0xC,
        (
            "俺はイリア・プラティエの\x01",
            "大ファンなんだ……\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0xC,
        (
            "こんな所に勤務したばっかりに\x01",
            "アルカンシェルの公演を\x01",
            "見に行けないなんてな……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_382E")

    label("loc_35E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_36CB")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3674")

    #C0145
    ChrTalk(
        0xC,
        (
            "……休憩していくか？\x01",
            "意外に空いてるぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xC,
        (
            "記念祭だってのに、\x01",
            "こんな所に泊まるような\x01",
            "観光客はいないからな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36C6")

    label("loc_3674")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_36A4")

    #C0147
    ChrTalk(
        0xC,
        "……今日は客が多いな……\x02",
    )

    CloseMessageWindow()
    Jump("loc_36C6")

    label("loc_36A4")


    #C0148
    ChrTalk(
        0xC,
        "……なんだ、休んでいくのか？\x02",
    )

    CloseMessageWindow()

    label("loc_36C6")

    Jump("loc_382E")

    label("loc_36CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_372A")

    #C0149
    ChrTalk(
        0xC,
        (
            "《アルカンシェル》公演……\x01",
            "昨日が初日だったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xC,
        "……行きたかったな……\x02",
    )

    CloseMessageWindow()
    Jump("loc_382E")

    label("loc_372A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_37D4")

    #C0151
    ChrTalk(
        0xC,
        (
            "うちに泊まるのは\x01",
            "共和国からの旅行者や\x01",
            "貿易商くらいのもんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xC,
        (
            "たまにバスに乗り損なって\x01",
            "足止め食らうヤツもいるからな。\x01",
            "こういう施設は必要なんだよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_382E")

    label("loc_37D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_382E")

    #C0153
    ChrTalk(
        0xC,
        "……休憩していくのか？\x02",
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0xC,
        (
            "好きにすればいい。\x01",
            "……寝心地は保証しないがな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_382E")

    Jump("loc_31AD")

    label("loc_3833")

    TalkEnd(0xC)
    Return()

    # Function_12_31A0 end

    def Function_13_3837(): pass

    label("Function_13_3837")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_38CB")
    Jump("loc_3915")

    label("loc_38CB")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_38EB")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3915")

    label("loc_38EB")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_390B")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3915")

    label("loc_390B")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3915")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0155
    ChrTalk(
        0xFE,
        "もぐもぐむしゃむしゃ……\x02",
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xFE,
        (
            "今日はここでゆっくりして\x01",
            "明日の定期便で帰るかな。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_13_3837 end

    def Function_14_3997(): pass

    label("Function_14_3997")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3A2B")
    Jump("loc_3A75")

    label("loc_3A2B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3A4B")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3A75")

    label("loc_3A4B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3A6B")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3A75")

    label("loc_3A6B")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3A75")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0157
    ChrTalk(
        0xFE,
        (
            "早く終わらないかなー。\x01",
            "もぐもぐ……もう食べ終わっちゃうよ。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_14_3997 end

    def Function_15_3AE3(): pass

    label("Function_15_3AE3")

    TalkBegin(0xFE)

    #C0158
    ChrTalk(
        0xFE,
        (
            "ふーん、ここがタングラム門か……\x01",
            "思ったより守りは薄いんだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xFE,
        (
            "クロスベルが\x01",
            "共和国の手に落ちるのも\x01",
            "時間の問題だね。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_15_3AE3 end

    def Function_16_3B67(): pass

    label("Function_16_3B67")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3BFB")
    Jump("loc_3C45")

    label("loc_3BFB")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3C1B")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3C45")

    label("loc_3C1B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3C3B")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3C45")

    label("loc_3C3B")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3C45")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0160
    ChrTalk(
        0xFE,
        (
            "クロスベル市に向かうなら\x01",
            "導力バスを使うのがよさそうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xFE,
        (
            "バス乗り場は確か外……だったな。\x01",
            "腹ごしらえもしたし行ってみるか。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_16_3B67 end

    def Function_17_3CF8(): pass

    label("Function_17_3CF8")

    TalkBegin(0xFE)

    #C0162
    ChrTalk(
        0xFE,
        (
            "クロスベル市への\x01",
            "導力バスっていうのは\x01",
            "どこから出ているのかしら？\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_17_3CF8 end

    def Function_18_3D45(): pass

    label("Function_18_3D45")

    TalkBegin(0xFE)

    #C0163
    ChrTalk(
        0xFE,
        (
            "ふぃー、混まない日を選んでたら\x01",
            "すっかり出遅れちまった。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xFE,
        (
            "まぁ仕方ない。\x01",
            "さっさと街の方に\x01",
            "商品の買い付けに行くとするか！\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0xFE,
        (
            "実際、商売よりも\x01",
            "記念祭で遊ぶ方が楽しみなんだがね！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_18_3D45 end

    def Function_19_3E06(): pass

    label("Function_19_3E06")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3E9A")
    Jump("loc_3EE4")

    label("loc_3E9A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3EBA")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3EE4")

    label("loc_3EBA")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3EDA")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3EE4")

    label("loc_3EDA")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3EE4")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0166
    ChrTalk(
        0xFE,
        (
            "記念祭は明日までだけど……\x01",
            "絶対混むから今日帰ることにしたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0xFE,
        (
            "同じこと考える人は\x01",
            "結構いるみたいだけどね。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_19_3E06 end

    def Function_20_3F87(): pass

    label("Function_20_3F87")

    TalkBegin(0xFE)

    #C0168
    ChrTalk(
        0xFE,
        (
            "私は急いでるんだ！\x01",
            "ほら、早くしてくれたまえ！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_20_3F87 end

    def Function_21_3FC1(): pass

    label("Function_21_3FC1")

    TalkBegin(0xFE)

    #C0169
    ChrTalk(
        0xFE,
        "検分なんて面倒だなぁ……\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_21_3FC1 end

    def Function_22_3FE6(): pass

    label("Function_22_3FE6")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_407A")
    Jump("loc_40C4")

    label("loc_407A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_409A")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_40C4")

    label("loc_409A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_40BA")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_40C4")

    label("loc_40BA")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_40C4")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0170
    ChrTalk(
        0xFE,
        (
            "バスはまだ来んのかのう。\x01",
            "かれこれ１時間はまっとるんじゃが……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_22_3FE6 end

    def Function_23_4134(): pass

    label("Function_23_4134")

    TalkBegin(0xFE)

    #C0171
    ChrTalk(
        0xFE,
        "朝早く出発したものだから眠くってね。\x02",
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0xFE,
        (
            "居眠り運転するわけには行かないし\x01",
            "しばらくここで\x01",
            "眠気を覚ましていくかなぁ。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_23_4134 end

    def Function_24_41B5(): pass

    label("Function_24_41B5")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4249")
    Jump("loc_4293")

    label("loc_4249")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4269")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4293")

    label("loc_4269")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4289")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4293")

    label("loc_4289")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4293")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0173
    ChrTalk(
        0xFE,
        "うむ……意外と料理が本格的だな。\x02",
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0xFE,
        (
            "こういう食堂は安い代わりに\x01",
            "適当な料理が出るのがお約束だが……\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0xFE,
        "いい意味で裏切られたよ。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_24_41B5 end

    def Function_25_4347(): pass

    label("Function_25_4347")

    TalkBegin(0xFE)

    #C0176
    ChrTalk(
        0xFE,
        "うふふ、おいしいわね、あなた。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_25_4347 end

    def Function_26_4372(): pass

    label("Function_26_4372")

    TalkBegin(0xFE)

    #C0177
    ChrTalk(
        0xFE,
        "東方人街の特産物を売りに来たんだ。\x02",
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0xFE,
        (
            "東方系の小物なんかは\x01",
            "なかなか他所じゃ売ってないからね。\x01",
            "これは売れるぞォ～！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_26_4372 end

    def Function_27_43F3(): pass

    label("Function_27_43F3")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4487")
    Jump("loc_44D1")

    label("loc_4487")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_44A7")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_44D1")

    label("loc_44A7")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_44C7")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_44D1")

    label("loc_44C7")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_44D1")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_45B6")

    #C0179
    ChrTalk(
        0xFE,
        "パクパク……ムシャムシャ……\x02",
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0xFE,
        (
            "……さぁて、クロスベルに来たものの\x01",
            "まったくもってノープランじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0xFE,
        (
            "記念祭に行った友人が勧める\x01",
            "アルモリカ村にでも行ってみるかのう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_463F")

    label("loc_45B6")


    #C0182
    ChrTalk(
        0xFE,
        (
            "景色が素晴らしいそうだし……\x01",
            "アルモリカ村にでも行ってみるかのう。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0xFE,
        (
            "……いやいや、\x01",
            "鉱山見物というのも悪くないな。\x01",
            "ウムム…………\x02",
        )
    )

    CloseMessageWindow()

    label("loc_463F")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_27_43F3 end

    def Function_28_4647(): pass

    label("Function_28_4647")

    TalkBegin(0xFE)

    #C0184
    ChrTalk(
        0xFE,
        (
            "長期休暇で家内を連れて\x01",
            "クロスベル市を訪れていたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0xFE,
        (
            "異様な近代化を遂げたクロスベル市と\x01",
            "自然を大きく残すその他の地域……\x01",
            "なかなか見ものだったな。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_28_4647 end

    def Function_29_46EB(): pass

    label("Function_29_46EB")

    TalkBegin(0xFE)

    #C0186
    ChrTalk(
        0xFE,
        (
            "外見は華やかだけど、\x01",
            "少し裏通りを歩くだけで\x01",
            "闇の世界に迷い込んだ感覚……\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xFE,
        (
            "私はクロスベルには\x01",
            "一種の恐怖を感じましたわ。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_29_46EB end

    def Function_30_4773(): pass

    label("Function_30_4773")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4807")
    Jump("loc_4851")

    label("loc_4807")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4827")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4851")

    label("loc_4827")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4847")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4851")

    label("loc_4847")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4851")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0188
    ChrTalk(
        0xFE,
        "遅めの朝食としゃれ込むかね。\x02",
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0xFE,
        "さて、何を食べようか……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_30_4773 end

    def Function_31_48BE(): pass

    label("Function_31_48BE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_4933")

    #C0190
    ChrTalk(
        0x22,
        (
            "#3600F今日はこちらの食堂に\x01",
            "食材を卸しに来たんです。\x02\x03",

            "よし、もうひと仕事\x01",
            "頑張るとしましょうか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_49DF")

    label("loc_4933")


    #C0191
    ChrTalk(
        0x22,
        (
            "#3600F今日はこちらの食堂に\x01",
            "食材を卸しに来たんですよ。\x02\x03",

            "#3604Fさてと……あまりティマスさんを\x01",
            "お待たせしても悪いですし。\x02\x03",

            "早いところ運んでしまわないと\x01",
            "いけませんね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_49DF")

    TalkEnd(0xFE)
    Return()

    # Function_31_48BE end

    def Function_32_49E3(): pass

    label("Function_32_49E3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A66")

    #C0192
    ChrTalk(
        0xFE,
        "ここの宿、意外といいベッドだね。\x02",
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0xFE,
        (
            "今まで数々の宿に泊まった\x01",
            "わたしが言うんだもの。\x01",
            "……間違いないよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_4A8F")

    label("loc_4A66")


    #C0194
    ChrTalk(
        0xFE,
        (
            "無骨なわりに\x01",
            "ふかふかなベッドだ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A8F")

    TalkEnd(0xFE)
    Return()

    # Function_32_49E3 end

    def Function_33_4A93(): pass

    label("Function_33_4A93")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4B27")
    Jump("loc_4B71")

    label("loc_4B27")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4B47")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4B71")

    label("loc_4B47")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4B67")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4B71")

    label("loc_4B67")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4B71")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_4DF0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D83")

    #C0195
    ChrTalk(
        0x24,
        (
            "今日は共和国帰りの観光客からの\x01",
            "依頼で来ていてな。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x24,
        (
            "ゲートを抜けた先の\x01",
            "《タングラム丘陵》に落した財布を\x01",
            "さっき回収したんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0x101,
        (
            "#0005F……えっと、\x01",
            "それだけですか？\x02\x03",

            "なんだか随分と\x01",
            "楽な仕事に聞こえますが……\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x25,
        "……ところが、そうでもない。\x02",
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0x25,
        (
            "《タングラム丘陵》の一帯は\x01",
            "共和国が領土を主張していてな。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0x25,
        (
            "落し物を拾うという目的だけでも、\x01",
            "面倒な許可申請が必要になるのだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0x103,
        "#0200F結構厳しいんですね。\x02",
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x24,
        (
            "ま、楽な仕事なんか\x01",
            "そうそうないってことさ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_4DF0")

    label("loc_4D83")


    #C0203
    ChrTalk(
        0xFE,
        (
            "この仕事に結構時間を\x01",
            "とられたからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0xFE,
        (
            "他の仕事も押してるし、\x01",
            "早いとこクロスベル市に\x01",
            "戻らないとな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4DF0")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_33_4A93 end

    def Function_34_4DF8(): pass

    label("Function_34_4DF8")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4E8C")
    Jump("loc_4ED6")

    label("loc_4E8C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4EAC")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4ED6")

    label("loc_4EAC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4ECC")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4ED6")

    label("loc_4ECC")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4ED6")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_4F66")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F16")
    Call(0, 33)
    Jump("loc_4F66")

    label("loc_4F16")


    #C0205
    ChrTalk(
        0xFE,
        (
            "領土問題に関しては\x01",
            "帝国も共和国も威圧的だ。\x01",
            "……警察なら覚えておく事だな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F66")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_34_4DF8 end

    def Function_35_4F6E(): pass

    label("Function_35_4F6E")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5002")
    Jump("loc_504C")

    label("loc_5002")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5022")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_504C")

    label("loc_5022")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5042")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_504C")

    label("loc_5042")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_504C")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_52C2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_51C5")

    #C0206
    ChrTalk(
        0xFE,
        "今から共和国のギルドに出張さ。\x02",
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0xFE,
        (
            "うんうん、故郷での\x01",
            "仕事となると腕が鳴るね。\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0xFE,
        (
            "イキのいい後輩が\x01",
            "入ってると面白いんだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0x101,
        (
            "#0009Fはは……リンさんって\x01",
            "後輩にも容赦しなさそうですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0xFE,
        (
            "もちろん。\x01",
            "遊びでやってるんじゃ\x01",
            "ないんだしね。\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0xFE,
        (
            "私も武術の修行中は、\x01",
            "偉大な先輩方に\x01",
            "厳しくされたものだよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_52C2")

    label("loc_51C5")


    #C0212
    ChrTalk(
        0xFE,
        (
            "目的のギルドがちょっと\x01",
            "入り組んだ所にあってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0xFE,
        (
            "列車だと乗り継ぎが必要だけど、\x01",
            "導力バスなら一本で行ってくれる場所だから\x01",
            "むしろこっちの方が早く到着するんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0xFE,
        (
            "時にはバスの“早さ”が\x01",
            "列車の“速さ”を凌駕することもある。\x01",
            "覚えておくといいよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_52C2")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_35_4F6E end

    def Function_36_52CA(): pass

    label("Function_36_52CA")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_535E")
    Jump("loc_53A8")

    label("loc_535E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_537E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_53A8")

    label("loc_537E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_539E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_53A8")

    label("loc_539E")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_53A8")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_556A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_54F7")

    #C0215
    ChrTalk(
        0xFE,
        (
            "リンは共和国の古武術、\x01",
            "《泰斗流》の流れを汲む\x01",
            "武術の使い手なの。\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0xFE,
        (
            "素手での格闘術なら、\x01",
            "クロスベルのギルドでも\x01",
            "１、２を争う腕前なのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0x104,
        (
            "#0305F共和国の高位遊撃士が\x01",
            "そんな名前の武術を操るって\x01",
            "聞いたことがあるな。\x02\x03",

            "#0304F道理で立ち振る舞いに\x01",
            "隙がねぇわけだぜ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_556A")

    label("loc_54F7")


    #C0218
    ChrTalk(
        0xFE,
        (
            "リンったら、\x01",
            "共和国での仕事だから\x01",
            "張り切っているのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0xFE,
        (
            "ふふっ、あんまり厳しいと\x01",
            "怖がられちゃうわよねぇ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_556A")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_36_52CA end

    def Function_37_5572(): pass

    label("Function_37_5572")

    TalkBegin(0xFE)

    #C0220
    ChrTalk(
        0x29,
        (
            "#0500Fクロスベル行きのバスは、\x01",
            "門を出てすぐの駐車場です。\x02\x03",

            "#0501F私はここまでしか手伝えませんが……\x01",
            "みなさん、健闘を祈ります！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_37_5572 end

    def Function_38_55FD(): pass

    label("Function_38_55FD")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5691")
    Jump("loc_56DB")

    label("loc_5691")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_56B1")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_56DB")

    label("loc_56B1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_56D1")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_56DB")

    label("loc_56D1")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_56DB")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0x5)"), scpexpr(EXPR_END)), "loc_57F1")

    #C0221
    ChrTalk(
        0x2A,
        (
            "#3404Fクロスベルに来たのは……\x01",
            "強いて言うなら宝石を捜しに、\x01",
            "と言った所ね。\x02\x03",

            "#3400Fそれを手に入れさえすれば、\x01",
            "共和国の民を熱狂の渦に\x01",
            "巻き込むほどの力を持つわ。\x02\x03",

            "#3402Fただし、あらゆる手を尽くす\x01",
            "必要があるけれど……ね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5B08")

    label("loc_57F1")


    #C0222
    ChrTalk(
        0x104,
        "#0305F（おお……美人がいる……！）\x02",
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0x2A,
        (
            "#3405F……あら。\x02\x03",

            "#3400Fあなた達、\x01",
            "バスに乗っていた人ではないわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0x101,
        (
            "#0005F……えっ！？\x02\x03",

            "#0012Fえ、えっと……\x01",
            "昨日夜遅くに着いたので、\x01",
            "ここの宿泊施設に一泊していたんです。\x02\x03",

            "#0006F（と、いうことにしておこう……）\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x2A,
        (
            "#3404Fフフ……そう。\x02\x03",

            "#3400Fまぁ、よくよく考えれば\x01",
            "大して不思議なことでも\x01",
            "なかったわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0x104,
        (
            "#0309Fお姉さんは、クロスベルに\x01",
            "何しに来たんッスか？\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0x2A,
        (
            "#3404F強いて言うなら……\x01",
            "宝石を捜しに、と言ったところかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0x101,
        "#0005F宝石……？\x02",
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0x2A,
        (
            "#3400Fそう、クロスベルの地に眠る、\x01",
            "魔性の宝石を捜しにね。\x02\x03",

            "#3404Fそれを手に入れさえすれば、\x01",
            "共和国の民を熱狂の渦に\x01",
            "巻き込むほどの力を持つわ。\x02\x03",

            "#3402Fただし、あらゆる手を尽くす\x01",
            "必要があるけれど……ね。\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0x101,
        "#0005F（……この人……？）\x02",
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0x2A,
        "#3404Fフフ、あまり深く考えないでいいわ。\x02",
    )

    CloseMessageWindow()
    OP_29(0x1B, 0x1, 0x5)

    label("loc_5B08")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_38_55FD end

    def Function_39_5B10(): pass

    label("Function_39_5B10")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5BA4")
    Jump("loc_5BEE")

    label("loc_5BA4")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5BC4")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5BEE")

    label("loc_5BC4")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5BE4")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5BEE")

    label("loc_5BE4")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5BEE")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0x6)"), scpexpr(EXPR_END)), "loc_5CE5")

    #C0232
    ChrTalk(
        0xFE,
        (
            "クロスベルに来たのは\x01",
            "３年ぶりになるかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0xFE,
        (
            "おほほ、孫に会えるのが\x01",
            "楽しみでならないわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0xFE,
        (
            "まだまだ小さい孫とミシュラムの\x01",
            "テーマパークで遊んだ事、\x01",
            "昨日のことのように思い出すわ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5F3B")

    label("loc_5CE5")


    #C0235
    ChrTalk(
        0xFE,
        (
            "おやおや……\x01",
            "かわいらしい坊やねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0xFE,
        (
            "私の孫にそっくりで、\x01",
            "頭のよさそうな顔をしているわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0x101,
        (
            "#0000Fえっと……お婆さんは、\x01",
            "クロスベルの人？\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0xFE,
        "いえいえ、私は共和国人よ。\x02",
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0xFE,
        (
            "息子夫婦がクロスベル市で\x01",
            "暮らしているから、\x01",
            "記念祭を理由に遊びに来たの。\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0xFE,
        (
            "クロスベルに来るのは\x01",
            "３年ぶりになるかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x102,
        (
            "#0102Fうふふ……\x01",
            "嬉しそうですね、お婆さん。\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0xFE,
        "おほほ……それはもう。\x02",
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0xFE,
        (
            "なにせ、孫と会えるのも\x01",
            "久しぶりですからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0xFE,
        (
            "前に来た時に、孫とミシュラムの\x01",
            "テーマパークで遊んだこと……\x01",
            "まるで昨日のことのようだわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0xFE,
        (
            "あれからどれだけ\x01",
            "大きくなったやら……\x01",
            "楽しみでならないの。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x1B, 0x1, 0x6)

    label("loc_5F3B")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_39_5B10 end

    def Function_40_5F43(): pass

    label("Function_40_5F43")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0x7)"), scpexpr(EXPR_END)), "loc_5FCB")

    #C0246
    ChrTalk(
        0xFE,
        (
            "……わしがこの\x01",
            "クロスベルに来たのは\x01",
            "釣りの為じゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0xFE,
        (
            "他の理由では断じてない。\x01",
            "……分かったらさっさと行け。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6334")

    label("loc_5FCB")


    #C0248
    ChrTalk(
        0xFE,
        "……なんだね。\x02",
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x101,
        (
            "#0006F（偏屈そうなおじいさんだな……）\x02\x03",

            "#0000Fえ、え～っと……\x01",
            "おじいさんは、クロスベルに何をしに？\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0xFE,
        "……なぜ、そんなことを聞く必要がある。\x02",
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x101,
        (
            "#0006Fい、いやその……\x01",
            "単に好奇心というか……\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0x104,
        (
            "#0300Fなんだ爺さん、人に言えないほど\x01",
            "やましいことでもしに来たのかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0xFE,
        "な、なんじゃと……！\x02",
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0x101,
        "#0005Fちょ……ランディ！？\x02",
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x104,
        (
            "#0304F実を言うと俺もそのクチでねぇ。\x02\x03",

            "#0300Fクロスベルは可愛い子がわんさか、\x01",
            "女の子いっぱいの楽しいお店もどっさりな\x01",
            "良いとこだもんな？\x02\x03",

            "#0309Fいや～、爺さん気が合う！\x01",
            "何なら俺にお気に入りの店を\x01",
            "教えてくれよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0xFE,
        (
            "だ、だ、誰がそんな破廉恥な\x01",
            "店などにいくかっ！！\x02",
        )
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0xFE,
        "……釣りじゃ、釣りッ！！\x02",
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0xFE,
        (
            "クロスベルの淡水魚を釣るために、\x01",
            "記念祭だというのに\x01",
            "１人寂しく来たんじゃ！！\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0xFE,
        "悪いか小僧！！\x02",
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0x104,
        (
            "#0309F……はは、悪くねぇよ。\x01",
            "からかって悪かったな、爺さん。\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0x101,
        "#0006F（悪知恵が働くなぁ……）\x02",
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0xFE,
        "フンッ！\x02",
    )

    CloseMessageWindow()
    OP_29(0x1B, 0x1, 0x7)

    label("loc_6334")

    TalkEnd(0xFE)
    Return()

    # Function_40_5F43 end

    def Function_41_6338(): pass

    label("Function_41_6338")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_63F2")

    #C0263
    ChrTalk(
        0xFE,
        (
            "私は共和国の珍しい雑貨などを\x01",
            "売り歩いているんですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0xFE,
        (
            "各国に知り合いがいるので\x01",
            "商談も意外とスムーズに進むんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0xFE,
        (
            "よければ皆様も\x01",
            "ひとつ、ごひいきに。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6616")

    label("loc_63F2")


    #C0266
    ChrTalk(
        0xFE,
        (
            "いやっはっはっは。\x01",
            "バスの到着が待ち遠しいですな。\x02",
        )
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0xFE,
        (
            "クロスベルは景気のいいところと\x01",
            "聞きますし、今から楽しみですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0x101,
        (
            "#0005F……へぇ、なにか\x01",
            "ご商売をされているんですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0xFE,
        (
            "ええ、共和国の珍しい雑貨などを\x01",
            "売り歩いているんですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0xFE,
        (
            "ついでに、クロスベルならではの\x01",
            "雑貨を仕入れて、\x01",
            "また共和国で売りたいな、と。\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0x103,
        (
            "#0205F個人の貿易商ですか……\x01",
            "なかなか大変なのでは？\x02",
        )
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0xFE,
        (
            "いえいえ、これでも人脈は\x01",
            "なかなか広い方ですから。\x02",
        )
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0xFE,
        (
            "各国に知り合いがいるので\x01",
            "商談も意外とスムーズに進むんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0xFE,
        (
            "よければ皆様も\x01",
            "ひとつ、ごひいきに。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x1B, 0x1, 0x8)

    label("loc_6616")

    TalkEnd(0xFE)
    Return()

    # Function_41_6338 end

    def Function_42_661A(): pass

    label("Function_42_661A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0x9)"), scpexpr(EXPR_END)), "loc_66EF")

    #C0275
    ChrTalk(
        0xFE,
        (
            "今まで共和国に旅行に行ってて、\x01",
            "記念祭にあわせて帰ってきたの。\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0xFE,
        (
            "でも、私のことなんて\x01",
            "どーでもいいじゃない？\x02",
        )
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0xFE,
        (
            "あなたもバスに乗るなら、\x01",
            "あの黒髪の女の人は\x01",
            "気を付けたほうがいいわよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6A08")

    label("loc_66EF")


    #C0278
    ChrTalk(
        0xFE,
        (
            "ねぇねぇ……あのお姉さん、\x01",
            "ヘンだと思わない？\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0x101,
        (
            "#0005Fえ……？\x01",
            "あのお姉さん、というと？\x02",
        )
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0xFE,
        (
            "ほら、向こうに座ってる\x01",
            "黒髪のパンツルックの人。\x02",
        )
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0xFE,
        (
            "旅客バスの中でも見てたけどさぁ、\x01",
            "なんだかちょっと\x01",
            "怪しい感じがするのよねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0xFE,
        (
            "妙に落ち着き払ってるっていうか、\x01",
            "只者じゃない感じがするもの。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0x5)"), scpexpr(EXPR_END)), "loc_68A0")

    #C0283
    ChrTalk(
        0x102,
        (
            "#0103Fううん……確かに、\x01",
            "普通の人には\x01",
            "見えなかったけれど。\x02\x03",

            "#0100F……ところで、\x01",
            "あなたはクロスベルには観光で？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6915")

    label("loc_68A0")


    #C0284
    ChrTalk(
        0x102,
        (
            "#0103Fううん……ちょっと\x01",
            "話してみないと\x01",
            "分からないけれど。\x02\x03",

            "#0100F……ところで、\x01",
            "あなたはクロスベルには観光で？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6915")


    #C0285
    ChrTalk(
        0xFE,
        (
            "ん、どっちかっていうと\x01",
            "里帰りかなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0xFE,
        (
            "今まで共和国に旅行に行ってて、\x01",
            "記念祭にあわせて帰ってきたワケ。\x02",
        )
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0xFE,
        (
            "……って私のことなんて\x01",
            "どーでもいいじゃない？\x02",
        )
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0xFE,
        (
            "あなたもバスに乗るなら、\x01",
            "あの人は気を付けたほうが\x01",
            "いいわよ、きっと。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x1B, 0x1, 0x9)

    label("loc_6A08")

    TalkEnd(0xFE)
    Return()

    # Function_42_661A end

    def Function_43_6A0C(): pass

    label("Function_43_6A0C")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6AA0")
    Jump("loc_6AEA")

    label("loc_6AA0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6AC0")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6AEA")

    label("loc_6AC0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6AE0")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6AEA")

    label("loc_6AE0")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6AEA")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0xA)"), scpexpr(EXPR_END)), "loc_6B87")

    #C0289
    ChrTalk(
        0xFE,
        (
            "僕たちは兄妹なんだ。\x01",
            "あまり似てないだろ？\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0xFE,
        (
            "揃って旅行好きで、\x01",
            "よく２人で遊びに出かけるのさ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6E44")

    label("loc_6B87")


    #C0291
    ChrTalk(
        0x2F,
        (
            "やぁ、こんにちは。\x01",
            "君たちもクロスベル市に\x01",
            "向かうところかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0x101,
        (
            "#0000Fええ、まあそんなところです。\x02\x03",

            "#0005Fあなた方は、その……\x01",
            "カップルで旅行ですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0x2F,
        (
            "……ぷっ。\x01",
            "やっぱりそう見えるかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0x103,
        "#0205F？　ちがうんですか？\x02",
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0x30,
        (
            "……アハハ、やあねぇ。\x01",
            "ちがうちがう。\x02",
        )
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0x30,
        "私たち、こう見えても兄妹なのよ。\x02",
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0x2F,
        (
            "全然似てないから\x01",
            "よく間違われるんだけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0x2F,
        (
            "揃って旅行好きで、\x01",
            "よく２人で遊びに出かけるのさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0x101,
        "#0000Fへぇ……仲がいいんですね。\x02",
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0x2F,
        (
            "まぁ、彼氏のいない妹のために\x01",
            "僕が一肌脱いでやってるわけさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0x30,
        (
            "まーっ、よく言うわよ。\x01",
            "兄さんだってお母さんによく\x01",
            "彼女を作れって言われてるじゃない。\x02",
        )
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0x2F,
        "はは……ま、そういうわけなんだ。\x02",
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0x2F,
        (
            "お互い、記念祭を\x01",
            "大いに楽しもうじゃないか。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x1B, 0x1, 0xA)

    label("loc_6E44")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_43_6A0C end

    def Function_44_6E4C(): pass

    label("Function_44_6E4C")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6EE0")
    Jump("loc_6F2A")

    label("loc_6EE0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6F00")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6F2A")

    label("loc_6F00")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6F20")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6F2A")

    label("loc_6F20")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6F2A")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0xA)"), scpexpr(EXPR_END)), "loc_6FBF")

    #C0304
    ChrTalk(
        0xFE,
        (
            "カップルに間違われたの、\x01",
            "これで何回目かしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0xFE,
        (
            "ま、お互い記念祭を\x01",
            "楽しみましょうよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6FC2")

    label("loc_6FBF")

    Call(0, 43)

    label("loc_6FC2")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_44_6E4C end

    def Function_45_6FCA(): pass

    label("Function_45_6FCA")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_705E")
    Jump("loc_70A8")

    label("loc_705E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_707E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_70A8")

    label("loc_707E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_709E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_70A8")

    label("loc_709E")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_70A8")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0xB)"), scpexpr(EXPR_END)), "loc_7174")

    #C0306
    ChrTalk(
        0xFE,
        "今日は、家族旅行なんだ。\x02",
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0xFE,
        (
            "普段から出張しがちだから、\x01",
            "こういう所で父親らしいところを\x01",
            "見せたい……\x02",
        )
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0xFE,
        (
            "ただそれだけのことだよ。\x01",
            "わっはっは。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7301")

    label("loc_7174")


    #C0309
    ChrTalk(
        0xFE,
        (
            "バスでの旅というのも\x01",
            "なかなか乙なものだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0xFE,
        "子供も喜んでくれたようだ。\x02",
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0x101,
        "#0000F今日は、家族旅行で？\x02",
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0xFE,
        "ああ、そういうことだ。\x02",
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0xFE,
        (
            "日頃支えてくれる息子に\x01",
            "是非とも楽しんでもらいたくてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0x102,
        "#0102Fふふ……いいお父さんですね。\x02",
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0xFE,
        "いや、照れるなお嬢さん。\x02",
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0xFE,
        (
            "普段から出張しがちだから、\x01",
            "こういう所で父親らしいところを\x01",
            "見せたい……\x02",
        )
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0xFE,
        (
            "ただそれだけのことだよ。\x01",
            "わっはっは。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x1B, 0x1, 0xB)

    label("loc_7301")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_45_6FCA end

    def Function_46_7309(): pass

    label("Function_46_7309")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_739D")
    Jump("loc_73E7")

    label("loc_739D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_73BD")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_73E7")

    label("loc_73BD")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_73DD")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_73E7")

    label("loc_73DD")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_73E7")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0xC)"), scpexpr(EXPR_END)), "loc_7470")

    #C0318
    ChrTalk(
        0xFE,
        (
            "お父さんは出張で\x01",
            "たくさんの国に行ってるから、\x01",
            "色々教えてくれて楽しいんだぁ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7507")

    label("loc_7470")


    #C0319
    ChrTalk(
        0xFE,
        (
            "クロスベルって景色がいいんだね。\x01",
            "すっごく気持ちよかった。\x02",
        )
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0xFE,
        (
            "お父さんは出張で\x01",
            "たくさんの国に行ってるから、\x01",
            "色々教えてくれて楽しいんだぁ。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x1B, 0x1, 0xC)

    label("loc_7507")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_46_7309 end

    def Function_47_750F(): pass

    label("Function_47_750F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(22280, 1000, 1150, 0)
    MoveCamera(359, 27, 0, 0)
    OP_6E(470, 0)
    SetCameraDistance(20000, 0)
    OP_4B(0x29, 0xFF)
    ClearMapObjFlags(0x1, 0x10)
    SetChrPos(0x101, -7150, 0, 9500, 90)
    SetChrPos(0x102, -7150, 0, 8000, 90)
    SetChrPos(0x103, -8650, 0, 9500, 90)
    SetChrPos(0x104, -8650, 0, 8000, 90)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x2A, -40, 600, 0, 180)
    SetChrPos(0x2B, -40, 600, 0, 180)
    SetChrPos(0x2C, -40, 600, 0, 180)
    SetChrPos(0x2D, -40, 600, 0, 180)
    SetChrPos(0x2E, -40, 600, 0, 180)
    SetChrPos(0x2F, -40, 600, 0, 180)
    SetChrPos(0x30, -40, 600, 0, 180)
    SetChrPos(0x31, -40, 600, 0, 180)
    SetChrPos(0x32, -40, 600, 0, 180)
    SetChrFlags(0x2C, 0x40)
    SetChrFlags(0x2D, 0x40)
    SetChrFlags(0x2E, 0x40)
    ClearChrFlags(0x2A, 0x80)
    ClearChrFlags(0x2B, 0x80)
    ClearChrFlags(0x2C, 0x80)
    ClearChrFlags(0x2D, 0x80)
    ClearChrFlags(0x2E, 0x80)
    ClearChrFlags(0x2F, 0x80)
    ClearChrFlags(0x30, 0x80)
    ClearChrFlags(0x31, 0x80)
    ClearChrFlags(0x32, 0x80)
    OP_A7(0x2A, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x2B, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x2C, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x2D, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x2E, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x2F, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x30, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x31, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x32, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x33, 0x80)
    ClearMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0x9, 0x1000)
    OP_78(0x9, 0x33)
    OP_D3(0x33, 0x0, 0x41EB0, 0x0, 0x0)
    SetMapObjFrame(0x9, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0x33, 33000, 0, 0, 0)
    OP_70(0x9, 0x0)
    OP_74(0x9, 0x1E)
    Sound(466, 0, 100, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_68(16030, 1000, 3510, 3000)
    MoveCamera(21, 27, 0, 3000)
    OP_6E(470, 3000)
    SetCameraDistance(28000, 3000)
    OP_71(0x9, 0x79, 0xB4, 0x0, 0x20)

    def lambda_7799():
        OP_98(0xFE, 0xFFFFD120, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_7799)
    WaitChrThread(0x33, 1)
    OP_71(0x9, 0x5B, 0x78, 0x0, 0x0)
    OP_79(0x9)
    Sleep(500)
    OP_71(0x7, 0x0, 0x8C, 0x0, 0x0)
    Sleep(300)
    Sound(143, 0, 100, 0)
    Sleep(200)
    Sound(145, 0, 100, 0)
    OP_79(0x7)
    OP_71(0x9, 0x3C, 0x5A, 0x0, 0x0)
    Sound(473, 0, 100, 0)
    OP_79(0x9)
    OP_68(450, 1000, -1190, 6000)
    MoveCamera(115, 37, 0, 8000)
    SetCameraDistance(20000, 6000)
    OP_71(0x9, 0x79, 0xB4, 0x0, 0x20)

    def lambda_7830():
        OP_98(0xFE, 0xFFFFADF8, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_7830)
    WaitChrThread(0x33, 1)
    OP_71(0x9, 0x5B, 0x78, 0x0, 0x0)
    OP_79(0x9)
    OP_6F(0x79)
    Fade(1000)
    OP_68(210, 1000, -2670, 0)
    MoveCamera(82, 21, 0, 0)
    OP_6E(470, 0)
    SetCameraDistance(18190, 0)
    OP_0D()
    OP_71(0x9, 0x0, 0x1E, 0x0, 0x0)
    Sound(464, 0, 100, 0)
    OP_79(0x9)

    def lambda_78A8():
        OP_95(0x2D, -60, 0, -3600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_78A8)

    def lambda_78C2():
        OP_A7(0x2D, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2D, 2, lambda_78C2)
    WaitChrThread(0x2D, 1)
    WaitChrThread(0x2D, 2)

    #C0321
    ChrTalk(
        0x29,
        (
            "#0503Fクロスベル自治州へ\x01",
            "ようこそいらっしゃいました。\x01",
            "長旅お疲れ様です。\x02\x03",

            "#0500Fクロスベル市行きのバスの到着まで\x01",
            "少しばかり時間をいただいています。\x02\x03",

            "よろしければ食堂の方で\x01",
            "休憩なさってください。\x02",
        )
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0x2D,
        "#5Pああ、そうさせてもらおうか。\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x29, 3, 0, 52)

    def lambda_79CE():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2D, 2, lambda_79CE)
    Sleep(750)
    Fade(1000)
    OP_68(-420, 1000, 4100, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(470, 0)
    SetCameraDistance(24500, 0)
    BeginChrThread(0x2D, 3, 0, 54)
    BeginChrThread(0x31, 3, 0, 53)
    Sleep(750)
    BeginChrThread(0x32, 3, 0, 53)
    Sleep(750)
    BeginChrThread(0x2C, 3, 0, 53)
    Sleep(750)
    BeginChrThread(0x2B, 3, 0, 53)
    Sleep(750)
    BeginChrThread(0x2E, 3, 0, 53)
    Sleep(750)
    BeginChrThread(0x2F, 3, 0, 53)
    Sleep(750)
    BeginChrThread(0x30, 3, 0, 53)
    Sleep(750)
    BeginChrThread(0x2A, 3, 0, 55)
    Sleep(750)
    Sleep(5000)
    FadeToDark(500, 0, -1)
    OP_0D()
    WaitChrThread(0x29, 3)
    WaitChrThread(0x2A, 3)
    OP_68(580, 1000, 8990, 0)
    MoveCamera(38, 21, 0, 0)
    OP_6E(470, 0)
    SetCameraDistance(15260, 0)
    OP_70(0x1, 0x0)
    OP_71(0x1, 0x0, 0x5, 0x0, 0x0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrFlags(0x2D, 0x80)
    SetChrFlags(0x31, 0x80)
    SetChrFlags(0x32, 0x80)
    SetChrFlags(0x2C, 0x80)
    SetChrFlags(0x2B, 0x80)
    SetChrFlags(0x2E, 0x80)
    SetChrFlags(0x2F, 0x80)
    SetChrFlags(0x30, 0x80)
    SetChrFlags(0x33, 0x80)
    SetMapObjFlags(0x9, 0x4)
    SetChrPos(0x29, 1630, 0, 8660, 270)
    SetChrPos(0x2A, 440, 0, 8900, 270)

    def lambda_7B34():
        OP_95(0xFE, 0, 0, 13900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_7B34)
    FadeToBright(500, 0)
    OP_0D()

    def lambda_7B58():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x5DC)
        ExitThread()

    QueueWorkItem(0x2A, 2, lambda_7B58)
    WaitChrThread(0x2A, 1)
    WaitChrThread(0x2A, 2)
    OP_71(0x1, 0x5, 0x0, 0x0, 0x0)
    Sound(106, 0, 100, 0)
    OP_79(0x1)
    OP_63(0x29, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x29)

    #C0323
    ChrTalk(
        0x104,
        "#0301F……今ので乗客は全員か？\x02",
    )

    CloseMessageWindow()
    OP_68(-370, 1000, 9430, 2000)
    MoveCamera(29, 21, 0, 2000)
    OP_6E(470, 2000)
    SetCameraDistance(18150, 2000)
    BeginChrThread(0x101, 3, 0, 48)
    BeginChrThread(0x102, 3, 0, 49)
    BeginChrThread(0x103, 2, 0, 50)
    BeginChrThread(0x104, 2, 0, 51)
    Sleep(1000)

    def lambda_7C0B():
        OP_98(0xFE, 0xFFFFFC18, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_7C0B)
    WaitChrThread(0x29, 1)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)

    #C0324
    ChrTalk(
        0x29,
        (
            "#11P#0501Fええ、今ので全員です。\x02\x03",

            "こちらが乗客のリストになりますので、\x01",
            "目を通してみてください。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7C9E():
        OP_98(0xFE, 0xFFFFFC18, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_7C9E)
    WaitChrThread(0x29, 1)
    SetChrName("")

    #A0325
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ノエルから乗客リストを見せてもらった。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0326
    ChrTalk(
        0x101,
        (
            "#5P#0000Fああ、ありがとう。\x01",
            "助かるよ。\x02\x03",

            "#0003F乗客は全部で９人か……\x01",
            "全員が共和国から来たってことは\x01",
            "間違いなさそうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0x103,
        (
            "#0200F……このようなもの、\x01",
            "部外者に見せてもいいのですか？\x02\x03",

            "言ってみれば、個人情報の漏えいに\x01",
            "あたるのでは……\x02",
        )
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0x29,
        (
            "#11P#0500Fソーニャ副司令に、\x01",
            "捜査の役に立ちそうな情報は\x01",
            "出来るだけ渡すようにと言われてるの。\x02\x03",

            "#0503F『名前や住所が分かるわけ\x01",
            "  じゃないから、情報漏えいなんて\x01",
            "  大したモノじゃないわ』って。\x02",
        )
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0x102,
        (
            "#6P#0104F現場での柔軟な判断……\x01",
            "さすがは副司令ね。\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0x104,
        (
            "#6P#0306Fかーっ……なんつうか、\x01",
            "ホント恐ろしいお人だぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0x101,
        (
            "#5P#0003F……うん、ありがとう曹長。\x01",
            "このリストは返すよ。\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0332
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ノエルに乗客リストを返した。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    def lambda_7F7E():
        OP_98(0xFE, 0x3E8, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_7F7E)
    WaitChrThread(0x29, 1)

    #C0333
    ChrTalk(
        0x29,
        (
            "#11P#0503Fはい、確かに。\x02\x03",

            "#0501Fそれで……どうでした？\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0x101,
        (
            "#5P#0003Fうーん……やっぱり最終的な判断は\x01",
            "自分たちの目で見て下す必要がありそうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0x102,
        (
            "#6P#0101F……だったら、善は急げね。\x02\x03",

            "クロスベル行きのバスが来るまで\x01",
            "そこまで時間はないわ。\x02\x03",

            "食堂の中にいる乗客から話を聞き出して、\x01",
            "偽ブランド業者を見つけ出しましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0x101,
        "#5P#0001Fああ……やるぞ、皆！\x02",
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0x104,
        "#6P#0300Fあいよ！\x02",
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0x103,
        "#6P#0200F合点承知です。\x02",
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0x29,
        "#11P#0501F皆さん……健闘をお祈りします！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(95990, 750, -6440, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(27500, 0)
    SetMapObjFlags(0x1, 0x10)
    OP_70(0x7, 0x0)
    ModifyEventFlags(1, 0, 0x80)
    ModifyEventFlags(1, 1, 0x80)
    SetChrPos(0x0, 95990, 0, -6440, 0)
    SetChrPos(0x1, 95990, 0, -6440, 0)
    SetChrPos(0x2, 95990, 0, -6440, 0)
    SetChrPos(0x3, 95990, 0, -6440, 0)
    ClearChrFlags(0x2B, 0x40)
    ClearChrFlags(0x2D, 0x40)
    ClearChrFlags(0x2E, 0x40)
    OP_A7(0x2A, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_70(0x7, 0x0)
    Call(0, 56)
    OP_29(0x1B, 0x1, 0x4)
    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    EventEnd(0x6)
    Return()

    # Function_47_750F end

    def Function_48_8227(): pass

    label("Function_48_8227")


    def lambda_822C():
        OP_95(0xFE, -1500, 0, 9500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_822C)
    WaitChrThread(0x101, 1)
    Return()

    # Function_48_8227 end

    def Function_49_8246(): pass

    label("Function_49_8246")


    def lambda_824B():
        OP_95(0xFE, -1500, 0, 8000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_824B)
    WaitChrThread(0x102, 1)
    Return()

    # Function_49_8246 end

    def Function_50_8265(): pass

    label("Function_50_8265")


    def lambda_826A():
        OP_95(0xFE, -3000, 0, 9500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_826A)
    WaitChrThread(0x103, 1)
    Return()

    # Function_50_8265 end

    def Function_51_8284(): pass

    label("Function_51_8284")


    def lambda_8289():
        OP_95(0xFE, -3000, 0, 8000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_8289)
    WaitChrThread(0x104, 1)
    Return()

    # Function_51_8284 end

    def Function_52_82A3(): pass

    label("Function_52_82A3")


    def lambda_82A8():
        OP_95(0xFE, -5000, 0, -5000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_82A8)
    WaitChrThread(0xFE, 1)

    def lambda_82C6():
        OP_95(0xFE, -5000, 0, -3600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_82C6)
    WaitChrThread(0xFE, 1)

    def lambda_82E4():
        OP_95(0xFE, -5000, 0, 30, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_82E4)
    WaitChrThread(0xFE, 1)

    def lambda_8302():
        OP_95(0xFE, -5000, 0, 3300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8302)
    WaitChrThread(0xFE, 1)

    def lambda_8320():
        OP_95(0xFE, 440, 0, 3300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8320)
    WaitChrThread(0xFE, 1)

    def lambda_833E():
        OP_95(0xFE, 440, 0, 8900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_833E)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_52_82A3 end

    def Function_53_8358(): pass

    label("Function_53_8358")


    def lambda_835D():
        OP_95(0xFE, -60, 0, -3600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_835D)

    def lambda_8377():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_8377)
    WaitChrThread(0xFE, 1)

    def lambda_838C():
        OP_95(0xFE, -5000, 0, -3600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_838C)
    WaitChrThread(0xFE, 1)

    def lambda_83AA():
        OP_95(0xFE, -5000, 0, 30, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_83AA)
    WaitChrThread(0xFE, 1)

    def lambda_83C8():
        OP_95(0xFE, -5000, 0, 3300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_83C8)
    WaitChrThread(0xFE, 1)

    def lambda_83E6():
        OP_95(0xFE, 440, 0, 3300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_83E6)
    WaitChrThread(0xFE, 1)

    def lambda_8404():
        OP_95(0xFE, 440, 0, 8900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8404)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_53_8358 end

    def Function_54_8422(): pass

    label("Function_54_8422")

    Sleep(900)

    def lambda_842A():
        OP_95(0xFE, -5000, 0, -3600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_842A)
    WaitChrThread(0xFE, 1)

    def lambda_8448():
        OP_95(0xFE, -5000, 0, 30, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8448)
    WaitChrThread(0xFE, 1)

    def lambda_8466():
        OP_95(0xFE, -5000, 0, 3300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8466)
    WaitChrThread(0xFE, 1)

    def lambda_8484():
        OP_95(0xFE, 440, 0, 3300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8484)
    WaitChrThread(0xFE, 1)

    def lambda_84A2():
        OP_95(0xFE, 440, 0, 8900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_84A2)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_54_8422 end

    def Function_55_84C0(): pass

    label("Function_55_84C0")


    def lambda_84C5():
        OP_95(0xFE, -60, 0, -3600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_84C5)

    def lambda_84DF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_84DF)
    WaitChrThread(0xFE, 1)

    def lambda_84F4():
        OP_95(0xFE, -5000, 0, -3600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_84F4)
    WaitChrThread(0xFE, 1)

    def lambda_8512():
        OP_95(0xFE, -5000, 0, 1150, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8512)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_55_84C0 end

    def Function_56_8530(): pass

    label("Function_56_8530")

    ClearChrFlags(0x2A, 0x80)
    SetChrChipByIndex(0x2A, 0x1F)
    SetChrSubChip(0x2A, 0x0)
    SetChrPos(0x2A, 100990, 0, -4180, 270)
    ClearChrFlags(0x2B, 0x80)
    SetChrChipByIndex(0x2B, 0x20)
    SetChrSubChip(0x2B, 0x0)
    SetChrPos(0x2B, 92890, 0, 2210, 90)
    ClearChrFlags(0x2F, 0x80)
    SetChrChipByIndex(0x2F, 0x5)
    SetChrSubChip(0x2F, 0x0)
    SetChrPos(0x2F, 100360, 0, 3970, 90)
    ClearChrFlags(0x30, 0x80)
    SetChrChipByIndex(0x30, 0x21)
    SetChrSubChip(0x30, 0x0)
    SetChrPos(0x30, 102900, 0, 3710, 270)
    ClearChrFlags(0x31, 0x80)
    SetChrChipByIndex(0x31, 0xD)
    SetChrSubChip(0x31, 0x0)
    SetChrPos(0x31, 162320, 150, 3010, 270)
    ClearChrFlags(0x32, 0x80)
    SetChrChipByIndex(0x32, 0x22)
    SetChrSubChip(0x32, 0x0)
    SetChrPos(0x32, 159720, 150, 3010, 90)
    ClearChrFlags(0x2D, 0x80)
    SetChrPos(0x2D, 104170, 0, -5830, 0)
    BeginChrThread(0x2D, 0, 0, 0)
    ClearChrFlags(0x2E, 0x80)
    SetChrPos(0x2E, 96390, 0, 6290, 180)
    BeginChrThread(0x2E, 0, 0, 0)
    ClearChrFlags(0x2C, 0x80)
    SetChrPos(0x2C, 152940, 0, 3430, 180)
    BeginChrThread(0x2C, 0, 0, 0)
    Return()

    # Function_56_8530 end

    def Function_57_8639(): pass

    label("Function_57_8639")

    Return()

    # Function_57_8639 end

    def Function_58_863A(): pass

    label("Function_58_863A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_4B(0x2D, 0xFF)
    OP_4B(0x2E, 0xFF)
    OP_4B(0x2C, 0xFF)
    OP_4B(0x29, 0xFF)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(97480, 750, -770, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(28920, 0)
    OP_0D()
    ClearChrFlags(0x29, 0x80)
    SetChrPos(0x29, 95990, 0, -8109, 0)
    OP_A7(0x29, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x2D, 0x40)
    ClearChrFlags(0x2E, 0x40)
    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    Sound(105, 0, 100, 0)

    def lambda_86F4():
        OP_95(0xFE, 95610, 0, -6230, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_86F4)

    def lambda_870E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x29, 2, lambda_870E)
    WaitChrThread(0x29, 1)
    WaitChrThread(0x29, 2)

    #C0340
    ChrTalk(
        0x29,
        (
            "#0500F乗客の皆様、先ほど\x01",
            "クロスベル市行きのバスが\x01",
            "到着いたしました。\x02\x03",

            "ご搭乗の方は駐車場の方に\x01",
            "向かわれて下さい。\x02",
        )
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0x30,
        (
            "#12Pバスが来たんですって。\x01",
            "兄さん、行きましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0x2F,
        "#6Pああ、そうだな。\x02",
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0x2B,
        (
            "#6Pうふふ、やっと孫に\x01",
            "会いに行けるわねぇ。\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x2A, 0x18)
    SetChrSubChip(0x2A, 0x0)
    SetChrPos(0x2A, 100730, 0, -5320, 180)
    SetChrChipByIndex(0x2B, 0x19)
    SetChrSubChip(0x2B, 0x0)
    SetChrPos(0x2B, 92920, 0, 1410, 180)
    SetChrChipByIndex(0x2F, 0x9)
    SetChrSubChip(0x2F, 0x0)
    SetChrPos(0x2F, 99180, 0, 4019, 180)
    SetChrChipByIndex(0x30, 0x1D)
    SetChrSubChip(0x30, 0x0)
    SetChrPos(0x30, 104160, 0, 3700, 180)
    SetChrPos(0x2C, 98010, 0, 8280, 0)
    SetChrPos(0x31, 98010, 0, 8280, 0)
    SetChrPos(0x32, 98010, 0, 8280, 0)
    Sound(820, 0, 100, 0)
    SetChrFlags(0x2C, 0x40)
    SetChrFlags(0x31, 0x40)
    SetChrFlags(0x32, 0x40)
    SetChrChipByIndex(0x31, 0x6)
    SetChrChipByIndex(0x32, 0x1E)
    OP_A7(0x2C, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x31, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x32, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_0D()
    BeginChrThread(0x29, 3, 0, 63)
    BeginChrThread(0x2A, 3, 0, 64)
    BeginChrThread(0x2D, 3, 0, 65)
    BeginChrThread(0x2B, 3, 0, 66)
    BeginChrThread(0x2E, 3, 0, 67)
    BeginChrThread(0x2F, 3, 0, 68)
    BeginChrThread(0x30, 3, 0, 69)
    Sleep(2500)
    OP_71(0x3, 0x0, 0x5, 0x0, 0x0)
    Sound(105, 0, 100, 0)
    OP_79(0x3)
    BeginChrThread(0x31, 3, 0, 70)
    Sleep(700)
    BeginChrThread(0x32, 3, 0, 70)
    Sleep(1500)
    BeginChrThread(0x2C, 3, 0, 70)
    Sleep(1500)
    OP_71(0x3, 0x5, 0x0, 0x0, 0x0)
    Sound(106, 0, 100, 0)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_68(95930, 1150, -2040, 0)
    MoveCamera(44, 24, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(24270, 0)
    SetChrFlags(0x2A, 0x80)
    SetChrFlags(0x2D, 0x80)
    SetChrFlags(0x31, 0x80)
    SetChrFlags(0x32, 0x80)
    SetChrFlags(0x2C, 0x80)
    SetChrFlags(0x2B, 0x80)
    SetChrFlags(0x2E, 0x80)
    SetChrFlags(0x2F, 0x80)
    SetChrFlags(0x30, 0x80)
    SetCameraDistance(23270, 3000)
    SetChrPos(0x101, 96600, 0, -1500, 180)
    SetChrPos(0x102, 95100, 0, -1500, 180)
    SetChrPos(0x103, 96600, 0, 0, 180)
    SetChrPos(0x104, 95100, 0, 0, 180)
    SetChrPos(0x29, 95850, 0, -3800, 0)
    FadeToBright(500, 0)
    OP_0D()

    #C0344
    ChrTalk(
        0x29,
        "#12P#0501F……首尾はどうでしたか？\x02",
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0x103,
        (
            "#5P#0200F……偽ブランド業者を確定するには、\x01",
            "情報が足りないという印象でしたけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0x104,
        (
            "#5P#0301Fどいつもこいつも、\x01",
            "記念祭に浮かれてるくらいしか\x01",
            "思わなかったなぁ。\x02\x03",

            "#0306Fつーか、ホントにあの中に\x01",
            "そんな悪人がいるのかねぇ？\x02",
        )
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0x101,
        "#5P#0003F…………………………\x02",
    )

    CloseMessageWindow()

    def lambda_8B92():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8B92)
    WaitChrThread(0x102, 1)

    #C0348
    ChrTalk(
        0x102,
        (
            "#5P#0105F……ロイド、もしかして……\x01",
            "何かに気づいたの？\x02",
        )
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0x101,
        (
            "#11P#0001F……ああ、少し引っかかることを\x01",
            "言っていた人物はいた。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x29, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0350
    ChrTalk(
        0x104,
        (
            "#5P#0305Fおいおい、マジか！？\x01",
            "一体そりゃ、どういう……\x02",
        )
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0x101,
        (
            "#11P#0003Fまだ、気になるって\x01",
            "レベルだけど。\x02\x03",

            "#0001Fバスの中で一度、\x01",
            "考えをまとめないとな。\x02",
        )
    )

    CloseMessageWindow()

    #C0352
    ChrTalk(
        0x103,
        (
            "#5P#0200Fだとすると、\x01",
            "急がないといけませんね。\x02\x03",

            "クロスベル市に着いてしまったら、\x01",
            "観光客が散り散りになって\x01",
            "マークしきれなくなります。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8DAD():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8DAD)
    WaitChrThread(0x102, 1)

    #C0353
    ChrTalk(
        0x102,
        (
            "#5P#0101Fええ、急いでバスの停留所に\x01",
            "向かいましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0354
    ChrTalk(
        0x29,
        (
            "#12P#0501Fクロスベル行きのバスは、\x01",
            "門を出てすぐの駐車場です。\x02\x03",

            "#0503F私はここまでしか手伝えませんが……\x01",
            "みなさん、健闘を祈ります！\x02",
        )
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0x101,
        "#5P#0000Fああ……ありがとう、ノエル曹長。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_4C(0x29, 0xFF)
    SetChrPos(0x0, -280, 0, 8060, 180)
    SetChrPos(0x29, 1720, 0, 7110, 270)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetMapObjFlags(0x4, 0x4)
    ModifyEventFlags(1, 2, 0x80)
    ModifyEventFlags(1, 3, 0x80)
    OP_29(0x1B, 0x1, 0xD)
    EventEnd(0x5)
    Return()

    # Function_58_863A end

    def Function_59_8F08(): pass

    label("Function_59_8F08")


    def lambda_8F0D():
        OP_95(0xFE, -1500, 0, 9500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8F0D)
    WaitChrThread(0x101, 1)
    Return()

    # Function_59_8F08 end

    def Function_60_8F27(): pass

    label("Function_60_8F27")


    def lambda_8F2C():
        OP_95(0xFE, -1500, 0, 8000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8F2C)
    WaitChrThread(0x102, 1)
    Return()

    # Function_60_8F27 end

    def Function_61_8F46(): pass

    label("Function_61_8F46")


    def lambda_8F4B():
        OP_95(0xFE, -3000, 0, 9500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8F4B)
    WaitChrThread(0x103, 1)
    Return()

    # Function_61_8F46 end

    def Function_62_8F65(): pass

    label("Function_62_8F65")


    def lambda_8F6A():
        OP_95(0xFE, -3000, 0, 8000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_8F6A)
    WaitChrThread(0x104, 1)
    Return()

    # Function_62_8F65 end

    def Function_63_8F84(): pass

    label("Function_63_8F84")


    def lambda_8F89():
        OP_95(0xFE, 93970, 0, -5720, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_8F89)
    WaitChrThread(0x29, 1)

    def lambda_8FA7():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_8FA7)
    WaitChrThread(0x29, 1)
    Return()

    # Function_63_8F84 end

    def Function_64_8FB4(): pass

    label("Function_64_8FB4")


    def lambda_8FB9():
        OP_95(0xFE, 100730, 0, -6040, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8FB9)
    WaitChrThread(0xFE, 1)

    def lambda_8FD7():
        OP_95(0xFE, 95850, 0, -6040, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8FD7)
    WaitChrThread(0xFE, 1)

    def lambda_8FF5():
        OP_95(0xFE, 95850, 0, -9890, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8FF5)

    def lambda_900F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_900F)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_64_8FB4 end

    def Function_65_9020(): pass

    label("Function_65_9020")

    Sleep(2000)

    def lambda_9028():
        OP_95(0xFE, 95850, 0, -6040, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9028)
    WaitChrThread(0xFE, 1)

    def lambda_9046():
        OP_95(0xFE, 95850, 0, -9890, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9046)

    def lambda_9060():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_9060)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_65_9020 end

    def Function_66_9071(): pass

    label("Function_66_9071")


    def lambda_9076():
        OP_95(0xFE, 92920, 0, -3460, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9076)
    WaitChrThread(0xFE, 1)

    def lambda_9094():
        OP_95(0xFE, 95850, 0, -3460, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9094)
    WaitChrThread(0xFE, 1)

    def lambda_90B2():
        OP_95(0xFE, 95850, 0, -9890, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_90B2)
    Sleep(2000)

    def lambda_90CF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_90CF)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_66_9071 end

    def Function_67_90E0(): pass

    label("Function_67_90E0")


    def lambda_90E5():
        OP_95(0xFE, 97290, 0, 4720, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_90E5)
    WaitChrThread(0xFE, 1)

    def lambda_9103():
        OP_95(0xFE, 95850, 0, -9890, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9103)
    Sleep(6000)

    def lambda_9120():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_9120)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_67_90E0 end

    def Function_68_9131(): pass

    label("Function_68_9131")


    def lambda_9136():
        OP_95(0xFE, 99180, 0, -330, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9136)
    WaitChrThread(0xFE, 1)

    def lambda_9154():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9154)
    WaitChrThread(0xFE, 1)
    Sleep(1000)

    def lambda_9168():
        OP_93(0xFE, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9168)
    WaitChrThread(0xFE, 1)

    def lambda_9179():
        OP_95(0xFE, 95850, 0, -330, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9179)
    WaitChrThread(0xFE, 1)

    def lambda_9197():
        OP_95(0xFE, 95850, 0, -9890, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9197)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_68_9131 end

    def Function_69_91B1(): pass

    label("Function_69_91B1")


    def lambda_91B6():
        OP_95(0xFE, 104160, 0, -330, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_91B6)
    WaitChrThread(0xFE, 1)

    def lambda_91D4():
        OP_95(0xFE, 95850, 0, -330, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_91D4)
    WaitChrThread(0xFE, 1)

    def lambda_91F2():
        OP_95(0xFE, 95850, 0, -9890, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_91F2)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_69_91B1 end

    def Function_70_920C(): pass

    label("Function_70_920C")

    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)

    def lambda_921C():
        OP_95(0xFE, 95850, 0, -9890, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_921C)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_70_920C end

    def Function_71_9236(): pass

    label("Function_71_9236")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_9274")

    #C0356
    ChrTalk(
        0x101,
        "#0001F今のうちに乗客に話を聞いておこう。\x02",
    )

    CloseMessageWindow()
    Jump("loc_92DA")

    label("loc_9274")


    #C0357
    ChrTalk(
        0x101,
        (
            "#0001Fクロスベル行きの\x01",
            "バスが来るまで、あまり時間がない。\x02\x03",

            "今のうちに乗客に話を聞いておこう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)

    label("loc_92DA")

    SetChrPos(0x0, 95790, 0, -5540, 0)
    EventEnd(0x5)
    Return()

    # Function_71_9236 end

    def Function_72_92EE(): pass

    label("Function_72_92EE")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_932C")

    #C0358
    ChrTalk(
        0x101,
        "#0001F今のうちに乗客に話を聞いておこう。\x02",
    )

    CloseMessageWindow()
    Jump("loc_9392")

    label("loc_932C")


    #C0359
    ChrTalk(
        0x101,
        (
            "#0001Fクロスベル行きの\x01",
            "バスが来るまで、あまり時間がない。\x02\x03",

            "今のうちに乗客に話を聞いておこう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)

    label("loc_9392")

    SetChrPos(0x0, 92410, 0, -50, 90)
    EventEnd(0x5)
    Return()

    # Function_72_92EE end

    def Function_73_93A6(): pass

    label("Function_73_93A6")

    EventBegin(0x0)

    #C0360
    ChrTalk(
        0x101,
        (
            "#0003Fもうすぐクロスベル行きのバスが出る……\x01",
            "バスの停留所に急ごう。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -8140, 0, 8140, 180)
    EventEnd(0x5)
    Return()

    # Function_73_93A6 end

    def Function_74_9405(): pass

    label("Function_74_9405")

    EventBegin(0x0)

    #C0361
    ChrTalk(
        0x101,
        (
            "#0003Fもうすぐクロスベル行きのバスが出る……\x01",
            "バスの停留所に急ごう。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 0, 0, 8140, 189)
    EventEnd(0x5)
    Return()

    # Function_74_9405 end

    def Function_75_9464(): pass

    label("Function_75_9464")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0362
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            "この先、警備隊専用貨物線路\x01",
            "    関係者以外立入禁止\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_75_9464 end

    SaveToFile()

Try(main)
