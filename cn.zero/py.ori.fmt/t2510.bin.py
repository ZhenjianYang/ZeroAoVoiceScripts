from ZeroScenarioHelper import *

def main():
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
        "奥利弗队员",             # 1
        "杰克队员",               # 2
        "阿雷库瑟队员",           # 3
        "提马斯",                 # 4
        "拉古",                   # 5
        "游客",                   # 6
        "商人",                   # 7
        "男孩",                   # 8
        "游客",                   # 9
        "游客",                   # 10
        "游客",                   # 11
        "游客",                   # 12
        "商人",                   # 13
        "游客",                   # 14
        "游客",                   # 15
        "游客",                   # 16
        "游客",                   # 17
        "游客",                   # 18
        "游客",                   # 19
        "游客",                   # 20
        "游客",                   # 21
        "商人",                   # 22
        "游客",                   # 23
        "游客",                   # 24
        "游客",                   # 25
        "游客",                   # 26
        "哈罗德",                 # 27
        "琪露露",                 # 28
        "游击士斯克特",           # 29
        "游击士温蔡尔",           # 30
        "游击士林",               # 31
        "游击士艾欧莉娅",         # 32
        "车１",                   # 33
        "诺艾尔上士",             # 34
        "黑发女性",               # 35
        "老婆婆",                 # 36
        "老人",                   # 37
        "贸易商",                 # 38
        "女性",                   # 39
        "哥哥",                   # 40
        "妹妹",                   # 41
        "父亲 ",                  # 42
        "男孩",                   # 43
        "巴士 ",                  # 44
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
    DeclNpc(100569,  50,      3920,    90,   469,  0x0, 0,   20,  0,   255, 255, 0,   34,  255,  0)
    DeclNpc(100599,  59,      4019,    90,   469,  0x0, 0,   21,  0,   255, 255, 0,   35,  255,  0)
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
        "Function_6_178F",         # 06, 6
        "Function_7_1AD8",         # 07, 7
        "Function_8_22C2",         # 08, 8
        "Function_9_22C6",         # 09, 9
        "Function_10_2AD4",        # 0A, 10
        "Function_11_2BE8",        # 0B, 11
        "Function_12_2BEC",        # 0C, 12
        "Function_13_31B1",        # 0D, 13
        "Function_14_3303",        # 0E, 14
        "Function_15_3443",        # 0F, 15
        "Function_16_34B9",        # 10, 16
        "Function_17_3632",        # 11, 17
        "Function_18_366B",        # 12, 18
        "Function_19_36FE",        # 13, 19
        "Function_20_387D",        # 14, 20
        "Function_21_38A3",        # 15, 21
        "Function_22_38C4",        # 16, 22
        "Function_23_3A00",        # 17, 23
        "Function_24_3A6D",        # 18, 24
        "Function_25_3BF1",        # 19, 25
        "Function_26_3C14",        # 1A, 26
        "Function_27_3C7B",        # 1B, 27
        "Function_28_3E9B",        # 1C, 28
        "Function_29_3F2D",        # 1D, 29
        "Function_30_3FAD",        # 1E, 30
        "Function_31_40F4",        # 1F, 31
        "Function_32_41B9",        # 20, 32
        "Function_33_4259",        # 21, 33
        "Function_34_4558",        # 22, 34
        "Function_35_46CE",        # 23, 35
        "Function_36_49CC",        # 24, 36
        "Function_37_4C4C",        # 25, 37
        "Function_38_4CB7",        # 26, 38
        "Function_39_513A",        # 27, 39
        "Function_40_5519",        # 28, 40
        "Function_41_5898",        # 29, 41
        "Function_42_5AEC",        # 2A, 42
        "Function_43_5E36",        # 2B, 43
        "Function_44_61F6",        # 2C, 44
        "Function_45_6378",        # 2D, 45
        "Function_46_665D",        # 2E, 46
        "Function_47_681B",        # 2F, 47
        "Function_48_73E5",        # 30, 48
        "Function_49_7404",        # 31, 49
        "Function_50_7423",        # 32, 50
        "Function_51_7442",        # 33, 51
        "Function_52_7461",        # 34, 52
        "Function_53_7516",        # 35, 53
        "Function_54_75E0",        # 36, 54
        "Function_55_767E",        # 37, 55
        "Function_56_76EE",        # 38, 56
        "Function_57_77F7",        # 39, 57
        "Function_58_77F8",        # 3A, 58
        "Function_59_7FD8",        # 3B, 59
        "Function_60_7FF7",        # 3C, 60
        "Function_61_8016",        # 3D, 61
        "Function_62_8035",        # 3E, 62
        "Function_63_8054",        # 3F, 63
        "Function_64_8084",        # 40, 64
        "Function_65_80F0",        # 41, 65
        "Function_66_8141",        # 42, 66
        "Function_67_81B0",        # 43, 67
        "Function_68_8201",        # 44, 68
        "Function_69_8281",        # 45, 69
        "Function_70_82DC",        # 46, 70
        "Function_71_8306",        # 47, 71
        "Function_72_83A8",        # 48, 72
        "Function_73_844A",        # 49, 73
        "Function_74_84A9",        # 4A, 74
        "Function_75_8508",        # 4B, 75
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

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_FC2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F46")

    #C0001
    ChrTalk(
        0x8,
        (
            "那么，今天的盘查工作\x01",
            "也必须努力呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        (
            "既然上级都已经腐败了，\x01",
            "所以现在无论怎样管制也\x01",
            "会有漏网之鱼……\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x8,
        (
            "但我们正在做的事情\x01",
            "绝对不是没有意义的哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_FBD")

    label("loc_F46")


    #C0004
    ChrTalk(
        0x8,
        (
            "因为司令收受贿赂，\x01",
            "所以无论怎样管制也\x01",
            "都会有漏网之鱼。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x8,
        (
            "但是，只要不放弃，\x01",
            "我们所做的工作就绝不是没有意义的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FBD")

    Jump("loc_1749")

    label("loc_FC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1067")

    #C0006
    ChrTalk(
        0x8,
        (
            "盘查中不知道发现了\x01",
            "多少次走私物品……\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x8,
        (
            "但那些人大多数都会\x01",
            "通过贿赂来获得放行。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x8,
        (
            "只要有钱，做了坏事也能免受制裁……\x01",
            "这种体制绝对是错误的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1749")

    label("loc_1067")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1234")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_120B")

    #C0009
    ChrTalk(
        0x8,
        (
            "诺艾尔上士……\x01",
            "这几位就是您说过的……\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x109,
        (
            "#0500F是，这几位就是对我们多方关照的\x01",
            "特别任务支援科的各位。\x02\x03",

            "调查遗迹的工作\x01",
            "还要仰仗他们的帮助。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x8,
        (
            "这样啊……对不起，\x01",
            "都因为我们太没用了……\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x101,
        (
            "#0000F不，请不必在意，\x01",
            "我们对这种工作已经习以为常了。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x104,
        (
            "#0304F哈哈，完全没错。\x02\x03",

            "#0300F总之，调查的事情就交给我们，\x01",
            "你们就加油做好国境门的警备工作吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x8,
        (
            "是……\x01",
            "诺艾尔上士就拜托你们多关照了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_122F")

    label("loc_120B")


    #C0015
    ChrTalk(
        0x8,
        "诺艾尔上士就拜托你们多关照了。\x02",
    )

    CloseMessageWindow()

    label("loc_122F")

    Jump("loc_1749")

    label("loc_1234")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1290")

    #C0016
    ChrTalk(
        0x8,
        (
            "嗯，导力车的检查\x01",
            "相当棘手啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x8,
        (
            "杰克好像也很忙……\x01",
            "真希望能得到帮助。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1749")

    label("loc_1290")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1380")
    OP_4B(0x8, 0xFF)
    OP_4B(0x15, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1323")

    #C0018
    ChrTalk(
        0x8,
        "……好，没问题了。\x02",
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x8,
        (
            "开往共和国的定期巴士\x01",
            "将在四十分钟之后抵达，\x01",
            "在那之前，请好好休息。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x15,
        "嗯，谢谢。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1373")

    label("loc_1323")


    #C0021
    ChrTalk(
        0x8,
        (
            "如果您不嫌弃的话，\x01",
            "可以去食堂用餐。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x15,
        (
            "嗯，刚好肚子饿了。\x01",
            "就去尝一尝吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1373")

    OP_4C(0x8, 0xFF)
    OP_4C(0x15, 0xFF)
    Jump("loc_1749")

    label("loc_1380")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_14B4")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1402")

    #C0023
    ChrTalk(
        0x8,
        (
            "杰克那家伙，白天去克洛斯贝尔市\x01",
            "检查货物了。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x8,
        (
            "不用留下来对付假货商这种\x01",
            "麻烦的对手，还真是幸运。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14AF")

    label("loc_1402")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0xD)"), scpexpr(EXPR_END)), "loc_146D")

    #C0025
    ChrTalk(
        0x8,
        (
            "假货商吗……\x01",
            "光凭外表是无法判断的啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x8,
        (
            "恶人才更加\x01",
            "擅于伪装成好人呢。\x01",
            "要注意哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14AF")

    label("loc_146D")


    #C0027
    ChrTalk(
        0x8,
        (
            "从共和国来的巴士\x01",
            "在午后就会抵达。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x8,
        (
            "嗯……\x01",
            "要忙起来了哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14AF")

    Jump("loc_1749")

    label("loc_14B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_15D5")
    OP_4B(0x8, 0xFF)
    OP_4B(0x10, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1554")

    #C0029
    ChrTalk(
        0x8,
        (
            "那么，请在这边的入境证上\x01",
            "签名……\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x10,
        (
            "（唰唰唰）……\x01",
            "这样可以吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x8,
        (
            "……好的，没问题了。\x01",
            "祝您在纪念庆典中玩得愉快。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_15C8")

    label("loc_1554")


    #C0032
    ChrTalk(
        0x8,
        (
            "出门后顺着道路\x01",
            "一直走，就可以\x01",
            "到克洛斯贝尔市了。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x8,
        "祝您在纪念庆典中玩得愉快。\x02",
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x10,
        "呵呵，感谢您的亲切说明。\x02",
    )

    CloseMessageWindow()

    label("loc_15C8")

    OP_4C(0x8, 0xFF)
    OP_4C(0x10, 0xFF)
    Jump("loc_1749")

    label("loc_15D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_16D1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_168E")
    OP_4B(0x8, 0xFF)
    OP_4B(0xE, 0xFF)

    #C0035
    ChrTalk(
        0x8,
        (
            "那么，为慎重起见，\x01",
            "我要检查一下货物。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x8,
        (
            "这是规定，\x01",
            "还请稍等片刻。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xE,
        (
            "真是麻烦啊……\x01",
            "唉，没办法的事。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xE,
        (
            "我儿子在等我，\x01",
            "请快一些。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    OP_4C(0x8, 0xFF)
    OP_4C(0xE, 0xFF)
    Jump("loc_16CC")

    label("loc_168E")


    #C0039
    ChrTalk(
        0xE,
        (
            "哎呀呀，真是麻烦。\x01",
            "儿子还在食堂等着我呢，\x01",
            "拜托你快一些。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16CC")

    Jump("loc_1749")

    label("loc_16D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1749")

    #C0040
    ChrTalk(
        0x8,
        (
            "在这里会对\x01",
            "来往于共和国的车辆\x01",
            "进行一定程度的检查。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x8,
        (
            "但是，这么简陋的大门，\x01",
            "要是想强行通过也很容易吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1749")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_175F")
    TalkEnd(0x15)
    Jump("loc_178E")

    label("loc_175F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1775")
    TalkEnd(0x10)
    Jump("loc_178E")

    label("loc_1775")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_178B")
    TalkEnd(0xE)
    Jump("loc_178E")

    label("loc_178B")

    TalkEnd(0x8)

    label("loc_178E")

    Return()

    # Function_5_E4A end

    def Function_6_178F(): pass

    label("Function_6_178F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_17E3")

    #C0042
    ChrTalk(
        0xFE,
        "没有异常！\x02",
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xFE,
        (
            "我只是在值得信任的长官的领导下\x01",
            "执行任务而已！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AD4")

    label("loc_17E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1828")

    #C0044
    ChrTalk(
        0xFE,
        "货物没有异常！\x02",
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xFE,
        (
            "在接待处签个名\x01",
            "就可以通过了！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AD4")

    label("loc_1828")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1865")

    #C0046
    ChrTalk(
        0xFE,
        "没有异常！\x02",
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xFE,
        (
            "诺艾尔上士！\x01",
            "任务辛苦了！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AD4")

    label("loc_1865")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_18AE")

    #C0048
    ChrTalk(
        0xFE,
        (
            "除了我自己的体力之外……\x01",
            "没有异常！\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xFE,
        "真是太忙了！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1AD4")

    label("loc_18AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_18E0")

    #C0050
    ChrTalk(
        0xFE,
        "没有异常！\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xFE,
        "又要忙起来了！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1AD4")

    label("loc_18E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1A2E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_19B4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1971")
    TurnDirection(0x9, 0x13, 0)

    #C0052
    ChrTalk(
        0xFE,
        (
            "开往克洛斯贝尔市的定期巴士\x01",
            "将从出门右边的乘车场\x01",
            "发车。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xFE,
        (
            "郊外方面今天没有异常！\x01",
            "继续警戒！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_19AF")

    label("loc_1971")


    #C0054
    ChrTalk(
        0xFE,
        (
            "呼……\x01",
            "有不少游客都是第一次来，\x01",
            "所以指路的工作量相当大。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19AF")

    Jump("loc_1A29")

    label("loc_19B4")


    #C0055
    ChrTalk(
        0xFE,
        (
            "稍后要去克洛斯贝尔市的\x01",
            "车站执行公务。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xFE,
        (
            "贝尔加德门的罗梅奥队员经常\x01",
            "会去车站执行任务，\x01",
            "他这次将会和我一起去。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A29")

    Jump("loc_1AD4")

    label("loc_1A2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1A6D")

    #C0057
    ChrTalk(
        0xFE,
        (
            "目前暂且……\x01",
            "没有异常！\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xFE,
        "忙到头晕眼花！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1AD4")

    label("loc_1A6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1AA7")

    #C0059
    ChrTalk(
        0xFE,
        "货物没有异常！\x02",
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xFE,
        "正在进行仔细检查！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1AD4")

    label("loc_1AA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1AD4")

    #C0061
    ChrTalk(
        0xFE,
        "没有异常！\x02",
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xFE,
        "继续警备工作！\x02",
    )

    CloseMessageWindow()

    label("loc_1AD4")

    TalkEnd(0xFE)
    Return()

    # Function_6_178F end

    def Function_7_1AD8(): pass

    label("Function_7_1AD8")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1B6C")
    Jump("loc_1BB6")

    label("loc_1B6C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1B8C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1BB6")

    label("loc_1B8C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1BAC")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1BB6")

    label("loc_1BAC")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1BB6")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1C43")

    #C0063
    ChrTalk(
        0xFE,
        (
            "由于巴士往来频繁，\x01",
            "所以要好好整理停车场。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xFE,
        (
            "……但是我肚子好饿，\x01",
            "午休快点来吧……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22BA")

    label("loc_1C43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1D4E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CFE")

    #C0065
    ChrTalk(
        0xFE,
        (
            "巴雷尔那家伙已经\x01",
            "完全康复了，\x01",
            "警备布署也复原了。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xFE,
        (
            "哎呀呀，在不熟悉的地方担任警备\x01",
            "真是好累啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xFE,
        (
            "……总之，我还是先填饱肚子，\x01",
            "然后再重新开始工作吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_1D49")

    label("loc_1CFE")


    #C0068
    ChrTalk(
        0xFE,
        (
            "我还是先填饱肚子，\x01",
            "再重新开始工作吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xFE,
        "（狼吞虎咽……）嗯～好吃！\x02",
    )

    CloseMessageWindow()

    label("loc_1D49")

    Jump("loc_22BA")

    label("loc_1D4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1D5C")
    Jump("loc_22BA")

    label("loc_1D5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1DD5")

    #C0070
    ChrTalk(
        0xFE,
        (
            "啊～好忙啊好忙啊。\x01",
            "工作很忙，必须快点吃完。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xFE,
        (
            "……但是吃太快的话\x01",
            "对身体不好吧，\x01",
            "真是左右为难啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22BA")

    label("loc_1DD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1EB2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E3B")

    #C0072
    ChrTalk(
        0xFE,
        (
            "看样子，明天会很忙呢。\x01",
            "趁现在赶快补充体力吧！\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)

    #C0073
    ChrTalk(
        0xFE,
        "（狼吞虎咽！）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_1EAD")

    label("loc_1E3B")

    SetChrSubChip(0xFE, 0x0)

    #C0074
    ChrTalk(
        0xFE,
        "（狼吞虎咽！）\x02",
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xFE,
        (
            "咕！……………………\x01",
            "……………………咳咳。\x01",
            "呼啊………………\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xFE,
        "……（狼吞虎咽！）\x02",
    )

    CloseMessageWindow()

    label("loc_1EAD")

    Jump("loc_22BA")

    label("loc_1EB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2002")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1FB2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F55")

    #C0077
    ChrTalk(
        0xFE,
        (
            "看到这么多游客，\x01",
            "我突然……\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xFE,
        (
            "就想去一次\x01",
            "利贝尔王国了。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xFE,
        (
            "那里的空气新鲜，水质清澈，\x01",
            "应该能吃到很美味的\x01",
            "料理吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_1FAD")

    label("loc_1F55")


    #C0080
    ChrTalk(
        0xFE,
        (
            "虽然我个人觉得阿尔摩利卡产的\x01",
            "蔬果也已经很好吃了……\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xFE,
        (
            "但还是想去一趟\x01",
            "利贝尔啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FAD")

    Jump("loc_1FFD")

    label("loc_1FB2")


    #C0082
    ChrTalk(
        0xFE,
        (
            "虽说还是上午，\x01",
            "肚子却好饿啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xFE,
        "……要是有人来送慰问品给我就好了。\x02",
    )

    CloseMessageWindow()

    label("loc_1FFD")

    Jump("loc_22BA")

    label("loc_2002")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2124")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_20D4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_208F")

    #C0084
    ChrTalk(
        0xFE,
        (
            "这个食堂是客人与队员\x01",
            "共用的。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0xFE,
        (
            "虽说是这样，要穿着制服的人在里面，\x01",
            "客人们也没法好好用餐吧……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_20CF")

    label("loc_208F")


    #C0086
    ChrTalk(
        0xFE,
        (
            "今天人也非常多……\x01",
            "没办法，还是快点吃完\x01",
            "然后回到岗位上吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20CF")

    Jump("loc_211F")

    label("loc_20D4")


    #C0087
    ChrTalk(
        0xFE,
        (
            "虽说还是上午，\x01",
            "肚子却好饿啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xFE,
        "……要是有人来送慰问品给我就好了。\x02",
    )

    CloseMessageWindow()

    label("loc_211F")

    Jump("loc_22BA")

    label("loc_2124")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_21C3")

    #C0089
    ChrTalk(
        0xFE,
        (
            "食堂的食物\x01",
            "虽说还算美味……\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0xFE,
        (
            "但给警备队发放的携带干粮\x01",
            "真的算不上是食物。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xFE,
        (
            "特别是对我这种自称美食家的人来说，\x01",
            "真是一个严重的问题啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22BA")

    label("loc_21C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_22BA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2256")

    #C0092
    ChrTalk(
        0xFE,
        (
            "（狼吞虎咽……）\x01",
            "好吃好吃……\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xFE,
        "食堂的食物还算不错了。\x02",
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xFE,
        (
            "不过，克洛斯贝尔市龙老饭店\x01",
            "那边的饭菜味道也很好哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_22BA")

    label("loc_2256")


    #C0095
    ChrTalk(
        0xFE,
        (
            "不值班的时候，\x01",
            "我都会去龙老饭店吃饭。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xFE,
        (
            "食堂的饭菜虽说还不错，\x01",
            "但那边的食物更让人欲罢不能。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22BA")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_7_1AD8 end

    def Function_8_22C2(): pass

    label("Function_8_22C2")

    Call(0, 9)
    Return()

    # Function_8_22C2 end

    def Function_9_22C6(): pass

    label("Function_9_22C6")

    TalkBegin(0xB)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_22D3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AD0")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",      # 0
            "购物\x01",      # 1
            "放弃\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2323")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_2323")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2343")
    OP_AF(0x6E)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2ACB")

    label("loc_2343")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2357")
    Jump("loc_2ACB")

    label("loc_2357")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2ACB")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_23FF")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x7)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_238C")
    Call(0, 10)
    Jump("loc_23FA")

    label("loc_238C")


    #C0097
    ChrTalk(
        0xB,
        (
            "一到了中午，警备队的人也会\x01",
            "过来吃饭，到时候会很忙。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0xB,
        (
            "唔……客人还很少，\x01",
            "就趁这段时间，先做好准备吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23FA")

    Jump("loc_2ACB")

    label("loc_23FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_2498")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x7)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_241B")
    Call(0, 10)
    Jump("loc_2493")

    label("loc_241B")


    #C0099
    ChrTalk(
        0xB,
        (
            "最近，偶尔会有人为了来这里吃饭\x01",
            "而专程赶到唐古拉姆门来。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xB,
        (
            "能让人吃了还想吃，\x01",
            "对于一个厨师来说就是最幸福的事了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2493")

    Jump("loc_2ACB")

    label("loc_2498")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_25FA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x7)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24B4")
    Call(0, 10)
    Jump("loc_25F5")

    label("loc_24B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_259F")

    #C0101
    ChrTalk(
        0xB,
        (
            "哎呀，诺艾尔上士……\x01",
            "你现在要去执行任务吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x109,
        (
            "#0500F是的。\x02\x03",

            "#0509F提马斯先生，机会难得。\x01",
            "您就做点什么拿手好菜\x01",
            "请我们吃吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xB,
        (
            "哈哈哈，就算是上士拜托我，\x01",
            "饭菜也不能免费哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xB,
        (
            "想吃东西的话，\x01",
            "就乖乖付钱吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_25F5")

    label("loc_259F")


    #C0105
    ChrTalk(
        0xB,
        (
            "就算是上士拜托我，\x01",
            "饭菜也是不能免费的哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xB,
        (
            "想吃好东西的话，\x01",
            "先付钱再来吃吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25F5")

    Jump("loc_2ACB")

    label("loc_25FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2656")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x7)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2616")
    Call(0, 10)
    Jump("loc_2651")

    label("loc_2616")


    #C0107
    ChrTalk(
        0xB,
        "今天来了好多客人。\x02",
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0xB,
        (
            "一个人接待\x01",
            "果然忙不过来啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2651")

    Jump("loc_2ACB")

    label("loc_2656")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2781")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x7)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2672")
    Call(0, 10)
    Jump("loc_277C")

    label("loc_2672")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2736")

    #C0109
    ChrTalk(
        0xB,
        (
            "索妮亚副司令\x01",
            "在午休时会与其他队员错开，\x01",
            "最后一个吃午饭。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xB,
        (
            "比起和部下一起吃饭联络感情，\x01",
            "副司令还是倾向于与他们划清界限。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0xB,
        (
            "她很了解一个上司该怎么做，\x01",
            "真是个聪明的人。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_277C")

    label("loc_2736")


    #C0112
    ChrTalk(
        0xB,
        (
            "……为什么索妮亚副司令\x01",
            "不是警备队的司令呢……\x01",
            "真是太不可思议了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_277C")

    Jump("loc_2ACB")

    label("loc_2781")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_28F8")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x7)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_279D")
    Call(0, 10)
    Jump("loc_28F3")

    label("loc_279D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2831")

    #C0113
    ChrTalk(
        0xB,
        (
            "其实，面向一般客人的菜式和\x01",
            "面向警卫队员的菜式是不一样的。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xB,
        (
            "警备队员因为\x01",
            "不得不从早忙到晚，所以\x01",
            "菜式中多是补充体力的料理。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28F3")

    label("loc_2831")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_28A2")

    #C0115
    ChrTalk(
        0xB,
        (
            "噢～……\x01",
            "白天果然人很多啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0xB,
        (
            "而且，还要配合共和国人\x01",
            "的口味来烹制，\x01",
            "所以真是够辛苦的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28F3")

    label("loc_28A2")


    #C0117
    ChrTalk(
        0xB,
        "必须趁现在做好相关准备呢。\x02",
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xB,
        (
            "共和国来的巴士抵达之后\x01",
            "就要变得忙碌起来了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28F3")

    Jump("loc_2ACB")

    label("loc_28F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_298B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x7)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2914")
    Call(0, 10)
    Jump("loc_2986")

    label("loc_2914")


    #C0119
    ChrTalk(
        0xB,
        (
            "除了乘导力列车之外，\x01",
            "好像也有不少\x01",
            "徒步到这里的人。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xB,
        (
            "不过，从共和国过来\x01",
            "基本就是一条直路……\x01",
            "不会迷路的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2986")

    Jump("loc_2ACB")

    label("loc_298B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2A07")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x7)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29A7")
    Call(0, 10)
    Jump("loc_2A02")

    label("loc_29A7")


    #C0121
    ChrTalk(
        0xB,
        (
            "担任唐古拉姆门的勤务人员\x01",
            "快一年了……\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0xB,
        (
            "能让外国人\x01",
            "品尝我做的食物，\x01",
            "我觉得很开心。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A02")

    Jump("loc_2ACB")

    label("loc_2A07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2ACB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A6D")

    #C0123
    ChrTalk(
        0xB,
        (
            "这里为停下来吃饭的旅行者们\x01",
            "准备了一整套的设施。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xB,
        "你也吃点什么吧？\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2ACB")

    label("loc_2A6D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x7)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A80")
    Call(0, 10)
    Jump("loc_2ACB")

    label("loc_2A80")


    #C0125
    ChrTalk(
        0xB,
        (
            "这里为停下来吃饭的旅行者们\x01",
            "准备了一整套的设施。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0xB,
        "你也吃点什么吧？\x02",
    )

    CloseMessageWindow()

    label("loc_2ACB")

    Jump("loc_22D3")

    label("loc_2AD0")

    TalkEnd(0xB)
    Return()

    # Function_9_22C6 end

    def Function_10_2AD4(): pass

    label("Function_10_2AD4")


    #C0127
    ChrTalk(
        0xB,
        (
            "前阵子我从几个好像是叫钓公师团\x01",
            "的人那里\x01",
            "学来了美味鱼锅的食谱。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0xB,
        (
            "吃鱼对身体有好处哦。　\x01",
            "下次要不要做来给队员们吃呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xB,
        (
            "对了，也教给你们吧。\x01",
            "大家一起品尝吧。\x02",
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
            scpstr(SCPSTR_CODE_ITEM, '芳醇潮锅'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "的做法被教授了。\x02",
        )
    )

    CloseMessageWindow()

    #A0131
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '芳醇潮锅'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "的做法已经学会了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    OP_B0(0x7)
    Return()

    # Function_10_2AD4 end

    def Function_11_2BE8(): pass

    label("Function_11_2BE8")

    Call(0, 12)
    Return()

    # Function_11_2BE8 end

    def Function_12_2BEC(): pass

    label("Function_12_2BEC")

    TalkBegin(0xC)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2BF9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_31AD")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",      # 0
            "休息\x01",      # 1
            "放弃\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2C49")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_2C49")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C69")
    OP_AF(0x6F)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_31A8")

    label("loc_2C69")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2C7D")
    Jump("loc_31A8")

    label("loc_2C7D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_31A8")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2D02")

    #C0132
    ChrTalk(
        0xC,
        (
            "这么早就来招待所，\x01",
            "真是些奇怪的家伙。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xC,
        (
            "……不过无所谓啦。\x01",
            "如果是要休息，就自便好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31A8")

    label("loc_2D02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_2E3B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DCB")

    #C0134
    ChrTalk(
        0xC,
        (
            "索妮亚副司令\x01",
            "为了不让队员负担过重，\x01",
            "似乎精心分配了工作量。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xC,
        (
            "因为如果处在疲劳状态的话，\x01",
            "一旦有紧急事件出现就无法应对了。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xC,
        (
            "你们也要随时保持一个\x01",
            "万全的身体状况啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2E36")

    label("loc_2DCB")


    #C0137
    ChrTalk(
        0xC,
        (
            "为了保证随时都能应对突发事件，\x01",
            "该休息的时候就要好好休息。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xC,
        "愿意的话，在这所设施里休息一下也行啊。\x02",
    )

    CloseMessageWindow()

    label("loc_2E36")

    Jump("loc_31A8")

    label("loc_2E3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2EDB")

    #C0139
    ChrTalk(
        0xC,
        (
            "好像是因为出现了什么怪物，\x01",
            "唐古拉姆门的警备队员都\x01",
            "不敢去执行任务了。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xC,
        (
            "一群胆小鬼。\x01",
            "就算是怪物又如何，\x01",
            "不是都已经和魔兽战斗过很多次了吗。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31A8")

    label("loc_2EDB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2F3A")

    #C0141
    ChrTalk(
        0xC,
        "……大家看上去很忙。\x02",
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xC,
        (
            "我现在比较闲，等会要不要去\x01",
            "提马斯那里帮帮忙呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31A8")

    label("loc_2F3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2FAF")

    #C0143
    ChrTalk(
        0xC,
        (
            "我是伊莉娅·普拉提耶的\x01",
            "超级崇拜者……\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0xC,
        (
            "因为要在这种地方执勤，\x01",
            "所以没法去看彩虹剧团\x01",
            "的公演……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31A8")

    label("loc_2FAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_307D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_302C")

    #C0145
    ChrTalk(
        0xC,
        (
            "……要休息吗？\x01",
            "现在倒是有不少空房间哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xC,
        (
            "因为是纪念庆典，\x01",
            "所以不会有游客在\x01",
            "这种地方住吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3078")

    label("loc_302C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_305C")

    #C0147
    ChrTalk(
        0xC,
        "……今天的客人好多啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3078")

    label("loc_305C")


    #C0148
    ChrTalk(
        0xC,
        "……什么啊，要休息吗？\x02",
    )

    CloseMessageWindow()

    label("loc_3078")

    Jump("loc_31A8")

    label("loc_307D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_30CA")

    #C0149
    ChrTalk(
        0xC,
        (
            "『彩虹剧团』公演……\x01",
            "昨天是首演哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xC,
        "……好想去啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_31A8")

    label("loc_30CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_315E")

    #C0151
    ChrTalk(
        0xC,
        (
            "在我们这边住宿的都是\x01",
            "共和国来的旅行者和\x01",
            "贸易商这样的人。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xC,
        (
            "偶尔也有错过巴士，\x01",
            "滞留在此的人留宿，\x01",
            "所以这样的设施很有必要的啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31A8")

    label("loc_315E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_31A8")

    #C0153
    ChrTalk(
        0xC,
        "……要去休息吗？\x02",
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0xC,
        (
            "请随意，\x01",
            "……不过不能保证舒适程度啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31A8")

    Jump("loc_2BF9")

    label("loc_31AD")

    TalkEnd(0xC)
    Return()

    # Function_12_2BEC end

    def Function_13_31B1(): pass

    label("Function_13_31B1")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3245")
    Jump("loc_328F")

    label("loc_3245")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3265")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_328F")

    label("loc_3265")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3285")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_328F")

    label("loc_3285")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_328F")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0155
    ChrTalk(
        0xFE,
        "（吧唧吧唧……）\x02",
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xFE,
        (
            "今天就在这悠闲地享受，\x01",
            "明天再搭班车回去吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_13_31B1 end

    def Function_14_3303(): pass

    label("Function_14_3303")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3397")
    Jump("loc_33E1")

    label("loc_3397")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_33B7")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_33E1")

    label("loc_33B7")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_33D7")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_33E1")

    label("loc_33D7")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_33E1")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0157
    ChrTalk(
        0xFE,
        (
            "能不能快点结束啊，\x01",
            "（吧唧吧唧……）已经吃完啦。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_14_3303 end

    def Function_15_3443(): pass

    label("Function_15_3443")

    TalkBegin(0xFE)

    #C0158
    ChrTalk(
        0xFE,
        (
            "哼，这就是唐古拉姆门吗……\x01",
            "守备比想象中要薄弱呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xFE,
        (
            "看来克洛斯贝尔\x01",
            "落入共和国手中\x01",
            "也只是时间问题而已。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_15_3443 end

    def Function_16_34B9(): pass

    label("Function_16_34B9")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_354D")
    Jump("loc_3597")

    label("loc_354D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_356D")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3597")

    label("loc_356D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_358D")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3597")

    label("loc_358D")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3597")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0160
    ChrTalk(
        0xFE,
        (
            "去克洛斯贝尔市的话，\x01",
            "好像乘坐导力巴士比较好哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xFE,
        (
            "巴士的搭乘处应该在外面……\x01",
            "肚子也填饱了，去看看吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_16_34B9 end

    def Function_17_3632(): pass

    label("Function_17_3632")

    TalkBegin(0xFE)

    #C0162
    ChrTalk(
        0xFE,
        (
            "开往克洛斯贝尔市\x01",
            "导力巴士\x01",
            "是从哪里发车来着？\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_17_3632 end

    def Function_18_366B(): pass

    label("Function_18_366B")

    TalkBegin(0xFE)

    #C0163
    ChrTalk(
        0xFE,
        (
            "哎～选择了一个不拥挤的日子\x01",
            "竟然也晚了很多。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xFE,
        (
            "真没办法。\x01",
            "赶快到街上\x01",
            "采购商品去吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0xFE,
        (
            "其实，比起做生意\x01",
            "去纪念庆典游玩比较有趣哦！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_18_366B end

    def Function_19_36FE(): pass

    label("Function_19_36FE")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3792")
    Jump("loc_37DC")

    label("loc_3792")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_37B2")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_37DC")

    label("loc_37B2")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_37D2")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_37DC")

    label("loc_37D2")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_37DC")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0166
    ChrTalk(
        0xFE,
        (
            "纪念庆典到明天就结束了……\x01",
            "到时肯定会非常挤，所以我决定今天就回去。\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0xFE,
        (
            "不过抱有同样想法的人\x01",
            "好像也有很多啊。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_19_36FE end

    def Function_20_387D(): pass

    label("Function_20_387D")

    TalkBegin(0xFE)

    #C0168
    ChrTalk(
        0xFE,
        (
            "我很急！\x01",
            "我说，动作快点！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_20_387D end

    def Function_21_38A3(): pass

    label("Function_21_38A3")

    TalkBegin(0xFE)

    #C0169
    ChrTalk(
        0xFE,
        "现场检查真是麻烦……\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_21_38A3 end

    def Function_22_38C4(): pass

    label("Function_22_38C4")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3958")
    Jump("loc_39A2")

    label("loc_3958")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3978")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_39A2")

    label("loc_3978")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3998")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_39A2")

    label("loc_3998")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_39A2")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0170
    ChrTalk(
        0xFE,
        (
            "巴士还没有来吗，\x01",
            "看来还要等上一个小时啊……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_22_38C4 end

    def Function_23_3A00(): pass

    label("Function_23_3A00")

    TalkBegin(0xFE)

    #C0171
    ChrTalk(
        0xFE,
        "早上很早就出发了，所以很困。\x02",
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0xFE,
        (
            "开车打瞌睡是绝对不行的，\x01",
            "所以暂且就在这里\x01",
            "小睡一会解解困意吧。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_23_3A00 end

    def Function_24_3A6D(): pass

    label("Function_24_3A6D")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3B01")
    Jump("loc_3B4B")

    label("loc_3B01")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3B21")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3B4B")

    label("loc_3B21")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3B41")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3B4B")

    label("loc_3B41")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3B4B")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0173
    ChrTalk(
        0xFE,
        "嗯……这里的食物竟然做得如此地道。\x02",
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0xFE,
        (
            "像这样的食堂通常应该是\x01",
            "价廉物不美才对……\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0xFE,
        "但这次似乎是个美好的意外呢。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_24_3A6D end

    def Function_25_3BF1(): pass

    label("Function_25_3BF1")

    TalkBegin(0xFE)

    #C0176
    ChrTalk(
        0xFE,
        "呵呵，真美味呢，老公。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_25_3BF1 end

    def Function_26_3C14(): pass

    label("Function_26_3C14")

    TalkBegin(0xFE)

    #C0177
    ChrTalk(
        0xFE,
        "我是来卖东方人街特产的。\x02",
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0xFE,
        (
            "东方风格的小物件\x01",
            "在别的地方很难买得到，\x01",
            "所以一定能大卖的～！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_26_3C14 end

    def Function_27_3C7B(): pass

    label("Function_27_3C7B")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3D0F")
    Jump("loc_3D59")

    label("loc_3D0F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3D2F")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3D59")

    label("loc_3D2F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3D4F")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3D59")

    label("loc_3D4F")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3D59")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E32")

    #C0179
    ChrTalk(
        0xFE,
        "（大吃特吃……狼吞虎咽……）\x02",
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0xFE,
        (
            "……虽然来到了克洛斯贝尔，\x01",
            "但我一点行程计划都没有。\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0xFE,
        (
            "要不要听从参加过纪念庆典的朋友的建议，\x01",
            "到阿尔摩利卡村去看一看呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_3E93")

    label("loc_3E32")


    #C0182
    ChrTalk(
        0xFE,
        (
            "那里的景色好像非常好……\x01",
            "要不要去看一看呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0xFE,
        (
            "……不不，\x01",
            "去矿山参观也不错。\x01",
            "唔嗯…………\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E93")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_27_3C7B end

    def Function_28_3E9B(): pass

    label("Function_28_3E9B")

    TalkBegin(0xFE)

    #C0184
    ChrTalk(
        0xFE,
        (
            "我趁着放长假的机会，带着老婆\x01",
            "来克洛斯贝尔市玩了一趟。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0xFE,
        (
            "高度现代化的克洛斯贝尔市和\x01",
            "基本保留自然原貌的其它地域……\x01",
            "确实值得一看啊。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_28_3E9B end

    def Function_29_3F2D(): pass

    label("Function_29_3F2D")

    TalkBegin(0xFE)

    #C0186
    ChrTalk(
        0xFE,
        (
            "虽说外观很华丽，\x01",
            "但只要稍微走进后巷里，\x01",
            "就会有种误入黑暗世界的感觉……\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xFE,
        (
            "我对克洛斯贝尔产生了\x01",
            "某种恐怖的感觉哦。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_29_3F2D end

    def Function_30_3FAD(): pass

    label("Function_30_3FAD")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4041")
    Jump("loc_408B")

    label("loc_4041")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4061")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_408B")

    label("loc_4061")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4081")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_408B")

    label("loc_4081")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_408B")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0188
    ChrTalk(
        0xFE,
        "放松一下，就当作是补吃早饭吧。\x02",
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0xFE,
        "嗯，吃什么好呢……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_30_3FAD end

    def Function_31_40F4(): pass

    label("Function_31_40F4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_4145")

    #C0190
    ChrTalk(
        0x22,
        (
            "#3600F我今天是来食堂\x01",
            "批售食材的。\x02\x03",

            "我得再\x01",
            "好好加把劲工作。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_41B5")

    label("loc_4145")


    #C0191
    ChrTalk(
        0x22,
        (
            "#3600F我今天是来食堂\x01",
            "批售食材的哦。\x02\x03",

            "#3604F嗯……让提马斯先生\x01",
            "久等也不太好。\x02\x03",

            "必须快点\x01",
            "将食材搬过去呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_41B5")

    TalkEnd(0xFE)
    Return()

    # Function_31_40F4 end

    def Function_32_41B9(): pass

    label("Function_32_41B9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_422C")

    #C0192
    ChrTalk(
        0xFE,
        "这个旅店的床还真是意外的舒服哦。\x02",
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0xFE,
        (
            "我至今为止住过无数旅店，\x01",
            "所以我的评价\x01",
            "是不会错的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_4255")

    label("loc_422C")


    #C0194
    ChrTalk(
        0xFE,
        (
            "虽然看上去简陋，\x01",
            "但实际相当松软……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4255")

    TalkEnd(0xFE)
    Return()

    # Function_32_41B9 end

    def Function_33_4259(): pass

    label("Function_33_4259")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_42ED")
    Jump("loc_4337")

    label("loc_42ED")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_430D")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4337")

    label("loc_430D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_432D")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4337")

    label("loc_432D")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4337")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_4550")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_44F7")

    #C0195
    ChrTalk(
        0x24,
        (
            "今天接到了要回共和国的\x01",
            "游客的委托哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x24,
        (
            "我刚才才在国境门前面的\x01",
            "『唐古拉姆丘陵』找回了\x01",
            "他丢失的钱包。\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0x101,
        (
            "#0005F……唔，\x01",
            "内容仅此而已吗？\x02\x03",

            "听起来像是\x01",
            "非常轻松的工作呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x25,
        "……但是，实际情况并非如此哦。\x02",
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0x25,
        (
            "共和国对『唐古拉姆丘陵』一带\x01",
            "提出了领土主张哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0x25,
        (
            "就算只是去寻找失物，\x01",
            "也要办理麻烦的许可申请才行。\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0x103,
        "#0200F管理相当严格呢。\x02",
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x24,
        (
            "哎，轻松的工作\x01",
            "哪有那么多。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_4550")

    label("loc_44F7")


    #C0203
    ChrTalk(
        0xFE,
        (
            "这项委托花了\x01",
            "很多时间。\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0xFE,
        (
            "所以其它委托就积压起来了，\x01",
            "必须早点回到\x01",
            "克洛斯贝尔市。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4550")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_33_4259 end

    def Function_34_4558(): pass

    label("Function_34_4558")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_45EC")
    Jump("loc_4636")

    label("loc_45EC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_460C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4636")

    label("loc_460C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_462C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4636")

    label("loc_462C")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4636")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_46C6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4676")
    Call(0, 33)
    Jump("loc_46C6")

    label("loc_4676")


    #C0205
    ChrTalk(
        0xFE,
        (
            "有关领土的问题，\x01",
            "帝国和共和国都是一步不让。\x01",
            "……这是身为警察所必须谨记的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_46C6")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_34_4558 end

    def Function_35_46CE(): pass

    label("Function_35_46CE")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4762")
    Jump("loc_47AC")

    label("loc_4762")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4782")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_47AC")

    label("loc_4782")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_47A2")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_47AC")

    label("loc_47A2")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_47AC")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_49C4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4909")

    #C0206
    ChrTalk(
        0xFE,
        "接下来要去共和国的游击士协会出差。\x02",
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0xFE,
        (
            "嗯嗯，因为工作地点是在故乡，\x01",
            "所以有些技痒了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0xFE,
        (
            "虽然有活力十足的后辈\x01",
            "加入进来很有趣啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0x101,
        (
            "#0009F哈哈……林小姐即使对后辈\x01",
            "似乎也不会放松要求呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0xFE,
        (
            "当然，\x01",
            "工作又不是在\x01",
            "做游戏。\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0xFE,
        (
            "我在武术修行时，\x01",
            "也得到了优秀前辈们\x01",
            "的严格指导。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_49C4")

    label("loc_4909")


    #C0212
    ChrTalk(
        0xFE,
        (
            "我们所要去的协会可是个\x01",
            "有点复杂的地方。\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0xFE,
        (
            "如果乘导力列车的话需要换乘，\x01",
            "但乘坐导力巴士就可以直达。\x01",
            "因此这条线路能更快到达。\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0xFE,
        (
            "有时候坐巴士可能比\x01",
            "坐导力列车更快，\x01",
            "要记住这点哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_49C4")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_35_46CE end

    def Function_36_49CC(): pass

    label("Function_36_49CC")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4A60")
    Jump("loc_4AAA")

    label("loc_4A60")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4A80")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4AAA")

    label("loc_4A80")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4AA0")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4AAA")

    label("loc_4AA0")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4AAA")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_4C44")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4BDB")

    #C0215
    ChrTalk(
        0xFE,
        (
            "林得到了共和国古武术\x01",
            "『泰斗流』的真传，\x01",
            "是个武术高手。\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0xFE,
        (
            "如果要说徒手格斗术，\x01",
            "那么她的实力在克洛斯贝尔的协会\x01",
            "里也是数一数二的。\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0x104,
        (
            "#0305F我听说共和国的高级游击士\x01",
            "用的就是\x01",
            "这种名称的武术。\x02\x03",

            "#0304F难怪她的一举一动都\x01",
            "让人无机可乘呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_4C44")

    label("loc_4BDB")


    #C0218
    ChrTalk(
        0xFE,
        (
            "因为这次工作地点\x01",
            "是在共和国，所以\x01",
            "林她干劲十足哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0xFE,
        (
            "呵呵，如果太过严格，\x01",
            "可是会把人家吓坏的哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C44")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_36_49CC end

    def Function_37_4C4C(): pass

    label("Function_37_4C4C")

    TalkBegin(0xFE)

    #C0220
    ChrTalk(
        0x29,
        (
            "#0500F开往克洛斯贝尔的巴士就在\x01",
            "门外的停车场里。\x02\x03",

            "#0501F我只能帮到这里了……\x01",
            "各位，祝你们好运！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_37_4C4C end

    def Function_38_4CB7(): pass

    label("Function_38_4CB7")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4D4B")
    Jump("loc_4D95")

    label("loc_4D4B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4D6B")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4D95")

    label("loc_4D6B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4D8B")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4D95")

    label("loc_4D8B")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4D95")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0x5)"), scpexpr(EXPR_END)), "loc_4E85")

    #C0221
    ChrTalk(
        0x2A,
        (
            "#3404F我来克洛斯贝尔的目的……\x01",
            "一定要说的话，就是为了\x01",
            "寻找宝石。\x02\x03",

            "#3400F只要得到那颗宝石，\x01",
            "就能将共和国国民卷入\x01",
            "狂热的漩涡。\x02\x03",

            "#3402F但是，必须要\x01",
            "想尽一切办法……才能将它弄到手哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5132")

    label("loc_4E85")


    #C0222
    ChrTalk(
        0x104,
        "#0305F（哦哦……有美女……！）\x02",
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0x2A,
        (
            "#3405F……哎呀。\x02\x03",

            "#3400F你们几个……\x01",
            "似乎并不是乘坐那辆巴士而来的人嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0x101,
        (
            "#0005F……啊！？\x02\x03",

            "#0012F呃，这个……\x01",
            "我们昨天夜里很晚才到，\x01",
            "所以就在这里投宿了一晚。\x02\x03",

            "#0006F（就、就先这么说吧……）\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x2A,
        (
            "#3404F呵呵……是吗？\x02\x03",

            "#3400F算啦，仔细想想，\x01",
            "这种情况也并没有\x01",
            "那么少见呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0x104,
        (
            "#0309F这位姐姐，您来克洛斯贝尔\x01",
            "是做什么的呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0x2A,
        (
            "#3404F一定要说的话……\x01",
            "是来寻找宝石的。\x02",
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
            "#3400F嗯，为了搜寻沉睡于克洛斯贝尔的，\x01",
            "具有魔性的宝石。\x02\x03",

            "#3404F只要得到那颗宝石，\x01",
            "就能将共和国国民卷入\x01",
            "狂热的漩涡。\x02\x03",

            "#3402F但是，必须要\x01",
            "想尽一切的办法……才能将它弄到手哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0x101,
        "#0005F（……这个人……？）\x02",
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0x2A,
        "#3404F呵呵，你们不用想太多哦。\x02",
    )

    CloseMessageWindow()
    OP_29(0x1B, 0x1, 0x5)

    label("loc_5132")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_38_4CB7 end

    def Function_39_513A(): pass

    label("Function_39_513A")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_51CE")
    Jump("loc_5218")

    label("loc_51CE")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_51EE")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5218")

    label("loc_51EE")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_520E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5218")

    label("loc_520E")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5218")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0x6)"), scpexpr(EXPR_END)), "loc_52F1")

    #C0232
    ChrTalk(
        0xFE,
        (
            "我大概都已经有三年\x01",
            "没来过克洛斯贝尔了。\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0xFE,
        (
            "呵呵，真是期待能\x01",
            "再次见到孙子啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0xFE,
        (
            "和小孙子在米修拉姆\x01",
            "的主题公园游玩的那天，\x01",
            "犹如昨天的事一样浮现在脑海……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5511")

    label("loc_52F1")


    #C0235
    ChrTalk(
        0xFE,
        (
            "哎呀呀……\x01",
            "那个小男孩真是很可爱啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0xFE,
        (
            "和我的孙子一模一样，\x01",
            "看上去很机灵。\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0x101,
        (
            "#0000F那个……老婆婆，\x01",
            "您是克洛斯贝尔人吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0xFE,
        "不是不是，我是共和国人。\x02",
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0xFE,
        (
            "儿子儿媳住在\x01",
            "克洛斯贝尔市里，\x01",
            "所以趁着这场纪念庆典就过来玩了。\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0xFE,
        (
            "我大概都已经有三年\x01",
            "没来过克洛斯贝尔了。\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x102,
        (
            "#0102F呵呵……\x01",
            "老婆婆，您看上去好像很开心呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0xFE,
        "呵呵……那是当然。\x02",
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0xFE,
        (
            "毕竟我和孙子已经\x01",
            "很久没有见过面了。\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0xFE,
        (
            "上次来的时候，还带孙子去米修拉姆\x01",
            "的主题公园玩过呢……\x01",
            "那就像是昨天才发生的事情一样。\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0xFE,
        (
            "与那时相比，不知道\x01",
            "他长大了多少呢……\x01",
            "真的好期待啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x1B, 0x1, 0x6)

    label("loc_5511")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_39_513A end

    def Function_40_5519(): pass

    label("Function_40_5519")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0x7)"), scpexpr(EXPR_END)), "loc_5583")

    #C0246
    ChrTalk(
        0xFE,
        (
            "……我来\x01",
            "克洛斯贝尔\x01",
            "只是为了钓鱼。\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0xFE,
        (
            "绝不会是其它理由。\x01",
            "……明白了就快走吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5894")

    label("loc_5583")


    #C0248
    ChrTalk(
        0xFE,
        "……有什么事啊？\x02",
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x101,
        (
            "#0006F（这位老爷爷似乎有点乖僻呢……）\x02\x03",

            "#0000F那、那个……\x01",
            "老爷爷，您来克洛斯贝尔是做什么的啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0xFE,
        "……为什么要问这种问题？\x02",
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x101,
        (
            "#0006F不、不是的，那个……\x01",
            "只是单纯的好奇……\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0x104,
        (
            "#0300F难道老爷爷来这里\x01",
            "是有不可告人的事？\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0xFE,
        "你、你说什么……！\x02",
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0x101,
        "#0005F喂……兰迪！？\x02",
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x104,
        (
            "#0304F说实话，我也是为了这个而来的。\x02\x03",

            "#0300F克洛斯贝尔是个好地方，\x01",
            "可爱的女孩子到处都是，\x01",
            "而且也有很多满是女孩子的好玩夜店哦。\x02\x03",

            "#0309F呀～我和老爷爷真投缘！\x01",
            "要不您给我介绍一些\x01",
            "中意的店吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0xFE,
        (
            "谁、谁、谁会去那种伤风败俗\x01",
            "的店啊！！\x02",
        )
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0xFE,
        "……是钓鱼，钓鱼！！\x02",
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0xFE,
        (
            "为了克洛斯贝尔的淡水鱼，\x01",
            "我才赶在热闹的纪念庆典期间\x01",
            "孤身一人来这里的！！\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0xFE,
        "不行吗？！可恶的小鬼！！\x02",
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0x104,
        (
            "#0309F……哈哈，这也不错哦。\x01",
            "抱歉开了您玩笑啊，老爷爷。\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0x101,
        "#0006F（他的奸计奏效了呢……）\x02",
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0xFE,
        "哼！\x02",
    )

    CloseMessageWindow()
    OP_29(0x1B, 0x1, 0x7)

    label("loc_5894")

    TalkEnd(0xFE)
    Return()

    # Function_40_5519 end

    def Function_41_5898(): pass

    label("Function_41_5898")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_5936")

    #C0263
    ChrTalk(
        0xFE,
        (
            "我是来贩卖共和国\x01",
            "的稀有杂货的行商。\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0xFE,
        (
            "由于在各国都有不少熟人，\x01",
            "所以谈起生意也意外地顺利。\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0xFE,
        (
            "如果方便的话，也请各位\x01",
            "多多惠顾。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5AE8")

    label("loc_5936")


    #C0266
    ChrTalk(
        0xFE,
        (
            "呀，哈哈哈哈。\x01",
            "巴士等得人好心急啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0xFE,
        (
            "听说克洛斯贝尔是个很繁荣的地方，\x01",
            "接下来真是令人期待啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0x101,
        (
            "#0005F……咦，您好像\x01",
            "是个生意人吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0xFE,
        (
            "嗯，我是来贩卖共和国\x01",
            "的稀有杂货的行商。\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0xFE,
        (
            "顺便采购克洛斯贝尔特有的\x01",
            "小商品，\x01",
            "再拿到共和国去卖。\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0x103,
        (
            "#0205F个体贸易商吗……\x01",
            "想必很辛苦吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0xFE,
        (
            "不不，别看我这样，\x01",
            "人脉也是相当广的。\x02",
        )
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0xFE,
        (
            "由于在各国都有不少熟人，\x01",
            "所以谈起生意也意外地顺利。\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0xFE,
        (
            "如果方便的话，也请各位\x01",
            "多多惠顾。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x1B, 0x1, 0x8)

    label("loc_5AE8")

    TalkEnd(0xFE)
    Return()

    # Function_41_5898 end

    def Function_42_5AEC(): pass

    label("Function_42_5AEC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0x9)"), scpexpr(EXPR_END)), "loc_5B9F")

    #C0275
    ChrTalk(
        0xFE,
        (
            "我之前一直都在共和国旅行，\x01",
            "如今正赶上纪念庆典，就回来一趟。\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0xFE,
        (
            "不过，我的事并不重要，\x01",
            "不是吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0xFE,
        (
            "你也要乘坐巴士的话，\x01",
            "小心一下那个黑发女人\x01",
            "比较好。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5E32")

    label("loc_5B9F")


    #C0278
    ChrTalk(
        0xFE,
        (
            "我说……你不觉得\x01",
            "那位姐姐很奇怪吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0x101,
        (
            "#0005F咦……？\x01",
            "那位姐姐？你是指……\x02",
        )
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0xFE,
        (
            "看，就是坐在对面的那个\x01",
            "黑头发、穿西裤套装的人。\x02",
        )
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0xFE,
        (
            "我在旅客巴士中也见到过她，\x01",
            "总觉得\x01",
            "她有些奇怪呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0xFE,
        (
            "该说是过于沉着吗，\x01",
            "总觉得不是个普通人。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0x5)"), scpexpr(EXPR_END)), "loc_5D00")

    #C0283
    ChrTalk(
        0x102,
        (
            "#0103F嗯……确实是，\x01",
            "看起来的确\x01",
            "不像是普通人。\x02\x03",

            "#0100F……话说回来，\x01",
            "您是来克洛斯贝尔观光的吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5D69")

    label("loc_5D00")


    #C0284
    ChrTalk(
        0x102,
        (
            "#0103F嗯……\x01",
            "不和她聊聊看的话，\x01",
            "便无法做出判断呢。\x02\x03",

            "#0100F……话说回来，\x01",
            "您是来克洛斯贝尔观光的吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5D69")


    #C0285
    ChrTalk(
        0xFE,
        (
            "嗯，硬要说的话，\x01",
            "算是回故乡吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0xFE,
        (
            "我之前一直都在共和国旅行，\x01",
            "如今正赶上纪念庆典，就回来一趟。\x02",
        )
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0xFE,
        (
            "……话说，我的事并不重要，\x01",
            "不是吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0xFE,
        (
            "如果你们也乘坐巴士，\x01",
            "一定要注意一下\x01",
            "那个人哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x1B, 0x1, 0x9)

    label("loc_5E32")

    TalkEnd(0xFE)
    Return()

    # Function_42_5AEC end

    def Function_43_5E36(): pass

    label("Function_43_5E36")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5ECA")
    Jump("loc_5F14")

    label("loc_5ECA")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5EEA")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5F14")

    label("loc_5EEA")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5F0A")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5F14")

    label("loc_5F0A")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5F14")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0xA)"), scpexpr(EXPR_END)), "loc_5FA1")

    #C0289
    ChrTalk(
        0xFE,
        (
            "我们是兄妹，\x01",
            "不过长得不太像吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0xFE,
        (
            "我们都喜欢旅行，\x01",
            "所以经常两个人一起出去玩。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_61EE")

    label("loc_5FA1")


    #C0291
    ChrTalk(
        0x2F,
        (
            "啊，各位好，\x01",
            "你们也要去\x01",
            "克洛斯贝尔市吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0x101,
        (
            "#0000F嗯，算是吧。\x02\x03",

            "#0005F请问……\x01",
            "两位是情侣一起旅行么？\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0x2F,
        (
            "噗……\x01",
            "果然看起来像是那样吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0x103,
        "#0205F啊？不是吗？\x02",
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0x30,
        (
            "……啊哈哈，不是哦。\x01",
            "不是不是。\x02",
        )
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0x30,
        "我们两个虽然看上去不像，但确实是兄妹哦。\x02",
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0x2F,
        (
            "因为长得完全不像，\x01",
            "所以经常被人误会呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0x2F,
        (
            "我们都喜欢旅行，\x01",
            "所以经常两个人一起出去玩。\x02",
        )
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0x101,
        "#0000F呵……两位关系很好呢。\x02",
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0x2F,
        (
            "那是啊，为了陪这个没有男朋友的妹妹，\x01",
            "我可是竭尽了全力啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0x30,
        (
            "哟，你还好意思说。\x01",
            "哥哥不也经常被母亲\x01",
            "念叨赶紧交个女朋友吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0x2F,
        "哈哈……哎，就是这么回事。\x02",
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0x2F,
        (
            "希望我们都能\x01",
            "好好享受这次纪念庆典啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x1B, 0x1, 0xA)

    label("loc_61EE")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_43_5E36 end

    def Function_44_61F6(): pass

    label("Function_44_61F6")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_628A")
    Jump("loc_62D4")

    label("loc_628A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_62AA")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_62D4")

    label("loc_62AA")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_62CA")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_62D4")

    label("loc_62CA")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_62D4")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0xA)"), scpexpr(EXPR_END)), "loc_636D")

    #C0304
    ChrTalk(
        0xFE,
        (
            "被误认为情侣这种情况，\x01",
            "也不知道发生过多少次了。\x02",
        )
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0xFE,
        (
            "嗯，希望我们都能\x01",
            "好好享受这次纪念庆典。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6370")

    label("loc_636D")

    Call(0, 43)

    label("loc_6370")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_44_61F6 end

    def Function_45_6378(): pass

    label("Function_45_6378")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_640C")
    Jump("loc_6456")

    label("loc_640C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_642C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6456")

    label("loc_642C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_644C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6456")

    label("loc_644C")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6456")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0xB)"), scpexpr(EXPR_END)), "loc_6506")

    #C0306
    ChrTalk(
        0xFE,
        "今天我们父子出来旅行。\x02",
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0xFE,
        (
            "因为我平时经常出差，\x01",
            "所以偶尔也想尽一点\x01",
            "身为父亲应尽的责任……\x02",
        )
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0xFE,
        (
            "仅此而已，\x01",
            "哇哈哈。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6655")

    label("loc_6506")


    #C0309
    ChrTalk(
        0xFE,
        (
            "乘坐巴士旅行\x01",
            "也别有情趣哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0xFE,
        "孩子好像也很开心。\x02",
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0x101,
        "#0000F您是带孩子出来旅行的吗？\x02",
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0xFE,
        "嗯，是啊。\x02",
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0xFE,
        (
            "所以就想和平时给予我支持的儿子\x01",
            "一起好好玩一下。\x02",
        )
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0x102,
        "#0102F呵呵……真是个好父亲呢。\x02",
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0xFE,
        "哎呀，小姐你说得我都不好意思了呢。\x02",
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0xFE,
        (
            "因为平时经常出差，\x01",
            "所以偶尔也想尽一点\x01",
            "身为父亲应尽的责任……\x02",
        )
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0xFE,
        (
            "仅此而已，\x01",
            "哇哈哈。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x1B, 0x1, 0xB)

    label("loc_6655")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_45_6378 end

    def Function_46_665D(): pass

    label("Function_46_665D")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_66F1")
    Jump("loc_673B")

    label("loc_66F1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6711")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_673B")

    label("loc_6711")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6731")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_673B")

    label("loc_6731")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_673B")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0xC)"), scpexpr(EXPR_END)), "loc_67AC")

    #C0318
    ChrTalk(
        0xFE,
        (
            "爸爸经常到各个国家\x01",
            "出差，总会给我讲\x01",
            "很多好玩的事情。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6813")

    label("loc_67AC")


    #C0319
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔的景色真美啊，\x01",
            "好开心！\x02",
        )
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0xFE,
        (
            "爸爸经常到各个国家\x01",
            "出差，总会给我讲\x01",
            "很多好玩的事情。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x1B, 0x1, 0xC)

    label("loc_6813")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_46_665D end

    def Function_47_681B(): pass

    label("Function_47_681B")

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

    def lambda_6AA5():
        OP_98(0xFE, 0xFFFFD120, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_6AA5)
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

    def lambda_6B3C():
        OP_98(0xFE, 0xFFFFADF8, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_6B3C)
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

    def lambda_6BB4():
        OP_95(0x2D, -60, 0, -3600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_6BB4)

    def lambda_6BCE():
        OP_A7(0x2D, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2D, 2, lambda_6BCE)
    WaitChrThread(0x2D, 1)
    WaitChrThread(0x2D, 2)

    #C0321
    ChrTalk(
        0x29,
        (
            "#0503F欢迎来到\x01",
            "克洛斯贝尔自治州，\x01",
            "长途旅行辛苦了。\x02\x03",

            "#0500F前往克洛斯贝尔市的巴士\x01",
            "过一段时间才会抵达。\x02\x03",

            "各位如果愿意，就请先到食堂\x01",
            "稍作休息吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0x2D,
        "#5P嗯，那就不客气了。\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x29, 3, 0, 52)

    def lambda_6C9C():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2D, 2, lambda_6C9C)
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

    def lambda_6E02():
        OP_95(0xFE, 0, 0, 13900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_6E02)
    FadeToBright(500, 0)
    OP_0D()

    def lambda_6E26():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x5DC)
        ExitThread()

    QueueWorkItem(0x2A, 2, lambda_6E26)
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
        "#0301F……所有乘客都已经进去了吗？\x02",
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

    def lambda_6EDD():
        OP_98(0xFE, 0xFFFFFC18, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_6EDD)
    WaitChrThread(0x29, 1)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)

    #C0324
    ChrTalk(
        0x29,
        (
            "#11P#0501F嗯，全员都进去了。\x02\x03",

            "这是乘客名单，\x01",
            "请过目。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6F46():
        OP_98(0xFE, 0xFFFFFC18, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_6F46)
    WaitChrThread(0x29, 1)
    SetChrName("")

    #A0325
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "从诺艾尔处接过乘客名单。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0326
    ChrTalk(
        0x101,
        (
            "#5P#0000F嗯，谢谢。\x01",
            "这很有帮助。\x02\x03",

            "#0003F乘客总共九人吗……\x01",
            "应该都是从共和国\x01",
            "过来的。\x02",
        )
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0x103,
        (
            "#0200F……这个东西，\x01",
            "可以让外人看吗？\x02\x03",

            "严格地说，这种行为其实\x01",
            "相当于泄露个人信息呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0x29,
        (
            "#11P#0500F索妮亚副司令说，\x01",
            "要尽量将有利于调查的情报\x01",
            "传达给各位。\x02\x03",

            "#0503F她说过『又不是知道\x01",
            "姓名和住址，也算不上是\x01",
            "泄露信息』。\x02",
        )
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0x102,
        (
            "#6P#0104F根据现场情况进行灵活的判断……\x01",
            "不愧是副司令。\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0x104,
        (
            "#6P#0306F嗯……怎么说呢，\x01",
            "真是个可怕的人。\x02",
        )
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0x101,
        (
            "#5P#0003F……嗯，谢谢了，上士。\x01",
            "这份名单还给你。\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0332
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "把乘客名单还给了诺艾尔。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    def lambda_718A():
        OP_98(0xFE, 0x3E8, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_718A)
    WaitChrThread(0x29, 1)

    #C0333
    ChrTalk(
        0x29,
        (
            "#11P#0503F好的，确认归还。\x02\x03",

            "#0501F那么……觉得如何？\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0x101,
        (
            "#5P#0003F嗯……果然还是需要\x01",
            "通过亲眼确认来下最终判断。\x02",
        )
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0x102,
        (
            "#6P#0101F……所以，事不宜迟。\x02\x03",

            "在前往克洛斯贝尔的巴士抵达之前，\x01",
            "已经没有多少时间了。\x02\x03",

            "我们这就去询问食堂里的乘客们，\x01",
            "找出其中的假货贩子吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0x101,
        "#5P#0001F嗯……行动起来吧，各位！\x02",
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0x104,
        "#6P#0300F好！\x02",
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0x103,
        "#6P#0200F明白。\x02",
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0x29,
        "#11P#0501F各位……祝你们好运！\x02",
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

    # Function_47_681B end

    def Function_48_73E5(): pass

    label("Function_48_73E5")


    def lambda_73EA():
        OP_95(0xFE, -1500, 0, 9500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_73EA)
    WaitChrThread(0x101, 1)
    Return()

    # Function_48_73E5 end

    def Function_49_7404(): pass

    label("Function_49_7404")


    def lambda_7409():
        OP_95(0xFE, -1500, 0, 8000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7409)
    WaitChrThread(0x102, 1)
    Return()

    # Function_49_7404 end

    def Function_50_7423(): pass

    label("Function_50_7423")


    def lambda_7428():
        OP_95(0xFE, -3000, 0, 9500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7428)
    WaitChrThread(0x103, 1)
    Return()

    # Function_50_7423 end

    def Function_51_7442(): pass

    label("Function_51_7442")


    def lambda_7447():
        OP_95(0xFE, -3000, 0, 8000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7447)
    WaitChrThread(0x104, 1)
    Return()

    # Function_51_7442 end

    def Function_52_7461(): pass

    label("Function_52_7461")


    def lambda_7466():
        OP_95(0xFE, -5000, 0, -5000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7466)
    WaitChrThread(0xFE, 1)

    def lambda_7484():
        OP_95(0xFE, -5000, 0, -3600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7484)
    WaitChrThread(0xFE, 1)

    def lambda_74A2():
        OP_95(0xFE, -5000, 0, 30, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_74A2)
    WaitChrThread(0xFE, 1)

    def lambda_74C0():
        OP_95(0xFE, -5000, 0, 3300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_74C0)
    WaitChrThread(0xFE, 1)

    def lambda_74DE():
        OP_95(0xFE, 440, 0, 3300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_74DE)
    WaitChrThread(0xFE, 1)

    def lambda_74FC():
        OP_95(0xFE, 440, 0, 8900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_74FC)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_52_7461 end

    def Function_53_7516(): pass

    label("Function_53_7516")


    def lambda_751B():
        OP_95(0xFE, -60, 0, -3600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_751B)

    def lambda_7535():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_7535)
    WaitChrThread(0xFE, 1)

    def lambda_754A():
        OP_95(0xFE, -5000, 0, -3600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_754A)
    WaitChrThread(0xFE, 1)

    def lambda_7568():
        OP_95(0xFE, -5000, 0, 30, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7568)
    WaitChrThread(0xFE, 1)

    def lambda_7586():
        OP_95(0xFE, -5000, 0, 3300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7586)
    WaitChrThread(0xFE, 1)

    def lambda_75A4():
        OP_95(0xFE, 440, 0, 3300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_75A4)
    WaitChrThread(0xFE, 1)

    def lambda_75C2():
        OP_95(0xFE, 440, 0, 8900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_75C2)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_53_7516 end

    def Function_54_75E0(): pass

    label("Function_54_75E0")

    Sleep(900)

    def lambda_75E8():
        OP_95(0xFE, -5000, 0, -3600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_75E8)
    WaitChrThread(0xFE, 1)

    def lambda_7606():
        OP_95(0xFE, -5000, 0, 30, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7606)
    WaitChrThread(0xFE, 1)

    def lambda_7624():
        OP_95(0xFE, -5000, 0, 3300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7624)
    WaitChrThread(0xFE, 1)

    def lambda_7642():
        OP_95(0xFE, 440, 0, 3300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7642)
    WaitChrThread(0xFE, 1)

    def lambda_7660():
        OP_95(0xFE, 440, 0, 8900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7660)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_54_75E0 end

    def Function_55_767E(): pass

    label("Function_55_767E")


    def lambda_7683():
        OP_95(0xFE, -60, 0, -3600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7683)

    def lambda_769D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_769D)
    WaitChrThread(0xFE, 1)

    def lambda_76B2():
        OP_95(0xFE, -5000, 0, -3600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_76B2)
    WaitChrThread(0xFE, 1)

    def lambda_76D0():
        OP_95(0xFE, -5000, 0, 1150, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_76D0)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_55_767E end

    def Function_56_76EE(): pass

    label("Function_56_76EE")

    ClearChrFlags(0x2A, 0x80)
    SetChrChipByIndex(0x2A, 0x1F)
    SetChrSubChip(0x2A, 0x0)
    SetChrPos(0x2A, 100990, 0, -4180, 270)
    ClearChrFlags(0x2B, 0x80)
    SetChrChipByIndex(0x2B, 0x20)
    SetChrSubChip(0x2B, 0x0)
    SetChrPos(0x2B, 93290, 150, 2510, 90)
    ClearChrFlags(0x2F, 0x80)
    SetChrChipByIndex(0x2F, 0x5)
    SetChrSubChip(0x2F, 0x0)
    SetChrPos(0x2F, 100760, 100, 3970, 90)
    ClearChrFlags(0x30, 0x80)
    SetChrChipByIndex(0x30, 0x21)
    SetChrSubChip(0x30, 0x0)
    SetChrPos(0x30, 102900, 150, 3710, 270)
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

    # Function_56_76EE end

    def Function_57_77F7(): pass

    label("Function_57_77F7")

    Return()

    # Function_57_77F7 end

    def Function_58_77F8(): pass

    label("Function_58_77F8")

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

    def lambda_78B2():
        OP_95(0xFE, 95610, 0, -6230, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_78B2)

    def lambda_78CC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x29, 2, lambda_78CC)
    WaitChrThread(0x29, 1)
    WaitChrThread(0x29, 2)

    #C0340
    ChrTalk(
        0x29,
        (
            "#0500F各位旅客，前往克洛斯贝尔\x01",
            "的巴士刚刚已经\x01",
            "抵达了。\x02\x03",

            "请各位乘客前往停车场\x01",
            "方向。\x02",
        )
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0x30,
        (
            "#12P巴士已经来了呢。\x01",
            "哥哥，我们走吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0x2F,
        "#6P哦，是啊。\x02",
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0x2B,
        (
            "#6P呵呵，终于可以去和我孙子\x01",
            "见面了。\x02",
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
        "#12P#0501F……结果怎么样了？\x02",
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0x103,
        (
            "#5P#0200F……由于情报不足，\x01",
            "所以还没法确定谁是假货贩子。\x02",
        )
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0x104,
        (
            "#5P#0301F现在只能看出，\x01",
            "这里每个人都因为纪念庆典\x01",
            "而相当兴奋。\x02\x03",

            "#0306F话说回来，在那里面真的有\x01",
            "那种坏人吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0x101,
        "#5P#0003F…………………………\x02",
    )

    CloseMessageWindow()

    def lambda_7CE0():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7CE0)
    WaitChrThread(0x102, 1)

    #C0348
    ChrTalk(
        0x102,
        (
            "#5P#0105F……罗伊德，莫非……\x01",
            "你注意到了什么？\x02",
        )
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0x101,
        (
            "#11P#0001F……是啊，我觉得有个人的回答\x01",
            "很可疑。\x02",
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
            "#5P#0305F喂喂，真的假的！？\x01",
            "到底是怎么一回事……\x02",
        )
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0x101,
        (
            "#11P#0003F但也就是令人觉得有些\x01",
            "在意的程度。\x02\x03",

            "#0001F让我们在巴士里\x01",
            "将线索再整理一下吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0352
    ChrTalk(
        0x103,
        (
            "#5P#0200F那样的话，\x01",
            "就必须得快些了。\x02\x03",

            "一旦到达克洛斯贝尔市，\x01",
            "游客们下车分散后，\x01",
            "就很难找到他们了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7EB7():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7EB7)
    WaitChrThread(0x102, 1)

    #C0353
    ChrTalk(
        0x102,
        (
            "#5P#0101F嗯，我们快点前往\x01",
            "巴士停靠站吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0354
    ChrTalk(
        0x29,
        (
            "#12P#0501F前往克洛斯贝尔的巴士就在\x01",
            "门口的停车场。\x02\x03",

            "#0503F我只能帮到这里了……\x01",
            "祝各位好运！\x02",
        )
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0x101,
        "#5P#0000F嗯……谢谢你，诺艾尔上士。\x02",
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

    # Function_58_77F8 end

    def Function_59_7FD8(): pass

    label("Function_59_7FD8")


    def lambda_7FDD():
        OP_95(0xFE, -1500, 0, 9500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7FDD)
    WaitChrThread(0x101, 1)
    Return()

    # Function_59_7FD8 end

    def Function_60_7FF7(): pass

    label("Function_60_7FF7")


    def lambda_7FFC():
        OP_95(0xFE, -1500, 0, 8000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7FFC)
    WaitChrThread(0x102, 1)
    Return()

    # Function_60_7FF7 end

    def Function_61_8016(): pass

    label("Function_61_8016")


    def lambda_801B():
        OP_95(0xFE, -3000, 0, 9500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_801B)
    WaitChrThread(0x103, 1)
    Return()

    # Function_61_8016 end

    def Function_62_8035(): pass

    label("Function_62_8035")


    def lambda_803A():
        OP_95(0xFE, -3000, 0, 8000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_803A)
    WaitChrThread(0x104, 1)
    Return()

    # Function_62_8035 end

    def Function_63_8054(): pass

    label("Function_63_8054")


    def lambda_8059():
        OP_95(0xFE, 93970, 0, -5720, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_8059)
    WaitChrThread(0x29, 1)

    def lambda_8077():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_8077)
    WaitChrThread(0x29, 1)
    Return()

    # Function_63_8054 end

    def Function_64_8084(): pass

    label("Function_64_8084")


    def lambda_8089():
        OP_95(0xFE, 100730, 0, -6040, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8089)
    WaitChrThread(0xFE, 1)

    def lambda_80A7():
        OP_95(0xFE, 95850, 0, -6040, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_80A7)
    WaitChrThread(0xFE, 1)

    def lambda_80C5():
        OP_95(0xFE, 95850, 0, -9890, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_80C5)

    def lambda_80DF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_80DF)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_64_8084 end

    def Function_65_80F0(): pass

    label("Function_65_80F0")

    Sleep(2000)

    def lambda_80F8():
        OP_95(0xFE, 95850, 0, -6040, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_80F8)
    WaitChrThread(0xFE, 1)

    def lambda_8116():
        OP_95(0xFE, 95850, 0, -9890, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8116)

    def lambda_8130():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_8130)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_65_80F0 end

    def Function_66_8141(): pass

    label("Function_66_8141")


    def lambda_8146():
        OP_95(0xFE, 92920, 0, -3460, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8146)
    WaitChrThread(0xFE, 1)

    def lambda_8164():
        OP_95(0xFE, 95850, 0, -3460, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8164)
    WaitChrThread(0xFE, 1)

    def lambda_8182():
        OP_95(0xFE, 95850, 0, -9890, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8182)
    Sleep(2000)

    def lambda_819F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_819F)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_66_8141 end

    def Function_67_81B0(): pass

    label("Function_67_81B0")


    def lambda_81B5():
        OP_95(0xFE, 97290, 0, 4720, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_81B5)
    WaitChrThread(0xFE, 1)

    def lambda_81D3():
        OP_95(0xFE, 95850, 0, -9890, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_81D3)
    Sleep(6000)

    def lambda_81F0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_81F0)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_67_81B0 end

    def Function_68_8201(): pass

    label("Function_68_8201")


    def lambda_8206():
        OP_95(0xFE, 99180, 0, -330, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8206)
    WaitChrThread(0xFE, 1)

    def lambda_8224():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8224)
    WaitChrThread(0xFE, 1)
    Sleep(1000)

    def lambda_8238():
        OP_93(0xFE, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8238)
    WaitChrThread(0xFE, 1)

    def lambda_8249():
        OP_95(0xFE, 95850, 0, -330, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8249)
    WaitChrThread(0xFE, 1)

    def lambda_8267():
        OP_95(0xFE, 95850, 0, -9890, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8267)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_68_8201 end

    def Function_69_8281(): pass

    label("Function_69_8281")


    def lambda_8286():
        OP_95(0xFE, 104160, 0, -330, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8286)
    WaitChrThread(0xFE, 1)

    def lambda_82A4():
        OP_95(0xFE, 95850, 0, -330, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_82A4)
    WaitChrThread(0xFE, 1)

    def lambda_82C2():
        OP_95(0xFE, 95850, 0, -9890, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_82C2)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_69_8281 end

    def Function_70_82DC(): pass

    label("Function_70_82DC")

    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)

    def lambda_82EC():
        OP_95(0xFE, 95850, 0, -9890, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_82EC)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_70_82DC end

    def Function_71_8306(): pass

    label("Function_71_8306")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_8338")

    #C0356
    ChrTalk(
        0x101,
        "#0001F趁现在与乘客们交谈吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_8394")

    label("loc_8338")


    #C0357
    ChrTalk(
        0x101,
        (
            "#0001F在前往克洛斯贝尔的巴士抵达之前，\x01",
            "已经没有多少时间了。\x02\x03",

            "趁现在与乘客们交谈吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)

    label("loc_8394")

    SetChrPos(0x0, 95790, 0, -5540, 0)
    EventEnd(0x5)
    Return()

    # Function_71_8306 end

    def Function_72_83A8(): pass

    label("Function_72_83A8")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_83DA")

    #C0358
    ChrTalk(
        0x101,
        "#0001F趁现在与乘客们交谈吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_8436")

    label("loc_83DA")


    #C0359
    ChrTalk(
        0x101,
        (
            "#0001F在前往克洛斯贝尔的巴士抵达之前，\x01",
            "已经没有多少时间了。\x02\x03",

            "趁现在与乘客们交谈吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)

    label("loc_8436")

    SetChrPos(0x0, 92410, 0, -50, 90)
    EventEnd(0x5)
    Return()

    # Function_72_83A8 end

    def Function_73_844A(): pass

    label("Function_73_844A")

    EventBegin(0x0)

    #C0360
    ChrTalk(
        0x101,
        (
            "#0003F前往克洛斯贝尔的巴士马上就要发车了……\x01",
            "快点到巴士停靠站去吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -8140, 0, 8140, 180)
    EventEnd(0x5)
    Return()

    # Function_73_844A end

    def Function_74_84A9(): pass

    label("Function_74_84A9")

    EventBegin(0x0)

    #C0361
    ChrTalk(
        0x101,
        (
            "#0003F前往克洛斯贝尔的巴士马上就要发车了……\x01",
            "快点到巴士停靠站去吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 0, 0, 8140, 189)
    EventEnd(0x5)
    Return()

    # Function_74_84A9 end

    def Function_75_8508(): pass

    label("Function_75_8508")

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
            " 前面是警备队专用运输铁道\x01",
            "     无关人员禁止入内\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_75_8508 end

    SaveToFile()

Try(main)
