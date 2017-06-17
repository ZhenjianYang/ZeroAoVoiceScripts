from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t1540.bin",                # FileName
        "t1540",                    # MapName
        "t1540",                    # Location
        0x0051,                     # MapIndex
        "ed7123",
        0x00002000,                 # Flags
        ("t1540", "t1540_1", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 81, 0, 1, 0, 3],
    )

    BuildStringList((
        "t1540",                  # 0
        "研修医リットン",         # 1
        "看護師シロン",           # 2
        "看護師フィリア",         # 3
        "マーサ師長",             # 4
        "看護師メイファ",         # 5
        "セシル",                 # 6
        "診察医ベルダイン",       # 7
        "ドノバン警部",           # 8
        "レイモンド捜査官",       # 9
        "入院患者",               # 10
        "入院患者",               # 11
        "入院患者",               # 12
        "入院患者",               # 13
        "入院患者",               # 14
        "女の子",                 # 15
        "入院患者",               # 16
        "入院患者",               # 17
        "入院患者",               # 18
        "入院患者",               # 19
        "入院患者",               # 20
        "入院患者",               # 21
        "入院患者",               # 22
        "入院患者",               # 23
        "入院患者",               # 24
        "入院患者",               # 25
        "入院患者",               # 26
        "入院患者",               # 27
        "入院患者",               # 28
        "入院患者",               # 29
        "入院患者",               # 30
        "入院患者",               # 31
        "入院患者",               # 32
        "入院患者",               # 33
        "入院患者",               # 34
        "入院患者",               # 35
        "入院患者",               # 36
        "黒月構成員",             # 37
        "見舞い客",               # 38
        "見舞い客",               # 39
        "観光客ヴェリアン",       # 40
        "ヨアヒム准教授",         # 41
    ))

    AddCharChip((
        "apl/ch50150.itc",                   # 00
        "chr/ch29900.itc",                   # 01
        "apl/ch50133.itc",                   # 02
        "apl/ch50137.itc",                   # 03
        "chr/ch29600.itc",                   # 04
        "chr/ch29800.itc",                   # 05
        "chr/ch07100.itc",                   # 06
        "apl/ch50143.itc",                   # 07
        "chr/ch33100.itc",                   # 08
        "apl/ch50132.itc",                   # 09
        "chr/ch22300.itc",                   # 0A
        "chr/ch00000.itc",                   # 0B
        "chr/ch05300.itc",                   # 0C
        "chr/ch29300.itc",                   # 0D
        "apl/ch50135.itc",                   # 0E
        "apl/ch50141.itc",                   # 0F
        "apl/ch50139.itc",                   # 10
        "chr/ch20400.itc",                   # 11
        "apl/ch50152.itc",                   # 12
        "apl/ch50142.itc",                   # 13
        "chr/ch20500.itc",                   # 14
        "chr/ch30300.itc",                   # 15
        "chr/ch30200.itc",                   # 16
        "chr/ch00000.itc",                   # 17
        "chr/ch00000.itc",                   # 18
        "chr/ch00000.itc",                   # 19
        "chr/ch00000.itc",                   # 1A
        "chr/ch00000.itc",                   # 1B
        "chr/ch00000.itc",                   # 1C
        "chr/ch00000.itc",                   # 1D
    ))

    DeclNpc(-4150,   699,     -56970,  270,  469,  0x0, 0,   0,   0,   255, 255, 1,   0,   255,  0)
    DeclNpc(110709,  0,       -5639,   0,    389,  0x0, 0,   1,   0,   0,   0,   1,   1,   255,  0)
    DeclNpc(24610,   0,       680,     225,  261,  0x0, 0,   1,   0,   0,   0,   1,   5,   255,  0)
    DeclNpc(108930,  0,       1450,    45,   261,  0x0, 0,   4,   0,   0,   0,   1,   6,   255,  0)
    DeclNpc(110709,  0,       -4320,   90,   389,  0x0, 0,   5,   0,   0,   0,   1,   7,   255,  0)
    DeclNpc(110709,  0,       -4320,   90,   389,  0x0, 0,   12,  0,   0,   0,   1,   8,   255,  0)
    DeclNpc(110720,  0,       -4239,   180,  389,  0x0, 0,   13,  0,   0,   0,   1,   9,   255,  0)
    DeclNpc(12779,   0,       1299,    270,  389,  0x0, 0,   21,  0,   0,   0,   1,   10,  255,  0)
    DeclNpc(11350,   0,       1299,    90,   389,  0x0, 0,   22,  0,   0,   0,   1,   11,  255,  0)
    DeclNpc(4849,    699,     -52060,  270,  469,  0x0, 0,   2,   0,   255, 255, 1,   13,  255,  0)
    DeclNpc(4809,    400,     -51959,  0,    469,  0x0, 0,   9,   0,   255, 255, 1,   14,  255,  0)
    DeclNpc(-4150,   699,     -52060,  270,  469,  0x0, 0,   3,   0,   255, 255, 1,   15,  255,  0)
    DeclNpc(4949,    699,     57029,   270,  469,  0x0, 0,   7,   0,   255, 255, 1,   16,  255,  0)
    DeclNpc(-4000,   699,     52029,   270,  469,  0x0, 0,   14,  0,   255, 255, 1,   17,  255,  0)
    DeclNpc(-3440,   0,       53919,   180,  389,  0x0, 0,   10,  0,   0,   0,   1,   20,  255,  0)
    DeclNpc(4949,    699,     52029,   270,  469,  0x0, 0,   2,   0,   255, 255, 1,   21,  255,  0)
    DeclNpc(-4000,   699,     52029,   270,  469,  0x0, 0,   3,   0,   255, 255, 1,   22,  255,  0)
    DeclNpc(4829,    400,     57029,   0,    469,  0x0, 0,   9,   0,   255, 255, 1,   23,  255,  0)
    DeclNpc(4849,    699,     -52060,  270,  469,  0x0, 0,   14,  0,   255, 255, 1,   24,  255,  0)
    DeclNpc(-4150,   699,     -56970,  270,  469,  0x0, 0,   15,  0,   255, 255, 1,   25,  255,  0)
    DeclNpc(4949,    699,     57029,   270,  469,  0x0, 0,   15,  0,   255, 255, 1,   26,  255,  0)
    DeclNpc(4949,    699,     52029,   270,  469,  0x0, 0,   3,   0,   255, 255, 1,   27,  255,  0)
    DeclNpc(-4150,   699,     -56970,  270,  469,  0x0, 0,   16,  0,   255, 255, 1,   28,  255,  0)
    DeclNpc(-4150,   699,     -52060,  270,  469,  0x0, 0,   14,  0,   255, 255, 1,   29,  255,  0)
    DeclNpc(4949,    699,     57029,   270,  469,  0x0, 0,   15,  0,   255, 255, 1,   30,  255,  0)
    DeclNpc(4949,    699,     52029,   270,  469,  0x0, 0,   3,   0,   255, 255, 1,   31,  255,  0)
    DeclNpc(-4000,   699,     52029,   270,  469,  0x0, 0,   2,   0,   255, 255, 1,   32,  255,  0)
    DeclNpc(-4150,   699,     -56970,  270,  469,  0x0, 0,   16,  0,   255, 255, 1,   33,  255,  0)
    DeclNpc(-4150,   699,     -52060,  270,  469,  0x0, 0,   15,  0,   255, 255, 1,   34,  255,  0)
    DeclNpc(-4000,   699,     57029,   270,  469,  0x0, 0,   2,   0,   255, 255, 1,   37,  255,  0)
    DeclNpc(-4230,   400,     57029,   0,    469,  0x0, 0,   9,   0,   255, 255, 1,   38,  255,  0)
    DeclNpc(-4000,   699,     52029,   270,  469,  0x0, 0,   15,  0,   255, 255, 1,   39,  255,  0)
    DeclNpc(-4150,   699,     -52060,  270,  469,  0x0, 0,   14,  0,   255, 255, 1,   41,  255,  0)
    DeclNpc(-4150,   699,     -56970,  270,  469,  0x0, 0,   16,  0,   255, 255, 1,   42,  255,  0)
    DeclNpc(4849,    699,     -52060,  270,  469,  0x0, 0,   7,   0,   255, 255, 1,   43,  255,  0)
    DeclNpc(4809,    400,     -51959,  0,    469,  0x0, 0,   19,  0,   255, 255, 1,   44,  255,  0)
    DeclNpc(4949,    699,     52029,   270,  469,  0x0, 0,   18,  0,   255, 255, 1,   45,  255,  0)
    DeclNpc(-4800,   0,       -53659,  0,    389,  0x0, 0,   17,  0,   0,   0,   1,   35,  255,  0)
    DeclNpc(-4409,   0,       53549,   180,  389,  0x0, 0,   20,  0,   0,   0,   1,   40,  255,  0)
    DeclNpc(30569,   0,       -21719,  315,  385,  0x0, 0,   8,   0,   0,   0,   1,   48,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   6,   0,   0,   0,   1,   46,  255,  0)

    DeclActor(23500,   0,       -830,    1500,    24610,   1500,    680,     0x007E, 1,  4,  0x0000)
    DeclActor(3960,    0,       56230,   1500,    4950,    1700,    57030,   0x007E, 1,  26, 0x0000)

    ScpFunction((
        "Function_0_608",          # 00, 0
        "Function_1_6C0",          # 01, 1
        "Function_2_BCF",          # 02, 2
        "Function_3_BD6",          # 03, 3
        "Function_4_129A",         # 04, 4
        "Function_5_13EA",         # 05, 5
        "Function_6_151A",         # 06, 6
        "Function_7_154E",         # 07, 7
        "Function_8_2670",         # 08, 8
        "Function_9_2723",         # 09, 9
        "Function_10_31B5",        # 0A, 10
        "Function_11_33EC",        # 0B, 11
        "Function_12_488D",        # 0C, 12
        "Function_13_4DD4",        # 0D, 13
    ))


    def Function_0_608(): pass

    label("Function_0_608")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_648"),
        (1, "loc_654"),
        (2, "loc_660"),
        (3, "loc_66C"),
        (4, "loc_678"),
        (5, "loc_684"),
        (6, "loc_690"),
        (SWITCH_DEFAULT, "loc_69C"),
    )


    label("loc_648")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_6A8")

    label("loc_654")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_6A8")

    label("loc_660")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_6A8")

    label("loc_66C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_6A8")

    label("loc_678")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_6A8")

    label("loc_684")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_6A8")

    label("loc_690")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_6A8")

    label("loc_69C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_6A8")

    label("loc_6A8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6BF")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_6A8")

    label("loc_6BF")

    Return()

    # Function_0_608 end

    def Function_1_6C0(): pass

    label("Function_1_6C0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6D8")
    ClearScenarioFlags(0x5F, 1)
    Call(0, 2)

    label("loc_6D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_730")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0xC, 110710, 0, -4320, 180)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xE, 5150, 0, -53670, 0)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x25, 0x80)
    ClearChrFlags(0x27, 0x80)
    ClearChrFlags(0x28, 0x80)
    ClearChrFlags(0x29, 0x80)
    ClearChrFlags(0x2B, 0x80)
    Jump("loc_B4B")

    label("loc_730")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_777")
    SetChrPos(0xE, 7320, 0, 4420, 180)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x26, 0x80)
    ClearChrFlags(0x27, 0x80)
    ClearChrFlags(0x28, 0x80)
    ClearChrFlags(0x29, 0x80)
    ClearChrFlags(0x2B, 0x80)
    ClearChrFlags(0x2C, 0x80)
    ClearChrFlags(0x2E, 0x80)
    Jump("loc_B4B")

    label("loc_777")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_7C8")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xE, 7320, 0, 4420, 180)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x25, 0x80)
    ClearChrFlags(0x27, 0x80)
    ClearChrFlags(0x28, 0x80)
    ClearChrFlags(0x29, 0x80)
    ClearChrFlags(0x2B, 0x80)
    ClearChrFlags(0x2C, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    Jump("loc_B4B")

    label("loc_7C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_7F4")
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0x25, 0x80)
    ClearChrFlags(0x27, 0x80)
    ClearChrFlags(0x28, 0x80)
    ClearChrFlags(0x29, 0x80)
    ClearChrFlags(0x2A, 0x80)
    Jump("loc_B4B")

    label("loc_7F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_836")
    SetChrPos(0xE, 29100, 0, -20520, 270)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0x24, 0x80)
    ClearChrFlags(0x2D, 0x80)
    Jump("loc_B4B")

    label("loc_836")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_85D")
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0x24, 0x80)
    Jump("loc_B4B")

    label("loc_85D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_884")
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    Jump("loc_B4B")

    label("loc_884")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_8ED")
    SetChrPos(0x30, -4130, 0, -55400, 180)
    ClearChrFlags(0x30, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0xC, 110710, 0, -4320, 180)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xE, 7320, 0, 4420, 180)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    Jump("loc_B4B")

    label("loc_8ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_925")
    SetChrPos(0x30, 4830, 0, 54990, 0)
    ClearChrFlags(0x30, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    Jump("loc_B4B")

    label("loc_925")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_962")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xE, 7320, 0, 4420, 180)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    Jump("loc_B4B")

    label("loc_962")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_9CB")
    SetChrPos(0x9, -4330, 0, -55480, 180)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 102380, 0, -2210, 180)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xE, -4630, 0, 53520, 180)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    Jump("loc_B4B")

    label("loc_9CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_A1E")
    SetChrPos(0x9, -4330, 0, -55480, 180)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xE, -4630, 0, 53520, 180)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    Jump("loc_B4B")

    label("loc_A1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_A8C")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0xA, -4010, 0, -53520, 0)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 102380, 0, -2210, 180)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xE, 29230, 0, -21560, 225)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x17, 0x80)
    Jump("loc_B4B")

    label("loc_A8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_AD7")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 4)), scpexpr(EXPR_END)), "loc_AD2")
    SetChrPos(0xA, 109200, 0, -8240, 180)

    label("loc_AD2")

    Jump("loc_B4B")

    label("loc_AD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_B3D")
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xC, 110710, 0, -4320, 180)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 1)), scpexpr(EXPR_END)), "loc_B38")
    SetChrPos(0x30, -4700, 0, 53690, 180)
    ClearChrFlags(0x30, 0x80)

    label("loc_B38")

    Jump("loc_B4B")

    label("loc_B3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_B4B")
    SetChrFlags(0xB, 0x80)

    label("loc_B4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B5E")
    ClearChrFlags(0x2F, 0x80)

    label("loc_B5E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B7D")
    Event(0, 10)
    Jump("loc_B97")

    label("loc_B7D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6B), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B97")
    Event(0, 13)

    label("loc_B97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_BAB")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 4)
    Jump("loc_BCE")

    label("loc_BAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_BBF")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 5)
    Jump("loc_BCE")

    label("loc_BBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 2)), scpexpr(EXPR_END)), "loc_BCE")
    ClearScenarioFlags(0x5C, 2)
    Event(0, 9)

    label("loc_BCE")

    Return()

    # Function_1_6C0 end

    def Function_2_BCF(): pass

    label("Function_2_BCF")

    Sound(160, 0, 100, 0)
    Return()

    # Function_2_BCF end

    def Function_3_BD6(): pass

    label("Function_3_BD6")

    OP_52(0x8, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x29, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2A, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2B, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2C, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapObjFrame(0xFF, "BED01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "BED02", 0x0, 0x1)
    SetMapObjFrame(0xFF, "BED03", 0x0, 0x1)
    SetMapObjFrame(0xFF, "BED04", 0x0, 0x1)
    SetMapObjFrame(0xFF, "BED05", 0x0, 0x1)
    SetMapObjFrame(0xFF, "BED06", 0x0, 0x1)
    SetMapObjFrame(0xFF, "BED07", 0x0, 0x1)
    SetMapObjFrame(0xFF, "BED08", 0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_DC1")
    SetMapObjFrame(0xFF, "BED03", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED04", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED07", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED08", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED05", 0x1, 0x1)
    Jump("loc_11F5")

    label("loc_DC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_E1D")
    SetMapObjFrame(0xFF, "BED03", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED04", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED07", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED08", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED05", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED02", 0x1, 0x1)
    Jump("loc_11F5")

    label("loc_E1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_E79")
    SetMapObjFrame(0xFF, "BED03", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED04", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED07", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED08", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED05", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED02", 0x1, 0x1)
    Jump("loc_11F5")

    label("loc_E79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_EC8")
    SetMapObjFrame(0xFF, "BED03", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED04", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED07", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED08", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED05", 0x1, 0x1)
    Jump("loc_11F5")

    label("loc_EC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_F17")
    SetMapObjFrame(0xFF, "BED04", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED02", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED08", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED07", 0x1, 0x1)
    Jump("loc_11F5")

    label("loc_F17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_F66")
    SetMapObjFrame(0xFF, "BED04", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED02", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED08", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED07", 0x1, 0x1)
    Jump("loc_11F5")

    label("loc_F66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_FA8")
    SetMapObjFrame(0xFF, "BED01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED02", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED08", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED07", 0x1, 0x1)
    Jump("loc_11F5")

    label("loc_FA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_FEA")
    SetMapObjFrame(0xFF, "BED01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED02", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED08", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED07", 0x1, 0x1)
    Jump("loc_11F5")

    label("loc_FEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_102C")
    SetMapObjFrame(0xFF, "BED01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED02", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED08", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED07", 0x1, 0x1)
    Jump("loc_11F5")

    label("loc_102C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_106E")
    SetMapObjFrame(0xFF, "BED01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED02", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED08", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED07", 0x1, 0x1)
    Jump("loc_11F5")

    label("loc_106E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_10B0")
    SetMapObjFrame(0xFF, "BED04", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED05", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED08", 0x1, 0x1)
    Jump("loc_11F5")

    label("loc_10B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_10F2")
    SetMapObjFrame(0xFF, "BED04", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED05", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED08", 0x1, 0x1)
    Jump("loc_11F5")

    label("loc_10F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_114E")
    SetMapObjFrame(0xFF, "BED08", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED05", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED07", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED04", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED02", 0x1, 0x1)
    Jump("loc_11F5")

    label("loc_114E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_119D")
    SetMapObjFrame(0xFF, "BED08", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED05", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED07", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED04", 0x1, 0x1)
    Jump("loc_11F5")

    label("loc_119D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_11EC")
    SetMapObjFrame(0xFF, "BED08", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED05", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED07", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED04", 0x1, 0x1)
    Jump("loc_11F5")

    label("loc_11EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_11F5")

    label("loc_11F5")

    OP_65(0x1, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1207")
    Jump("loc_1214")

    label("loc_1207")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1214")
    OP_66(0x1, 0x1)

    label("loc_1214")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1222")
    Jump("loc_124A")

    label("loc_1222")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_1234")
    OP_65(0x0, 0x1)
    Jump("loc_124A")

    label("loc_1234")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_124A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 4)), scpexpr(EXPR_END)), "loc_124A")
    OP_65(0x0, 0x1)

    label("loc_124A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1266")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_1299")

    label("loc_1266")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1282")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_1299")

    label("loc_1282")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1299")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)

    label("loc_1299")

    Return()

    # Function_3_BD6 end

    def Function_4_129A(): pass

    label("Function_4_129A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(4640, 1000, 2930, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x101, 2750, 0, 2430, 90)
    SetChrPos(0x102, 2800, 0, 3550, 90)
    SetChrPos(0x103, 1240, 0, 2380, 90)
    SetChrPos(0x104, 1190, 0, 3580, 90)
    SetChrPos(0x136, 4680, 0, 2930, 90)
    FadeToBright(1000, 0)
    OP_68(10640, 1000, 2930, 5000)

    def lambda_1348():
        OP_95(0xFE, 11750, 0, 2430, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1348)

    def lambda_1362():
        OP_95(0xFE, 11800, 0, 3550, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1362)

    def lambda_137C():
        OP_95(0xFE, 10240, 0, 2380, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_137C)

    def lambda_1396():
        OP_95(0xFE, 10190, 0, 3580, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1396)

    def lambda_13B0():
        OP_95(0xFE, 13680, 0, 2930, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x136, 1, lambda_13B0)
    OP_0D()
    Sleep(2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x136, 1)
    OP_6F(0x1)
    Call(0, 7)
    Return()

    # Function_4_129A end

    def Function_5_13EA(): pass

    label("Function_5_13EA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(36760, 1000, -18000, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x101, 39350, 100, -18000, 270)
    SetChrPos(0x102, 39350, 100, -18000, 270)
    SetChrPos(0x103, 39350, 100, -18000, 270)
    SetChrPos(0x104, 39350, 100, -18000, 270)
    SetChrPos(0x136, 39350, 100, -18000, 270)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x136, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    BeginChrThread(0x136, 3, 0, 6)
    Sleep(800)
    BeginChrThread(0x101, 3, 0, 6)
    Sleep(800)
    BeginChrThread(0x102, 3, 0, 6)
    Sleep(800)
    BeginChrThread(0x103, 3, 0, 6)
    Sleep(800)
    BeginChrThread(0x104, 3, 0, 6)
    OP_0D()
    Sleep(2000)
    FadeToDark(1000, 0, -1)
    WaitChrThread(0x136, 3)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x104, 0x2)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    OP_0D()
    Call(0, 7)
    Return()

    # Function_5_13EA end

    def Function_6_151A(): pass

    label("Function_6_151A")


    def lambda_151F():
        OP_95(0xFE, 27690, 0, -18220, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_151F)

    def lambda_1539():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1539)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_6_151A end

    def Function_7_154E(): pass

    label("Function_7_154E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(27000, 1300, -23530, 0)
    MoveCamera(49, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23010, 0)
    SetChrPos(0x101, 26200, 0, -20300, 180)
    SetChrPos(0x102, 27700, 0, -20300, 180)
    SetChrPos(0x103, 26200, 0, -18900, 180)
    SetChrPos(0x104, 27700, 0, -18900, 180)
    SetChrPos(0x136, 27000, 0, -22000, 180)
    OP_68(27000, 1300, -25030, 2000)

    def lambda_15F3():
        OP_95(0xFE, 27000, 0, -26000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x136, 1, lambda_15F3)

    def lambda_160D():
        OP_95(0xFE, 26200, 0, -24300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_160D)
    Sleep(50)

    def lambda_162A():
        OP_95(0xFE, 27700, 0, -24300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_162A)
    Sleep(50)

    def lambda_1647():
        OP_95(0xFE, 26200, 0, -22900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1647)
    Sleep(50)

    def lambda_1664():
        OP_95(0xFE, 27700, 0, -22900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1664)
    FadeToBright(1000, 0)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x136, 1)

    def lambda_169B():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x136, 1, lambda_169B)
    WaitChrThread(0x136, 1)
    OP_6F(0x1)
    OP_0D()

    #C0001
    ChrTalk(
        0x136,
        (
            "#1300F#12Pこの病室だけど……\x02\x03",

            "他の患者さんもいるから\x01",
            "あまりうるさくしないでね？\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x101,
        (
            "#0000F#5Pああ、大丈夫。\x01",
            "話を聞かせてもらうだけだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x136,
        (
            "#1309F#12Pふふ……\x01",
            "それじゃあ入りましょう。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-3410, 1000, -55120, 0)
    MoveCamera(30, 19, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(26050, 0)
    OP_4B(0x30, 0xFF)
    OP_4B(0x8, 0xFF)
    SetChrSubChip(0x8, 0x2)
    ClearChrFlags(0x30, 0x80)
    SetChrPos(0x30, -4130, 0, -55510, 180)
    SetChrPos(0x136, 0, 0, -49400, 180)
    SetChrPos(0x101, -600, 0, -48200, 180)
    SetChrPos(0x102, 600, 0, -48200, 180)
    SetChrPos(0x103, -600, 0, -47000, 180)
    SetChrPos(0x104, 600, 0, -47000, 180)
    OP_A7(0x136, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()

    #N0004
    NpcTalk(
        0x30,
        "医師",
        (
            "#2404F#5Pふむ……\x01",
            "経過は良好のようだね。\x02\x03",

            "#2400Fうん、これなら\x01",
            "明日にでも退院できるだろう。\x02",
        )
    )

    CloseMessageWindow()

    #N0005
    NpcTalk(
        0x8,
        "研修医の青年",
        "#4Pホ、ホントですか！？\x02",
    )

    CloseMessageWindow()

    #N0006
    NpcTalk(
        0x30,
        "医師",
        (
            "#2400F#5Pああ、嘘は言わないよ。\x02\x03",

            "#2409Fふふ……\x01",
            "退院したら覚悟するといい。\x02\x03",

            "君にやってもらう仕事を\x01",
            "山ほど用意してあるからね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #N0007
    NpcTalk(
        0x8,
        "研修医の青年",
        "#4Pちょ、ヨアヒム先生！？\x02",
    )

    CloseMessageWindow()

    #N0008
    NpcTalk(
        0x8,
        "研修医の青年",
        (
            "#4P病み上がりの人間に\x01",
            "そんな殺生な……\x02",
        )
    )

    CloseMessageWindow()

    #N0009
    NpcTalk(
        0x30,
        "医師",
        (
            "#2403F#5P裂傷と打撲と捻挫くらいで\x01",
            "情けないことを言いなさんな。\x02\x03",

            "#2400F逆にしこたま休んで\x01",
            "体力が有り余ってるだろう？\x02\x03",

            "#2409Fうんうん、今まで以上に\x01",
            "バリバリと働けるだろうさ。\x02",
        )
    )

    CloseMessageWindow()

    #N0010
    NpcTalk(
        0x8,
        "研修医の青年",
        (
            "#4P……先生って\x01",
            "よくＳって言われませんか？\x02",
        )
    )

    CloseMessageWindow()

    #N0011
    NpcTalk(
        0x30,
        "医師",
        (
            "#2403F#5Pうーん、僕としては\x01",
            "Ｍの方だと思うんだけどねぇ。\x02",
        )
    )

    CloseMessageWindow()
    ClearMapObjFlags(0x3, 0x10)
    OP_71(0x3, 0x0, 0xA, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x3)
    Sleep(300)

    #N0012
    NpcTalk(
        0x136,
        "セシルの声",
        (
            "#4Pもう……\x01",
            "何の話をしてるんですか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x30, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(-1940, 1000, -54350, 3000)

    def lambda_1BBA():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x30, 1, lambda_1BBA)
    WaitChrThread(0x30, 1)

    def lambda_1BCB():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x136, 1, lambda_1BCB)

    def lambda_1BE0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x136, 2, lambda_1BE0)
    Sleep(200)

    def lambda_1BF4():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1BF4)

    def lambda_1C09():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1C09)
    Sleep(100)

    def lambda_1C1D():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1C1D)

    def lambda_1C32():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1C32)
    Sleep(150)

    def lambda_1C46():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1C46)

    def lambda_1C5B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1C5B)
    Sleep(150)

    def lambda_1C6F():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1C6F)

    def lambda_1C84():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1C84)
    WaitChrThread(0x136, 1)

    def lambda_1C99():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x136, 1, lambda_1C99)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)

    def lambda_1CAE():
        OP_93(0xFE, 0xE1, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1CAE)

    def lambda_1CBB():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1CBB)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    def lambda_1CD0():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1CD0)

    def lambda_1CDD():
        OP_93(0xFE, 0xE1, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1CDD)
    WaitChrThread(0x136, 1)

    def lambda_1CEE():
        OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x136, 1, lambda_1CEE)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    Sleep(100)

    def lambda_1D0E():
        OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1D0E)
    Sleep(100)

    def lambda_1D26():
        OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1D26)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    Sleep(80)

    def lambda_1D46():
        OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1D46)
    Sleep(80)

    def lambda_1D5E():
        OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1D5E)
    WaitChrThread(0x136, 1)

    def lambda_1D77():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x136, 1, lambda_1D77)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x136, 1)
    WaitChrThread(0x136, 2)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x104, 2)
    OP_6F(0x1)
    OP_71(0x3, 0xA, 0x0, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x3)
    SetMapObjFlags(0x3, 0x10)

    #N0013
    NpcTalk(
        0x30,
        "医師",
        "#2405F#6Pおや……\x02",
    )

    CloseMessageWindow()

    #N0014
    NpcTalk(
        0x8,
        "研修医の青年",
        "#6Pあ……セシルさん！\x02",
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x136,
        (
            "#1306F#11Pお２人とも……\x01",
            "他の患者さんもいるんですから\x01",
            "あまり変な話をしたら駄目ですよ？\x02\x03",

            "#1301F子供が聞いたらどうするんですか？\x02",
        )
    )

    CloseMessageWindow()

    #N0016
    NpcTalk(
        0x8,
        "研修医の青年",
        "#6Pす、すみません……\x02",
    )

    CloseMessageWindow()

    #N0017
    NpcTalk(
        0x30,
        "医師",
        "#2406F#6Pはは、参ったな。\x02",
    )

    CloseMessageWindow()
    OP_63(0x30, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #N0018
    NpcTalk(
        0x30,
        "医師",
        "#2405F#6Pおや、そちらの方々は？\x02",
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x136,
        (
            "#1300F#11Pクロスベル警察の方です。\x02\x03",

            "その、例の事件について\x01",
            "リットンさんから直接\x01",
            "お話を聞きたいそうです。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0020
    ChrTalk(
        0x8,
        "#6Pあ……\x02",
    )

    CloseMessageWindow()

    #N0021
    NpcTalk(
        0x30,
        "医師",
        (
            "#2410F#6Pなるほど、そういう事か。\x02\x03",

            "#2400Fとなると僕はここで\x01",
            "退散した方がよさそうだね。\x02\x03",

            "他の病室を回診してくるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x136,
        (
            "#1302F#11Pお疲れさまです。\x02\x03",

            "#1300F……サボったら駄目ですよ？\x01",
            "水辺の方で釣りとか。\x02",
        )
    )

    CloseMessageWindow()

    #N0023
    NpcTalk(
        0x30,
        "医師",
        (
            "#2405F#6Pギクッ……\x01",
            "いやいや、滅相もない。\x02\x03",

            "#2404F──それじゃあ、失礼。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_20DB():

        label("loc_20DB")

        TurnDirection(0x101, 0x30, 500)
        Yield()
        Jump("loc_20DB")

    QueueWorkItem2(0x101, 1, lambda_20DB)

    def lambda_20ED():

        label("loc_20ED")

        TurnDirection(0x102, 0x30, 500)
        Yield()
        Jump("loc_20ED")

    QueueWorkItem2(0x102, 1, lambda_20ED)

    def lambda_20FF():

        label("loc_20FF")

        TurnDirection(0x103, 0x30, 500)
        Yield()
        Jump("loc_20FF")

    QueueWorkItem2(0x103, 1, lambda_20FF)

    def lambda_2111():

        label("loc_2111")

        TurnDirection(0x104, 0x30, 500)
        Yield()
        Jump("loc_2111")

    QueueWorkItem2(0x104, 1, lambda_2111)

    def lambda_2123():

        label("loc_2123")

        TurnDirection(0x136, 0x30, 500)
        Yield()
        Jump("loc_2123")

    QueueWorkItem2(0x136, 1, lambda_2123)

    def lambda_2135():
        OP_96(0xFE, 0xFFFFF8DA, 0x0, 0xFFFF220C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x136, 2, lambda_2135)
    BeginChrThread(0x30, 3, 0, 8)
    WaitChrThread(0x30, 3)
    WaitChrThread(0x136, 2)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x136, 0x1)
    SetChrFlags(0x30, 0x80)

    def lambda_2176():
        TurnDirection(0xFE, 0x136, 300)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2176)

    def lambda_2183():
        TurnDirection(0xFE, 0x136, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2183)

    def lambda_2190():
        TurnDirection(0xFE, 0x136, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2190)

    def lambda_219D():
        TurnDirection(0xFE, 0x136, 300)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_219D)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0024
    ChrTalk(
        0x101,
        "#0005F#5Pえっと、今の人は？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x136, 0x101, 500)
    Sleep(300)

    #C0025
    ChrTalk(
        0x136,
        (
            "#1300F#12Pヨアヒム先生といって\x01",
            "准教授をされている方よ。\x02\x03",

            "#1306Fとても優秀な先生なんだけど\x01",
            "少し趣味人すぎるというか……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x136, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x136, 0x13B, 0x1F4)
    OP_68(-2550, 1000, -54720, 3000)

    def lambda_228E():
        OP_93(0xFE, 0xD7, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_228E)

    def lambda_229B():
        OP_93(0xFE, 0xD7, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_229B)
    Sleep(100)

    def lambda_22AB():
        OP_93(0xFE, 0xD7, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_22AB)

    def lambda_22B8():
        OP_93(0xFE, 0xD7, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_22B8)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    def lambda_22D5():
        OP_95(0xFE, -3180, 0, -55730, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x136, 1, lambda_22D5)
    WaitChrThread(0x136, 1)

    def lambda_22F3():
        OP_95(0xFE, -4030, 0, -55490, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x136, 1, lambda_22F3)
    WaitChrThread(0x136, 1)

    def lambda_2311():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x136, 1, lambda_2311)
    WaitChrThread(0x136, 1)

    def lambda_2322():
        OP_9B(0x0, 0xFE, 0x0, 0x2EE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2322)
    Sleep(50)

    def lambda_233A():
        OP_9B(0x0, 0xFE, 0x0, 0x2EE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_233A)
    Sleep(100)

    def lambda_2352():
        OP_9B(0x0, 0xFE, 0x0, 0x2EE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2352)
    Sleep(80)

    def lambda_236A():
        OP_9B(0x0, 0xFE, 0x0, 0x2EE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_236A)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x1)

    #C0026
    ChrTalk(
        0x136,
        (
            "#1300F#5P……それで、リットンさん。\x01",
            "お時間を頂いても大丈夫ですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x8,
        (
            "#6Pえ、ええ。\x01",
            "それは構わないですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x8,
        (
            "#6Pでも、どうして\x01",
            "クロスベル警察の人が？\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x8,
        (
            "#6P警備隊が調べていたんじゃ\x01",
            "なかったのかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x101,
        (
            "#0003F#5Pそれが、警備隊の方でも\x01",
            "手詰まりになったらしくて……\x02\x03",

            "#0001F自分たちも捜査協力を\x01",
            "することになったんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x8,
        "#6Pそうなのか……\x02",
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x8,
        (
            "#6Pうーん、やっぱり僕が\x01",
            "夢を見たとか思われてるのかなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x8,
        (
            "#6Pそれとも夢遊病？\x01",
            "いやいや、そんなわけが……\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x102,
        (
            "#0103F#11Pその、できれば改めて\x01",
            "聞かせていただけませんか？\x02\x03",

            "#0101F１週間前の夜、起きた事について。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x8,
        "#6Pあ、ああ……\x02",
    )

    CloseMessageWindow()
    StopBGM(0xBB8)
    Sleep(100)
    SetChrSubChip(0x8, 0x0)
    Sleep(200)
    OP_63(0x8, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x8)

    #C0036
    ChrTalk(
        0x8,
        (
            "#11P──そうだな。\x01",
            "あれは研修レポートを書き上げた\x01",
            "深夜のことだった。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x204), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x5C, 0)
    NewScene("t160B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_7_154E end

    def Function_8_2670(): pass

    label("Function_8_2670")


    def lambda_2675():
        OP_95(0xFE, 10, 0, -55640, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2675)
    WaitChrThread(0xFE, 1)

    def lambda_2693():
        OP_95(0xFE, 10, 0, -51540, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2693)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    ClearMapObjFlags(0x3, 0x10)
    OP_71(0x3, 0x0, 0xA, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x3)

    def lambda_26D3():
        OP_95(0xFE, 30, 0, -48960, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_26D3)
    Sleep(500)

    def lambda_26F0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_26F0)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Sleep(500)
    OP_71(0x3, 0xA, 0x0, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x3)
    SetMapObjFlags(0x3, 0x10)
    Return()

    # Function_8_2670 end

    def Function_9_2723(): pass

    label("Function_9_2723")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(0, 16777215, -1)
    OP_68(-3120, 2000, -54300, 0)
    MoveCamera(35, 25, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(26050, 0)
    OP_4B(0x8, 0xFF)
    SetChrSubChip(0x8, 0x2)
    SetChrPos(0x101, -3700, 0, -55250, 180)
    SetChrPos(0x102, -4600, 0, -55250, 180)
    SetChrPos(0x103, -3700, 0, -54150, 180)
    SetChrPos(0x104, -4600, 0, -54150, 180)
    SetChrPos(0x136, -2500, 0, -55250, 225)
    FadeToBright(0, -1)
    FadeToBright(1000, 16777215)
    OP_68(-3120, 500, -54300, 3000)
    OP_6F(0x1)
    OP_0D()

    #C0037
    ChrTalk(
        0x8,
        (
            "#4P……記憶があるのは\x01",
            "実際には、そこまでなんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x8,
        (
            "#4P翌朝、用務員さんが\x01",
            "ズタボロになって気絶した\x01",
            "僕のことを発見してくれて……\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x8,
        (
            "#4Pそれで緊急入院して\x01",
            "今現在に至るというわけさ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)

    #C0040
    ChrTalk(
        0x101,
        (
            "#0003F#5P……なるほど。\x01",
            "状況は一通り把握しました。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x104,
        (
            "#0301F#5P襲ってきた魔獣どもの姿は\x01",
            "はっきりとは見てないのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x8,
        (
            "#4Pいや、恥ずかしながら\x01",
            "ショックで気絶したらしくてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x8,
        (
            "#4P真っ赤に光る目と白い牙、\x01",
            "それと黒っぽい毛並みくらいしか\x01",
            "覚えていないんだよ……\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x8,
        (
            "#4Pただ、警備隊も確認してたけど、\x01",
            "狼っぽいと言われたらそうだと思う。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x103,
        "#0203F#5Pなるほど……\x02",
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x102,
        (
            "#0101F#5Pその……\x01",
            "傷の方はどうだったんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x8,
        (
            "#4Pうん、右肩のところに\x01",
            "牙で噛まれたような跡はあった。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x8,
        (
            "#4P逆にそれ以外の怪我は\x01",
            "打撲とか捻挫とかくらいでね。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x8,
        (
            "#4Pたぶん噛み付かれたあと、\x01",
            "そのまま床に引き倒されたと\x01",
            "思うんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x101,
        (
            "#0003F#5P……なぜか魔獣はそれ以上\x01",
            "あなたを襲わなかった。\x02\x03",

            "#0001Fつまり、そういう事ですね？\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x8,
        "#4Pそうそう、そうなんだ！\x02",
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x8,
        (
            "#4P本当なら食い千切られても\x01",
            "おかしくないところなのに……\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x8,
        (
            "#4Pおまけに場所が屋上だろ？\x01",
            "もう警備隊の人にも胡散臭い目で\x01",
            "見られちゃってさぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x8,
        (
            "#4Pしまいには、夜中フラフラ街道に出て\x01",
            "魔獣に襲われたんじゃないかって\x01",
            "疑われる始末だったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x103,
        (
            "#0200F#5Pでも、あなたが発見されたのは\x01",
            "この建物の屋上ですよね……？\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x8,
        (
            "#4Pうーん、襲われたパニックで\x01",
            "屋上まで逃げてから気絶した……\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x8,
        "#4Pその可能性はゼロじゃないかもなぁ。\x02",
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
    Sleep(1200)

    #C0058
    ChrTalk(
        0x101,
        (
            "#0006F#5Pそ、それはさすがに\x01",
            "無理があるんじゃ……\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x136,
        (
            "#1306F#11Pもう、リットンさん。\x02\x03",

            "#1301F襲われたあなたが\x01",
            "そんな自信のないことで\x01",
            "どうするんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x8,
        "#4Pいや、その……すみません。\x02",
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x8,
        (
            "#4Pでもねぇ、説明が付かない事を\x01",
            "そのままにするのも嫌じゃない？\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x8,
        (
            "#4Pだったら自分の記憶が\x01",
            "曖昧になってるって考えた方が\x01",
            "気が楽っていうか……\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x8,
        (
            "#4Pというか、もし本当に魔獣が\x01",
            "屋上なんかに現れたんだとしたら\x01",
            "……ちょっと恐すぎない？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)

    #C0064
    ChrTalk(
        0x136,
        (
            "#1306F#11Pふう……気持ちは\x01",
            "分からなくもないですけど。\x02\x03",

            "#1301Fでも、本当にそうだとしたら\x01",
            "ちゃんと対策を考えないと……\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x101,
        (
            "#0003F#5P…………………………………………\x02\x03",

            "#0000Fご協力、ありがとうございました。\x02\x03",

            "自分たちの方でも\x01",
            "襲われた現場を調べてみます。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x8,
        "#4Pあ、ああ、よろしく頼むよ。\x02",
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x8,
        (
            "#4Pちゃんとした説明がついて\x01",
            "対策できるんだったら\x01",
            "それに越した事はないからね。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    StopBGM(0x7D0)
    SetChrPos(0x0, -2910, 0, -54690, 90)
    SetScenarioFlags(0x62, 1)
    OP_29(0x3F, 0x1, 0xA)
    SetChrSubChip(0x8, 0x0)
    OP_4C(0x8, 0xFF)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7123", 0)
    EventEnd(0x5)
    Return()

    # Function_9_2723 end

    def Function_10_31B5(): pass

    label("Function_10_31B5")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(26720, 1000, -24500, 0)
    MoveCamera(49, 19, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, 26940, 0, -23600, 180)
    SetChrPos(0x102, 27970, 0, -24220, 270)
    SetChrPos(0x103, 28250, 0, -25380, 270)
    SetChrPos(0x104, 26030, 0, -25470, 0)
    SetChrPos(0x136, 25110, 0, -23850, 90)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 7)), scpexpr(EXPR_END)), "loc_328E")

    #C0068
    ChrTalk(
        0x104,
        (
            "#12P#0300Fさてと……\x01",
            "今度は屋上の調査か？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_32BD")

    label("loc_328E")


    #C0069
    ChrTalk(
        0x104,
        (
            "#12P#0300Fさてと……\x01",
            "ここの屋上だったな？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32BD")


    #C0070
    ChrTalk(
        0x101,
        (
            "#5P#0001Fああ、まずは\x01",
            "襲われた現場に行ってみよう。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x136, 500)
    Sleep(300)

    #C0071
    ChrTalk(
        0x101,
        "#0005F#11Pセシル姉、時間の方は大丈夫？\x02",
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x136,
        (
            "#6P#1306Fそうね、そろそろ\x01",
            "休憩時間が終わっちゃうかも……\x02\x03",

            "#1300Fでも、せめてリットンさんが\x01",
            "発見された場所までは案内するわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x101,
        "#0000F#11Pうん、よろしく頼むよ。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 27000, 0, -26000, 0)
    SetScenarioFlags(0x62, 2)
    EventEnd(0x5)
    Return()

    # Function_10_31B5 end

    def Function_11_33EC(): pass

    label("Function_11_33EC")

    EventBegin(0x0)
    Fade(1000)
    OP_68(23570, 1000, -500, 0)
    MoveCamera(68, 15, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(26180, 0)
    SetChrPos(0x101, 22560, 0, -1490, 45)
    SetChrPos(0x102, 21620, 0, -3050, 45)
    SetChrPos(0x103, 21010, 0, -2400, 45)
    SetChrPos(0x104, 22860, 0, -3470, 45)
    OP_4B(0xA, 0xFF)
    SetChrPos(0xA, 24600, 0, 300, 225)
    OP_4B(0xB, 0xFF)
    SetChrPos(0xB, 30540, 0, 20, 270)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6A, 1)), scpexpr(EXPR_END)), "loc_34EB")

    #C0074
    ChrTalk(
        0xA,
        "#5Pあ、お疲れさまでーす。\x02",
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xA,
        "#5P調査の方はいかがですか～？\x02",
    )

    CloseMessageWindow()
    Jump("loc_3546")

    label("loc_34EB")


    #C0076
    ChrTalk(
        0xA,
        "#5Pあ、お疲れさまでーす。\x02",
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xA,
        (
            "#5Pたしか警察の方ですよね？\x01",
            "調査の方はいかがですか～？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3546")


    #C0078
    ChrTalk(
        0x101,
        (
            "#0004F#6Pはい、一通り終了しました。\x02\x03",

            "#0000Fそれで、セシル姉……\x01",
            "いやセシルさんに\x01",
            "報告しようと思いまして。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xA,
        "#5Pあ、そうだったんですか～。\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1200)

    #C0080
    ChrTalk(
        0xA,
        (
            "#5Pうふふっ……\x01",
            "それにしてもセシル先輩から\x01",
            "聞いていた通りだったなぁ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0081
    ChrTalk(
        0x101,
        "#0005F#6Pえ……？\x02",
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xA,
        (
            "#5Pうふふ、いつもロイド君の話を\x01",
            "聞かされてたんですよ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xA,
        (
            "#5P最近クロスベルに帰ってきたって\x01",
            "セシル先輩、ずっと嬉しそうで～。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xA,
        (
            "#5Pうふふ……\x01",
            "これだけ可愛かったら納得だなぁ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    #C0085
    ChrTalk(
        0x101,
        "#0011F#6Pか、可愛いって……\x02",
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x103,
        "#0211F#6P（……鼻の下、伸びてます。）\x02",
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x102,
        (
            "#0103F#12P（まったく……\x01",
            "  勤務中にだらしがないわね。）\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0xE1, 0x1F4)

    #C0088
    ChrTalk(
        0x101,
        (
            "#0013F#5P（の、伸びてないし、\x01",
            "  だらしがなくもないって！）\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3814():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3814)
    WaitChrThread(0x104, 1)
    Sleep(300)

    #C0089
    ChrTalk(
        0x104,
        (
            "#0304F#12P（フッ……\x01",
            "  まあ待ちな、ロイド。）\x02\x03",

            "#0302F（ここはお兄さんに任せとけ。）\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x101,
        "#0005F#5P（へ……）\x02",
    )

    CloseMessageWindow()
    OP_68(23600, 1000, -700, 1000)

    def lambda_38AB():
        OP_95(0xFE, 22880, 0, -1560, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_38AB)

    def lambda_38C5():
        OP_96(0xFE, 0x5168, 0x0, 0xFFFFFA6A, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_38C5)

    def lambda_38DF():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_38DF)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x101, 2)
    OP_93(0x104, 0x2D, 0x1F4)
    Sleep(300)

    #C0091
    ChrTalk(
        0x104,
        (
            "#0309F#2Pははっ……\x01",
            "可愛いってのは君みたいな子に\x01",
            "使うべきだと思うけどな。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0092
    ChrTalk(
        0xA,
        "#5Pえ……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6A, 1)), scpexpr(EXPR_END)), "loc_39BC")

    #C0093
    ChrTalk(
        0x104,
        (
            "#0304F#2Pまあ俺も、コイツが\x01",
            "可愛いってのは同感だけどね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A86")

    label("loc_39BC")


    #C0094
    ChrTalk(
        0x104,
        (
            "#0302F#2Pいきなりごめん。\x01",
            "俺はランディっていうんだ。\x02\x03",

            "君の名前は？\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xA,
        "#5Pえっと、フィリアですけど～。\x02",
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xA,
        (
            "#5Pランディさんは\x01",
            "ロイド君の同僚さんですか～？\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x104,
        "#0304F#2Pああ、これでも警察官でね。\x02",
    )

    CloseMessageWindow()

    label("loc_3A86")

    Sleep(300)

    #C0098
    ChrTalk(
        0x104,
        (
            "#0302F#2Pどう、お近づきの印に\x01",
            "週末みんなで合コンでも？\x02\x03",

            "当然コイツも連れてくるし、\x01",
            "こっちも女の子がいるから\x01",
            "楽しいと思うよ？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3B10():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3B10)
    WaitChrThread(0x101, 1)

    #C0099
    ChrTalk(
        0x101,
        "#0001F#6Pちょ、ちょっと……\x02",
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xA,
        "#5Pんー、そうですねぇ。\x02",
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xA,
        (
            "#5Pたまには息抜きもしたいし、\x01",
            "スケジュールが合いそうな子を\x01",
            "誘ってみましょうか～？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3BB6():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3BB6)
    WaitChrThread(0x101, 1)

    #C0102
    ChrTalk(
        0x104,
        (
            "#0309F#2Pうんうん、そうしてよ。\x02\x03",

            "#0300Fクロスベルの居酒屋でいいかな？\x01",
            "俺の方でセッティングするからさ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0103
    ChrTalk(
        0x103,
        "#0200F#6P（……ソツがないですね。）\x02",
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x102,
        (
            "#0106F#12P（さすがナンパが\x01",
            "  趣味と言うだけはあるわね……）\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x101,
        (
            "#0006F#6P（というか俺たち、セシル姉に\x01",
            "  報告に来てるんだけど……）\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x104,
        (
            "#0309F#2Pいや～、しかし光栄だな。\x02\x03",

            "君みたいな白衣の天使と\x01",
            "お近づきになれるなんてさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xA,
        (
            "#5Pえ～、でもウチのナース服って\x01",
            "別に白衣じゃないですよ～？\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0xA,
        "#5Pそれでもいいんですか～？\x02",
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x104,
        (
            "#0304F#2Pノープロブレムさ。\x02\x03",

            "#0302Fその服だって可愛いし、\x01",
            "それ以上に、中の子たちが\x01",
            "みんな抜群に可愛いからね。\x02\x03",

            "#0309F君なんか特にさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xA,
        "#5Pも～、ランディさんったらぁ。\x02",
    )

    CloseMessageWindow()
    ClearMapObjFlags(0x2, 0x10)
    OP_71(0x2, 0x0, 0xA, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x2)
    Sleep(300)

    #N0111
    NpcTalk(
        0xB,
        "おばさんの声",
        (
            "おや、抜群に可愛いだなんて\x01",
            "照れちまうねぇ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_3F2D():
        OP_95(0xFE, 24940, 0, -190, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_3F2D)

    def lambda_3F47():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_3F47)

    def lambda_3F58():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3F58)
    WaitChrThread(0xA, 1)
    Sleep(500)

    def lambda_3F6C():
        OP_96(0xFE, 0x5E10, 0x0, 0x258, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_3F6C)
    WaitChrThread(0xB, 1)
    WaitChrThread(0xB, 2)
    WaitChrThread(0xA, 2)
    SetMapObjFlags(0x2, 0x10)
    OP_71(0x2, 0xA, 0x0, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x2)

    #C0112
    ChrTalk(
        0x104,
        "#0305F#2Pへ……\x02",
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xA,
        "#5Pあはは、師長……\x02",
    )

    CloseMessageWindow()

    def lambda_3FDB():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_3FDB)
    WaitChrThread(0xB, 1)

    #C0114
    ChrTalk(
        0xB,
        "#2Pあはは、じゃないだろ。\x02",
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0xB,
        (
            "#2P午後の検温はどうしたんだい？\x01",
            "アンタの担当だろう。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0116
    ChrTalk(
        0xA,
        "#5Pあ……\x02",
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xB,
        (
            "#2Pそれに週末といえば、\x01",
            "大きな手術が入っているのを\x01",
            "忘れたのかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xA,
        "#5Pあはは、そーでした。\x02",
    )

    CloseMessageWindow()

    def lambda_40D3():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_40D3)
    WaitChrThread(0xA, 1)

    #C0119
    ChrTalk(
        0xA,
        (
            "#5Pゴメンなさい、ランディさん。\x01",
            "またの機会ということで～。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xA,
        "#5Pロイド君に皆さんも、またね～！\x02",
    )

    CloseMessageWindow()

    def lambda_414B():

        label("loc_414B")

        TurnDirection(0x104, 0xA, 500)
        Yield()
        Jump("loc_414B")

    QueueWorkItem2(0x104, 1, lambda_414B)

    def lambda_415D():

        label("loc_415D")

        TurnDirection(0xB, 0xA, 500)
        Yield()
        Jump("loc_415D")

    QueueWorkItem2(0xB, 1, lambda_415D)

    def lambda_416F():
        OP_95(0xFE, 26210, 0, 1130, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_416F)
    WaitChrThread(0xA, 1)

    def lambda_418D():
        OP_95(0xFE, 28770, 0, -20, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_418D)
    WaitChrThread(0xA, 1)
    ClearMapObjFlags(0x2, 0x10)
    OP_71(0x2, 0x0, 0xA, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x2)

    def lambda_41C6():
        OP_95(0xFE, 31000, 0, 10, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_41C6)
    Sleep(150)

    def lambda_41E3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_41E3)
    WaitChrThread(0xA, 1)
    WaitChrThread(0xA, 2)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetMapObjFlags(0x2, 0x10)
    OP_71(0x2, 0xA, 0x0, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x2)
    EndChrThread(0x104, 0x1)
    EndChrThread(0xB, 0x1)

    #C0121
    ChrTalk(
        0x104,
        "#0305F#2Pえっと……\x02",
    )

    CloseMessageWindow()

    def lambda_4242():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_4242)
    WaitChrThread(0xB, 1)

    #C0122
    ChrTalk(
        0xB,
        (
            "#5P何なら代わりに\x01",
            "週末アタシが付き合おうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0xB,
        (
            "#5Pこれでも白衣の天使と\x01",
            "言えなくもないだろうしねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x104,
        (
            "#0309F#2Pい、いやぁ……あはは。\x01",
            "さすがに畏れ多いッスから。\x02\x03",

            "#0306F（タッチだ……ロイド。）\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x87, 0x1F4)

    def lambda_4326():
        OP_96(0xFE, 0x594C, 0x0, 0xFFFFF272, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4326)

    def lambda_4340():
        OP_93(0xFE, 0x2D, 0x64)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_4340)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x104, 2)

    #C0125
    ChrTalk(
        0x101,
        "#0001F#5Pはあ、まったく……\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x190)
    OP_68(23820, 1000, -720, 1000)

    def lambda_438E():
        OP_96(0xFE, 0x5492, 0x0, 0xFFFFFB14, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_438E)
    WaitChrThread(0x101, 1)
    OP_6F(0x1)

    #C0126
    ChrTalk(
        0x101,
        (
            "#0006F#6P……すみません。\x01",
            "騒がしくしてしまって。\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x101, 2)

    def lambda_43EC():
        OP_93(0xFE, 0x104, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_43EC)
    WaitChrThread(0xB, 1)
    Sleep(300)

    #C0127
    ChrTalk(
        0xB,
        "#5Pふう、まあいいさ。\x02",
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0xB,
        (
            "#5Pそれで、調査はもういいのかい？\x01",
            "セシルを呼ぼうとしてたみたいだが。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x101,
        (
            "#0000F#6Pはい、一通り終了しました。\x02\x03",

            "それで、幾つか判明したので\x01",
            "彼女に報告しようと思いまして。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0xB,
        (
            "#5Pセシルはこの時間だと\x01",
            "たしかあの子の所に……\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xB,
        (
            "#5Pうーん、アナウンスで呼ぶのも\x01",
            "ちょっとアレだしねぇ……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x22, 0x24, 0xFA, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1200)

    #C0132
    ChrTalk(
        0xB,
        "#5Pそうだ、あんたたち。\x02",
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xB,
        (
            "#5P多分あの娘は、この上の階の\x01",
            "一番奥の病室にいると思うんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xB,
        "#5Pそっちに行ってくれるかね？\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0135
    ChrTalk(
        0x101,
        "#0005F#6P病室……ですか？\x02",
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x102,
        "#0105F#12Pお邪魔してもいいんでしょうか？\x02",
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xB,
        (
            "#5Pああ、ちょっと訳アリの子が\x01",
            "入院していてねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xB,
        (
            "#5Pできればアンタたちにも\x01",
            "見舞ってあげて欲しいんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x101,
        (
            "#0000F#6Pなるほど……\x01",
            "分かりました。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x104,
        (
            "#0300F#12P適当に遊んであげりゃあ\x01",
            "いいって事ッスよね？\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xB,
        "#5Pま、そういう事さね。\x02",
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xB,
        "#5Pそれじゃあよろしく頼むよ。\x02",
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x103,
        "#0200F#6P………………………………\x02",
    )

    CloseMessageWindow()
    OP_93(0xB, 0x5A, 0x1F4)

    def lambda_47B3():
        OP_95(0xFE, 28870, 0, 20, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_47B3)
    WaitChrThread(0xB, 1)
    ClearMapObjFlags(0x2, 0x10)
    OP_71(0x2, 0x0, 0xA, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x2)

    def lambda_47EC():
        OP_95(0xFE, 30850, 0, 10, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_47EC)
    Sleep(200)

    def lambda_4809():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_4809)
    WaitChrThread(0xB, 1)
    WaitChrThread(0xB, 2)
    SetMapObjFlags(0x2, 0x10)
    OP_71(0x2, 0xA, 0x0, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x2)
    SetChrPos(0xB, 108930, 0, 1450, 45)
    OP_4C(0xB, 0xFF)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    SetChrPos(0xA, 109200, 0, -8240, 180)
    OP_4C(0xA, 0xFF)
    SetChrPos(0x0, 22400, 0, -1750, 45)
    OP_65(0x0, 0x1)
    SetScenarioFlags(0x63, 4)
    OP_29(0x3F, 0x1, 0x13)
    EventEnd(0x5)
    Return()

    # Function_11_33EC end

    def Function_12_488D(): pass

    label("Function_12_488D")

    EventBegin(0x0)
    OP_4B(0xB, 0xFF)
    Fade(1000)
    OP_68(107900, 1000, 1500, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0xB, 108930, 0, 1450, 270)
    SetChrPos(0x101, 107230, 0, 850, 90)
    SetChrPos(0x102, 107230, 0, 2180, 90)
    SetChrPos(0x103, 105980, 0, 850, 90)
    SetChrPos(0x104, 105980, 0, 2180, 90)
    OP_0D()

    #C0144
    ChrTalk(
        0xB,
        "#11Pおや、アンタたち。\x02",
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0xB,
        (
            "#11Pセシルがいるのは\x01",
            "３階の一番奥の病室だよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0146
    ChrTalk(
        0xB,
        "#11Pおや……？\x02",
    )

    CloseMessageWindow()
    OP_68(106400, 1000, 1500, 3000)

    def lambda_49AA():

        label("loc_49AA")

        TurnDirection(0x101, 0xB, 500)
        Yield()
        Jump("loc_49AA")

    QueueWorkItem2(0x101, 2, lambda_49AA)

    def lambda_49BC():

        label("loc_49BC")

        TurnDirection(0x102, 0xB, 500)
        Yield()
        Jump("loc_49BC")

    QueueWorkItem2(0x102, 2, lambda_49BC)

    def lambda_49CE():

        label("loc_49CE")

        TurnDirection(0x104, 0xB, 500)
        Yield()
        Jump("loc_49CE")

    QueueWorkItem2(0x104, 2, lambda_49CE)

    def lambda_49E0():
        OP_96(0xFE, 0x19DFC, 0x0, 0x352, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_49E0)
    Sleep(500)

    def lambda_49FD():
        OP_96(0xFE, 0x1A2DE, 0x0, 0x1C2, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_49FD)
    Sleep(500)
    OP_63(0x103, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_4A2C():
        OP_96(0xFE, 0x19884, 0x0, 0x352, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4A2C)
    WaitChrThread(0xB, 1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x103, 1)
    OP_64(0x103)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x104, 0x2)
    OP_6F(0x79)

    #C0147
    ChrTalk(
        0x101,
        "#0005F#11P師長さん……？\x02",
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x103,
        "#0208F#6P#40W……なんでしょう………？\x02",
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0149
    ChrTalk(
        0xB,
        "#11Pやっぱりそうだ！\x02",
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xB,
        "#11Pあんた、ティオちゃんだろ！？\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0151
    ChrTalk(
        0x101,
        "#0011F#11Pえ……！？\x02",
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x102,
        "#0105F#5Pどうして……\x02",
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x103,
        (
            "#0208F#6P#40W………………………………\x02\x03",

            "#0206F#40W……ご無沙汰……してます。\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0xB,
        "#11Pはは、やっぱりそうだ。\x02",
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0xB,
        (
            "#11P大きくなったねぇ！\x01",
            "こんなに美人さんになって！\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xB,
        "#11Pうんうん、見違えたよ！\x02",
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1200)
    OP_93(0xB, 0x2D, 0x1F4)
    Sleep(300)

    #C0157
    ChrTalk(
        0xB,
        (
            "#5Pおや、しかしどうして\x01",
            "あんたが警察の坊やたちと……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xB, 0x10E, 0x190)

    #C0158
    ChrTalk(
        0xB,
        "#11Pん～……？\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0xB, 1)

    #C0159
    ChrTalk(
        0x103,
        (
            "#0208F#6P#40Wその……\x01",
            "……色々事情があって。\x02\x03",

            "#0203F#40Wまた近いうちに\x01",
            "挨拶に来るつもりです……\x02\x03",

            "#0202F#40W今日は急ぐので、これで……\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0xB,
        "#11Pあ、ああ……\x02",
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xB,
        (
            "#11P──そうだね。\x01",
            "また今度、ゆっくりおいで。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 104070, 0, 940, 270)
    SetChrPos(0xB, 108930, 0, 1450, 45)
    OP_4C(0xB, 0xFF)
    SetScenarioFlags(0x63, 5)
    ClearScenarioFlags(0x0, 4)
    EventEnd(0x5)
    Return()

    # Function_12_488D end

    def Function_13_4DD4(): pass

    label("Function_13_4DD4")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50104.itc", 0x1E)
    OP_68(27690, 1000, -9660, 0)
    MoveCamera(52, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25500, 0)
    SetChrPos(0x101, 26000, 0, -6300, 180)
    SetChrPos(0x102, 27600, 0, -6000, 180)
    SetChrPos(0x103, 26800, 0, -8400, 180)
    SetChrPos(0x104, 26800, 0, -5000, 180)
    FadeToBright(1000, 0)
    SetCameraDistance(24000, 3000)

    def lambda_4E6F():
        OP_95(0xFE, 26000, 0, -8800, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4E6F)

    def lambda_4E89():
        OP_95(0xFE, 27600, 0, -8500, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4E89)

    def lambda_4EA3():
        OP_95(0xFE, 26800, 0, -10400, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4EA3)

    def lambda_4EBD():
        OP_95(0xFE, 26800, 0, -7500, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4EBD)
    OP_0D()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x10)

    #C0162
    ChrTalk(
        0x103,
        "#0208F#5P………………………………\x02",
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x101,
        (
            "#0001F#5Pティオ……\x01",
            "前にこの病院に？\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0x103,
        (
            "#0208F#5P……ええ。\x02\x03",

            "６年ほど前のことです。\x02\x03",

            "#0206F黙っているつもりでは\x01",
            "なかったんですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0x104,
        "#0303F#5Pふむ……\x02",
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x101,
        (
            "#0006F#5Pその……何ていうか。\x02\x03",

            "#0000Fあんまり気にするなよ。\x01",
            "誰にだって言いにくいことは\x01",
            "あるんだし……\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x103,
        "#0208F#5P……ですが………\x02",
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x102)
    OP_68(27590, 1000, -9860, 1000)
    SetCameraDistance(23500, 1000)
    OP_95(0x102, 26970, 0, -9830, 2000, 0x0)
    Fade(500)

    def lambda_5087():
        OP_A6(0xFE, 0x0, 0x1E, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_5087)
    SetCameraDistance(22330, 0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0x103, 0x2)
    SetChrFlags(0x103, 0x10)
    SetChrChipByIndex(0x103, 0x1E)
    SetChrSubChip(0x103, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()

    #C0168
    ChrTalk(
        0x102,
        "#0104F#5Pえいっ。\x02",
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0169
    ChrTalk(
        0x103,
        "#0205F#5Pエ、エリィさん……？\x02",
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x102,
        (
            "#0102F#5Pそんな顔しないの。\x02\x03",

            "せっかくの可愛い顔が台無しよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x103,
        "#0205F#5P…………………………………\x02",
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x104,
        (
            "#0304F#5Pま、十年以上生きてりゃ、\x01",
            "お互い色々あるってことだろ。\x02\x03",

            "#0300Fまして俺たちは出会って\x01",
            "まだ一月くらいの関係だしな。\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x101,
        (
            "#0004F#5P年齢も性別も違う……\x01",
            "趣味も多分、バラバラだろう。\x02\x03",

            "それでも俺たちはこうして\x01",
            "仲間として一緒に行動してる……\x02\x03",

            "#0000F今は、それでいいんじゃないか？\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x103,
        "#0208F#5Pロイドさん、ランディさん……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0x1)
    Sleep(100)
    SetChrSubChip(0x103, 0x2)
    Sleep(100)
    SetChrSubChip(0x103, 0x3)
    Sleep(100)
    SetChrSubChip(0x103, 0x4)
    Sleep(300)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x103)

    #C0175
    ChrTalk(
        0x103,
        (
            "#0204F#5P……そうですね。\x02\x03",

            "#0202F少々、ナーバスに\x01",
            "なっていたみたいです。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0x4)
    Sleep(100)
    SetChrSubChip(0x103, 0x3)
    Sleep(100)
    SetChrSubChip(0x103, 0x2)
    Sleep(100)
    SetChrSubChip(0x103, 0x1)
    Sleep(100)
    SetChrSubChip(0x103, 0x0)
    Sleep(100)
    Fade(500)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x4)
    ClearChrFlags(0x103, 0x2)
    ClearChrFlags(0x103, 0x10)
    OP_93(0x103, 0xB4, 0x0)
    SetChrPos(0x102, 27070, 0, -9460, 180)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_0D()
    OP_93(0x103, 0x0, 0x12C)
    Sleep(300)

    #C0176
    ChrTalk(
        0x103,
        (
            "#0204F#12P……時間を取らせました。\x01",
            "セシルさんの所に行きましょう。\x02\x03",

            "#0202F調査結果を報告しないと。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x101,
        (
            "#0000F#5Pそうだな。\x01",
            "３階の病室に行ってみるか。\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(22580, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 26590, 0, -12170, 180)
    OP_50(0x66, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x66), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x63, 6)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_13_4DD4 end

    SaveToFile()

Try(main)
