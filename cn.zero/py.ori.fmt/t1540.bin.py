from ZeroScenarioHelper import *

def main():
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
        "实习医生利顿",           # 1
        "希伦护士",               # 2
        "菲莉亚护士",             # 3
        "玛萨护士长",             # 4
        "梅菲尔护士",             # 5
        "塞茜尔",                 # 6
        "诊断医生贝尔达因",       # 7
        "多诺邦警督",             # 8
        "雷蒙德搜查官",           # 9
        "住院患者",               # 10
        "住院患者",               # 11
        "住院患者",               # 12
        "住院患者",               # 13
        "住院患者",               # 14
        "女孩",                   # 15
        "住院患者",               # 16
        "住院患者",               # 17
        "住院患者",               # 18
        "住院患者",               # 19
        "住院患者",               # 20
        "住院患者",               # 21
        "住院患者",               # 22
        "住院患者",               # 23
        "住院患者",               # 24
        "住院患者",               # 25
        "住院患者",               # 26
        "住院患者",               # 27
        "住院患者",               # 28
        "住院患者",               # 29
        "住院患者",               # 30
        "住院患者",               # 31
        "住院患者",               # 32
        "住院患者",               # 33
        "住院患者",               # 34
        "住院患者",               # 35
        "住院患者",               # 36
        "黑月成员",               # 37
        "探视者",                 # 38
        "探视者",                 # 39
        "游客威利安",             # 40
        "约亚西姆副教授",         # 41
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
        "Function_8_2544",         # 08, 8
        "Function_9_25F7",         # 09, 9
        "Function_10_2F4D",        # 0A, 10
        "Function_11_3158",        # 0B, 11
        "Function_12_4419",        # 0C, 12
        "Function_13_48E8",        # 0D, 13
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
            "#1300F#12P就是这个病房……\x02\x03",

            "还有其他病人也在，\x01",
            "不要太吵闹哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x101,
        (
            "#0000F#5P嗯，没问题。\x01",
            "我们只是询问一下情况而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x136,
        (
            "#1309F#12P呵呵……\x01",
            "那就进去吧。\x02",
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
        "医生",
        (
            "#2404F#5P唔……\x01",
            "似乎恢复良好啊。\x02\x03",

            "#2400F嗯，这样的话，\x01",
            "明天应该就可以出院了吧。\x02",
        )
    )

    CloseMessageWindow()

    #N0005
    NpcTalk(
        0x8,
        "青年实习医生",
        "#4P真、真的吗！？\x02",
    )

    CloseMessageWindow()

    #N0006
    NpcTalk(
        0x30,
        "医生",
        (
            "#2400F#5P嗯，我不会说谎的。\x02\x03",

            "#2409F呵呵……\x01",
            "先做好出院之后的心理准备吧。\x02\x03",

            "我准备了堆积如山的工作\x01",
            "给你做呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #N0007
    NpcTalk(
        0x8,
        "青年实习医生",
        "#4P等一下啊，约亚西姆医生！？\x02",
    )

    CloseMessageWindow()

    #N0008
    NpcTalk(
        0x8,
        "青年实习医生",
        (
            "#4P对待伤势初愈的人，\x01",
            "怎么能这么残酷……\x02",
        )
    )

    CloseMessageWindow()

    #N0009
    NpcTalk(
        0x30,
        "医生",
        (
            "#2403F#5P只是划伤、磕碰和扭伤而已，\x01",
            "别说这么没出息的话。\x02\x03",

            "#2400F休息了这么久，\x01",
            "你的体力反而更加充沛了吧？\x02\x03",

            "#2409F嗯，一定能比以前\x01",
            "工作得更卖力吧。\x02",
        )
    )

    CloseMessageWindow()

    #N0010
    NpcTalk(
        0x8,
        "青年实习医生",
        (
            "#4P……医生，\x01",
            "是不是常有人说你是Ｓ？\x02",
        )
    )

    CloseMessageWindow()

    #N0011
    NpcTalk(
        0x30,
        "医生",
        (
            "#2403F#5P嗯～可我倒觉得\x01",
            "自己是Ｍ呢。\x02",
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
        "塞茜尔的声音",
        (
            "#4P真是的……\x01",
            "你们到底在说什么啊？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x30, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(-1940, 1000, -54350, 3000)

    def lambda_1B46():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x30, 1, lambda_1B46)
    WaitChrThread(0x30, 1)

    def lambda_1B57():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x136, 1, lambda_1B57)

    def lambda_1B6C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x136, 2, lambda_1B6C)
    Sleep(200)

    def lambda_1B80():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1B80)

    def lambda_1B95():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1B95)
    Sleep(100)

    def lambda_1BA9():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1BA9)

    def lambda_1BBE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1BBE)
    Sleep(150)

    def lambda_1BD2():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1BD2)

    def lambda_1BE7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1BE7)
    Sleep(150)

    def lambda_1BFB():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1BFB)

    def lambda_1C10():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1C10)
    WaitChrThread(0x136, 1)

    def lambda_1C25():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x136, 1, lambda_1C25)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)

    def lambda_1C3A():
        OP_93(0xFE, 0xE1, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1C3A)

    def lambda_1C47():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1C47)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    def lambda_1C5C():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1C5C)

    def lambda_1C69():
        OP_93(0xFE, 0xE1, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1C69)
    WaitChrThread(0x136, 1)

    def lambda_1C7A():
        OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x136, 1, lambda_1C7A)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    Sleep(100)

    def lambda_1C9A():
        OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1C9A)
    Sleep(100)

    def lambda_1CB2():
        OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1CB2)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    Sleep(80)

    def lambda_1CD2():
        OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1CD2)
    Sleep(80)

    def lambda_1CEA():
        OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1CEA)
    WaitChrThread(0x136, 1)

    def lambda_1D03():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x136, 1, lambda_1D03)
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
        "医生",
        "#2405F#6P哎呀……\x02",
    )

    CloseMessageWindow()

    #N0014
    NpcTalk(
        0x8,
        "青年实习医生",
        "#6P啊……塞茜尔小姐！\x02",
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x136,
        (
            "#1306F#11P你们两位真是的……\x01",
            "还有其他病人也在呢，\x01",
            "不要说些太奇怪的话哦。\x02\x03",

            "#1301F要是被小孩子听到怎么办呢？\x02",
        )
    )

    CloseMessageWindow()

    #N0016
    NpcTalk(
        0x8,
        "青年实习医生",
        "#6P对、对不起……\x02",
    )

    CloseMessageWindow()

    #N0017
    NpcTalk(
        0x30,
        "医生",
        "#2406F#6P哈哈，说不过你呢。\x02",
    )

    CloseMessageWindow()
    OP_63(0x30, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #N0018
    NpcTalk(
        0x30,
        "医生",
        "#2405F#6P哎呀，这几位是？\x02",
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x136,
        (
            "#1300F#11P克洛斯贝尔警察局的人。\x02\x03",

            "那个……就之前那次事件，\x01",
            "他们好像想直接听听\x01",
            "利顿医生的说法。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0020
    ChrTalk(
        0x8,
        "#6P啊……\x02",
    )

    CloseMessageWindow()

    #N0021
    NpcTalk(
        0x30,
        "医生",
        (
            "#2410F#6P原来如此，是这样啊。\x02\x03",

            "#2400F那我还是先\x01",
            "回避一下吧。\x02\x03",

            "正好也要到其它病房查房呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x136,
        (
            "#1302F#11P您辛苦了。\x02\x03",

            "#1300F……可不能偷懒哦。\x01",
            "比如偷跑出去，到水边钓鱼什么的。\x02",
        )
    )

    CloseMessageWindow()

    #N0023
    NpcTalk(
        0x30,
        "医生",
        (
            "#2405F#6P呃……\x01",
            "不会不会，我怎么会那样做。\x02\x03",

            "#2404F──那么，失陪了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2021():

        label("loc_2021")

        TurnDirection(0x101, 0x30, 500)
        Yield()
        Jump("loc_2021")

    QueueWorkItem2(0x101, 1, lambda_2021)

    def lambda_2033():

        label("loc_2033")

        TurnDirection(0x102, 0x30, 500)
        Yield()
        Jump("loc_2033")

    QueueWorkItem2(0x102, 1, lambda_2033)

    def lambda_2045():

        label("loc_2045")

        TurnDirection(0x103, 0x30, 500)
        Yield()
        Jump("loc_2045")

    QueueWorkItem2(0x103, 1, lambda_2045)

    def lambda_2057():

        label("loc_2057")

        TurnDirection(0x104, 0x30, 500)
        Yield()
        Jump("loc_2057")

    QueueWorkItem2(0x104, 1, lambda_2057)

    def lambda_2069():

        label("loc_2069")

        TurnDirection(0x136, 0x30, 500)
        Yield()
        Jump("loc_2069")

    QueueWorkItem2(0x136, 1, lambda_2069)

    def lambda_207B():
        OP_96(0xFE, 0xFFFFF8DA, 0x0, 0xFFFF220C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x136, 2, lambda_207B)
    BeginChrThread(0x30, 3, 0, 8)
    WaitChrThread(0x30, 3)
    WaitChrThread(0x136, 2)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x136, 0x1)
    SetChrFlags(0x30, 0x80)

    def lambda_20BC():
        TurnDirection(0xFE, 0x136, 300)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_20BC)

    def lambda_20C9():
        TurnDirection(0xFE, 0x136, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_20C9)

    def lambda_20D6():
        TurnDirection(0xFE, 0x136, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_20D6)

    def lambda_20E3():
        TurnDirection(0xFE, 0x136, 300)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_20E3)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0024
    ChrTalk(
        0x101,
        "#0005F#5P那个，刚才的人是？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x136, 0x101, 500)
    Sleep(300)

    #C0025
    ChrTalk(
        0x136,
        (
            "#1300F#12P他是约亚西姆医生，\x01",
            "是位副教授哦。\x02\x03",

            "#1306F虽然是位非常优秀的医生，\x01",
            "但是太过沉溺于个人的兴趣爱好……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x136, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x136, 0x13B, 0x1F4)
    OP_68(-2550, 1000, -54720, 3000)

    def lambda_21CA():
        OP_93(0xFE, 0xD7, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_21CA)

    def lambda_21D7():
        OP_93(0xFE, 0xD7, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_21D7)
    Sleep(100)

    def lambda_21E7():
        OP_93(0xFE, 0xD7, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_21E7)

    def lambda_21F4():
        OP_93(0xFE, 0xD7, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_21F4)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    def lambda_2211():
        OP_95(0xFE, -3180, 0, -55730, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x136, 1, lambda_2211)
    WaitChrThread(0x136, 1)

    def lambda_222F():
        OP_95(0xFE, -4030, 0, -55490, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x136, 1, lambda_222F)
    WaitChrThread(0x136, 1)

    def lambda_224D():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x136, 1, lambda_224D)
    WaitChrThread(0x136, 1)

    def lambda_225E():
        OP_9B(0x0, 0xFE, 0x0, 0x2EE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_225E)
    Sleep(50)

    def lambda_2276():
        OP_9B(0x0, 0xFE, 0x0, 0x2EE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2276)
    Sleep(100)

    def lambda_228E():
        OP_9B(0x0, 0xFE, 0x0, 0x2EE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_228E)
    Sleep(80)

    def lambda_22A6():
        OP_9B(0x0, 0xFE, 0x0, 0x2EE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_22A6)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x1)

    #C0026
    ChrTalk(
        0x136,
        (
            "#1300F#5P……那么，利顿医生。\x01",
            "能占用您一点时间吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x8,
        (
            "#6P嗯、嗯。\x01",
            "那倒是没问题……\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x8,
        (
            "#6P不过，为什么\x01",
            "克洛斯贝尔警察局的人会来呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x8,
        (
            "#6P负责这次事件调查的\x01",
            "不是警备队吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x101,
        (
            "#0003F#5P这个，警备队\x01",
            "似乎也无计可施了……\x02\x03",

            "#0001F所以我们就来\x01",
            "协助调查。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x8,
        "#6P是这样吗……\x02",
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x8,
        (
            "#6P嗯～他们果然认为\x01",
            "那只是我在做梦吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x8,
        (
            "#6P还是觉得我有梦游症？\x01",
            "不不，那应该不可能……\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x102,
        (
            "#0103F#11P那个，如果可以的话，\x01",
            "能不能请您从头说起？\x02\x03",

            "#0101F关于一周前的晚上发生的事情。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x8,
        "#6P啊，好的……\x02",
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
            "#11P──让我想想……\x01",
            "那件事发生在深夜，\x01",
            "当时我正好刚写完实习报告。\x02",
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

    def Function_8_2544(): pass

    label("Function_8_2544")


    def lambda_2549():
        OP_95(0xFE, 10, 0, -55640, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2549)
    WaitChrThread(0xFE, 1)

    def lambda_2567():
        OP_95(0xFE, 10, 0, -51540, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2567)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    ClearMapObjFlags(0x3, 0x10)
    OP_71(0x3, 0x0, 0xA, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x3)

    def lambda_25A7():
        OP_95(0xFE, 30, 0, -48960, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_25A7)
    Sleep(500)

    def lambda_25C4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_25C4)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Sleep(500)
    OP_71(0x3, 0xA, 0x0, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x3)
    SetMapObjFlags(0x3, 0x10)
    Return()

    # Function_8_2544 end

    def Function_9_25F7(): pass

    label("Function_9_25F7")

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
            "#4P……其实我的记忆\x01",
            "就到这里了。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x8,
        (
            "#4P第二天早上，勤杂工先生\x01",
            "在楼顶上发现了全身是伤，\x01",
            "已经晕过去的我……\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x8,
        (
            "#4P在办理了紧急住院手续之后，\x01",
            "就一直躺到了现在。\x02",
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
            "#0003F#5P……原来如此，\x01",
            "情况已经基本掌握了。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x104,
        (
            "#0301F#5P至于袭击你的那些魔兽，\x01",
            "你没有看清楚它们的样子吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x8,
        (
            "#4P哎呀，说到这里，实在难为情，\x01",
            "我好像是因为受惊过度而晕过去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x8,
        (
            "#4P只记得血红发光的眼睛\x01",
            "和白色的锐利牙齿，\x01",
            "还有黑色的皮毛……\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x8,
        (
            "#4P话说，警备队的人也向我确认过这些了，\x01",
            "他们认为我说的是狼，我也觉得的确很像。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x103,
        "#0203F#5P原来如此……\x02",
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x102,
        (
            "#0101F#5P那个……\x01",
            "您的伤势怎样？\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x8,
        (
            "#4P嗯，右肩上\x01",
            "有被牙咬过的痕迹。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x8,
        (
            "#4P但除此以外的伤\x01",
            "就只是磕伤碰伤和扭伤而已了。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x8,
        (
            "#4P我想，可能是被咬\x01",
            "之后就直接倒在了\x01",
            "地上吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x101,
        (
            "#0003F#5P……但不知为何，\x01",
            "魔兽却没有继续袭击你。\x02\x03",

            "#0001F奇怪的地方就在这里吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x8,
        "#4P对对，就是这样！\x02",
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x8,
        (
            "#4P那种情况下，就算被撕成碎片\x01",
            "也不奇怪呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x8,
        (
            "#4P而且地点还是楼顶，\x01",
            "所以警备队的人也都用充满怀疑的\x01",
            "目光看着我。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x8,
        (
            "#4P最后还怀疑我是不是\x01",
            "晚上迷迷糊糊地跑到郊外，\x01",
            "在外面被魔兽袭击的。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x103,
        (
            "#0200F#5P但是，你是在\x01",
            "这栋建筑物的楼顶被发现的吧……？\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x8,
        (
            "#4P嗯～但遭到袭击之后，惊惶失措地\x01",
            "逃到楼顶上，然后再晕过去……\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x8,
        "#4P这种可能性或许也并非为零吧。\x02",
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
            "#0006F#5P这、这个终究还是\x01",
            "不太可能吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x136,
        (
            "#1306F#11P真是的，利顿医生。\x02\x03",

            "#1301F遭遇袭击的你\x01",
            "怎么可以对自己的记忆\x01",
            "这么没有自信呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x8,
        "#4P呃，那个……对不起。\x02",
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x8,
        (
            "#4P可是，无法说明的事就这么\x01",
            "一直摆在那里，也会让人难以释怀吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x8,
        (
            "#4P与其那样的话，还不如相信\x01",
            "是自己的记忆模糊了，\x01",
            "反而会比较轻松……\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x8,
        (
            "#4P而且，如果真的有魔兽\x01",
            "出现在楼顶上，\x01",
            "……岂不是太可怕了吗？\x02",
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
            "#1306F#11P呼……你的心情\x01",
            "也不是无法理解。\x02\x03",

            "#1301F可是，如果真的是这样，\x01",
            "就更要认真思考对策……\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x101,
        (
            "#0003F#5P…………………………………………\x02\x03",

            "#0000F谢谢您的合作。\x02\x03",

            "我们也会再去调查一下\x01",
            "您遇袭的现场。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x8,
        "#4P啊，好的，拜托了。\x02",
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x8,
        (
            "#4P如果能给出说明\x01",
            "并采取对策的话，\x01",
            "就真是再好不过了。\x02",
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

    # Function_9_25F7 end

    def Function_10_2F4D(): pass

    label("Function_10_2F4D")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 7)), scpexpr(EXPR_END)), "loc_3026")

    #C0068
    ChrTalk(
        0x104,
        (
            "#12P#0300F那么……\x01",
            "这次是要去楼顶调查吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3053")

    label("loc_3026")


    #C0069
    ChrTalk(
        0x104,
        (
            "#12P#0300F那么……\x01",
            "就是这栋楼的楼顶吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3053")


    #C0070
    ChrTalk(
        0x101,
        (
            "#5P#0001F嗯，先去\x01",
            "实习医生遇袭的现场看看吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x136, 500)
    Sleep(300)

    #C0071
    ChrTalk(
        0x101,
        "#0005F#11P塞茜尔姐姐，时间没问题吗？\x02",
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x136,
        (
            "#6P#1306F对哦，休息时间\x01",
            "好像也快结束了……\x02\x03",

            "#1300F不过，我至少先把你们\x01",
            "带到利顿医生被发现的地方吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x101,
        "#0000F#11P嗯，拜托啦。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 27000, 0, -26000, 0)
    SetScenarioFlags(0x62, 2)
    EventEnd(0x5)
    Return()

    # Function_10_2F4D end

    def Function_11_3158(): pass

    label("Function_11_3158")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6A, 1)), scpexpr(EXPR_END)), "loc_3249")

    #C0074
    ChrTalk(
        0xA,
        "#5P啊，辛苦了～\x02",
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xA,
        "#5P调查的情况怎么样了～？\x02",
    )

    CloseMessageWindow()
    Jump("loc_3290")

    label("loc_3249")


    #C0076
    ChrTalk(
        0xA,
        "#5P啊，辛苦了～\x02",
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xA,
        (
            "#5P你们好像是警察吧？\x01",
            "调查的情况怎么样了～？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3290")


    #C0078
    ChrTalk(
        0x101,
        (
            "#0004F#6P嗯，基本查完一遍了。\x02\x03",

            "#0000F所以想跟塞茜尔姐姐……\x01",
            "不，是跟塞茜尔小姐\x01",
            "报告一下。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xA,
        "#5P啊，是这样吗～\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1200)

    #C0080
    ChrTalk(
        0xA,
        (
            "#5P呵呵……\x01",
            "话说回来，还真是和塞茜尔前辈\x01",
            "说得一模一样呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0081
    ChrTalk(
        0x101,
        "#0005F#6P哎……？\x02",
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xA,
        (
            "#5P呵呵，她经常\x01",
            "跟我们说起罗伊德呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xA,
        (
            "#5P塞茜尔前辈告诉我们你最近回到克洛斯贝尔了，\x01",
            "她看上去真的非常开心呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xA,
        (
            "#5P呵呵……\x01",
            "原来你这么可爱，那就可以理解了。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    #C0085
    ChrTalk(
        0x101,
        "#0011F#6P可、可爱……\x02",
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x103,
        "#0211F#6P（……一副猥琐的表情。）\x02",
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x102,
        (
            "#0103F#12P（真是的……\x01",
            "  在执勤中可真是不成体统呢。）\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0xE1, 0x1F4)

    #C0088
    ChrTalk(
        0x101,
        (
            "#0013F#5P（我、我才没有猥琐，\x01",
            "  也没有不成体统啦！）\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3512():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3512)
    WaitChrThread(0x104, 1)
    Sleep(300)

    #C0089
    ChrTalk(
        0x104,
        (
            "#0304F#12P（呼……\x01",
            "  好了，看着吧，罗伊德。）\x02\x03",

            "#0302F（这里就交给哥哥我好了。）\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x101,
        "#0005F#5P（哎……）\x02",
    )

    CloseMessageWindow()
    OP_68(23600, 1000, -700, 1000)

    def lambda_35A5():
        OP_95(0xFE, 22880, 0, -1560, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_35A5)

    def lambda_35BF():
        OP_96(0xFE, 0x5168, 0x0, 0xFFFFFA6A, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_35BF)

    def lambda_35D9():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_35D9)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x101, 2)
    OP_93(0x104, 0x2D, 0x1F4)
    Sleep(300)

    #C0091
    ChrTalk(
        0x104,
        (
            "#0309F#2P哈哈……\x01",
            "可爱这个词，应该用来\x01",
            "形容像你这样的女孩子呀。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0092
    ChrTalk(
        0xA,
        "#5P哎……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6A, 1)), scpexpr(EXPR_END)), "loc_369E")

    #C0093
    ChrTalk(
        0x104,
        (
            "#0304F#2P虽然我也同意\x01",
            "这小子很可爱就是了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3748")

    label("loc_369E")


    #C0094
    ChrTalk(
        0x104,
        (
            "#0302F#2P出言冒昧，抱歉了。\x01",
            "我叫兰迪。\x02\x03",

            "请问你的名字是……？\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xA,
        "#5P那个……我叫菲莉亚～\x02",
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xA,
        (
            "#5P兰迪先生\x01",
            "是罗伊德的同事吗～？\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x104,
        "#0304F#2P嗯，我也是一名警官哦。\x02",
    )

    CloseMessageWindow()

    label("loc_3748")

    Sleep(300)

    #C0098
    ChrTalk(
        0x104,
        (
            "#0302F#2P如何，作为友好的证明，\x01",
            "周末要不要一起开个联谊会？\x02\x03",

            "当然也会带这家伙去的，\x01",
            "而且我们这边也有女孩子，\x01",
            "大家一定都会玩得很开心哦。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_37DC():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_37DC)
    WaitChrThread(0x101, 1)

    #C0099
    ChrTalk(
        0x101,
        "#0001F#6P等、等一下……\x02",
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xA,
        "#5P嗯～这个嘛。\x02",
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xA,
        (
            "#5P我倒是偶尔也想放松一下，\x01",
            "要是找到行程安排合适的女孩，\x01",
            "我就邀请一下试试吧～\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3872():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3872)
    WaitChrThread(0x101, 1)

    #C0102
    ChrTalk(
        0x104,
        (
            "#0309F#2P嗯嗯，那就拜托啦。\x02\x03",

            "#0300F地点就定在克洛斯贝尔的酒馆怎么样？\x01",
            "就由我来负责订位吧。\x02",
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
        "#0200F#6P（……还真是滴水不漏啊。）\x02",
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x102,
        (
            "#0106F#12P（不愧是把搭讪\x01",
            "  当作兴趣爱好的人……）\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x101,
        (
            "#0006F#6P（话说，我们可是来找\x01",
            "  塞茜尔姐姐报告的啊……）\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x104,
        (
            "#0309F#2P哎呀～话说，还真是荣幸啊。\x02\x03",

            "能够与你这样的白衣天使\x01",
            "交上朋友。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xA,
        (
            "#5P哎～但我们这里的护士服\x01",
            "并不是白色的哦～\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0xA,
        "#5P那也没关系吗～？\x02",
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x104,
        (
            "#0304F#2P没问题啦。\x02\x03",

            "#0302F这套衣服也很可爱的，\x01",
            "而且更重要的是，穿着它的女孩们\x01",
            "也个个可爱超群。\x02\x03",

            "#0309F特别是你哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xA,
        "#5P讨厌～兰迪先生真是的。\x02",
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
        "中年女性的声音",
        (
            "哎呀，还说什么可爱超群，\x01",
            "真是让人不好意思呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_3B8F():
        OP_95(0xFE, 24940, 0, -190, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_3B8F)

    def lambda_3BA9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_3BA9)

    def lambda_3BBA():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3BBA)
    WaitChrThread(0xA, 1)
    Sleep(500)

    def lambda_3BCE():
        OP_96(0xFE, 0x5E10, 0x0, 0x258, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_3BCE)
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
        "#0305F#2P哎……\x02",
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xA,
        "#5P啊哈哈，护士长……\x02",
    )

    CloseMessageWindow()

    def lambda_3C3F():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_3C3F)
    WaitChrThread(0xB, 1)

    #C0114
    ChrTalk(
        0xB,
        "#2P你还有空说什么『啊哈哈』吗。\x02",
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0xB,
        (
            "#2P下午测量体温的工作完成了吗？\x01",
            "那是你负责的吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0116
    ChrTalk(
        0xA,
        "#5P啊……\x02",
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xB,
        (
            "#2P而且，说到周末，\x01",
            "你难道忘了这周末\x01",
            "还有个大手术吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xA,
        "#5P啊哈哈，是这样呢。\x02",
    )

    CloseMessageWindow()

    def lambda_3D2B():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3D2B)
    WaitChrThread(0xA, 1)

    #C0119
    ChrTalk(
        0xA,
        (
            "#5P抱歉哦，兰迪先生。\x01",
            "下次有机会再说吧～\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xA,
        "#5P罗伊德和诸位，下次见哦～！\x02",
    )

    CloseMessageWindow()

    def lambda_3D8D():

        label("loc_3D8D")

        TurnDirection(0x104, 0xA, 500)
        Yield()
        Jump("loc_3D8D")

    QueueWorkItem2(0x104, 1, lambda_3D8D)

    def lambda_3D9F():

        label("loc_3D9F")

        TurnDirection(0xB, 0xA, 500)
        Yield()
        Jump("loc_3D9F")

    QueueWorkItem2(0xB, 1, lambda_3D9F)

    def lambda_3DB1():
        OP_95(0xFE, 26210, 0, 1130, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3DB1)
    WaitChrThread(0xA, 1)

    def lambda_3DCF():
        OP_95(0xFE, 28770, 0, -20, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3DCF)
    WaitChrThread(0xA, 1)
    ClearMapObjFlags(0x2, 0x10)
    OP_71(0x2, 0x0, 0xA, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x2)

    def lambda_3E08():
        OP_95(0xFE, 31000, 0, 10, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3E08)
    Sleep(150)

    def lambda_3E25():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_3E25)
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
        "#0305F#2P哎……\x02",
    )

    CloseMessageWindow()

    def lambda_3E80():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_3E80)
    WaitChrThread(0xB, 1)

    #C0122
    ChrTalk(
        0xB,
        (
            "#5P不然的话，作为补偿，\x01",
            "这周末我就替她们陪你联谊吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0xB,
        (
            "#5P再怎么说，我也\x01",
            "同样算是个白衣天使吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x104,
        (
            "#0309F#2P还、还是不必了……啊哈哈。\x01",
            "这实在是消受不起啊。\x02\x03",

            "#0306F（换你上了……罗伊德。）\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x87, 0x1F4)

    def lambda_3F5E():
        OP_96(0xFE, 0x594C, 0x0, 0xFFFFF272, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3F5E)

    def lambda_3F78():
        OP_93(0xFE, 0x2D, 0x64)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_3F78)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x104, 2)

    #C0125
    ChrTalk(
        0x101,
        "#0001F#5P唉，真是的……\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x190)
    OP_68(23820, 1000, -720, 1000)

    def lambda_3FC2():
        OP_96(0xFE, 0x5492, 0x0, 0xFFFFFB14, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3FC2)
    WaitChrThread(0x101, 1)
    OP_6F(0x1)

    #C0126
    ChrTalk(
        0x101,
        (
            "#0006F#6P……不好意思。\x01",
            "我们刚才太吵闹了。\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x101, 2)

    def lambda_401A():
        OP_93(0xFE, 0x104, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_401A)
    WaitChrThread(0xB, 1)
    Sleep(300)

    #C0127
    ChrTalk(
        0xB,
        "#5P呼，算了。\x02",
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0xB,
        (
            "#5P话说回来，调查结束了吗？\x01",
            "你们好像是要找塞茜尔吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x101,
        (
            "#0000F#6P是的，已经基本查完一遍了。\x02\x03",

            "所以打算向她报告\x01",
            "几个已经查明的疑点。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0xB,
        (
            "#5P这个时间的话，塞茜尔\x01",
            "好像会去找那个孩子……\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xB,
        (
            "#5P嗯～用广播喊她\x01",
            "似乎也不太好……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x22, 0x24, 0xFA, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1200)

    #C0132
    ChrTalk(
        0xB,
        "#5P对了，你们几个。\x02",
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xB,
        (
            "#5P我想她现在应该在\x01",
            "楼上最里面的病房。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xB,
        "#5P你们能不能直接过去找她？\x02",
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
        "#0005F#6P病房……吗？\x02",
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x102,
        "#0105F#12P我们过去打扰不要紧吗？\x02",
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xB,
        (
            "#5P嗯，那间病房里住的是个\x01",
            "情况比较特殊的孩子。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xB,
        (
            "#5P可以的话，希望你们\x01",
            "也能去看看她。\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x101,
        (
            "#0000F#6P原来如此……\x01",
            "明白了。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x104,
        (
            "#0300F#12P适当陪她玩一会\x01",
            "就行了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xB,
        "#5P嗯，就是这样。\x02",
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xB,
        "#5P那么就拜托你们了。\x02",
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x103,
        "#0200F#6P………………………………\x02",
    )

    CloseMessageWindow()
    OP_93(0xB, 0x5A, 0x1F4)

    def lambda_433F():
        OP_95(0xFE, 28870, 0, 20, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_433F)
    WaitChrThread(0xB, 1)
    ClearMapObjFlags(0x2, 0x10)
    OP_71(0x2, 0x0, 0xA, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x2)

    def lambda_4378():
        OP_95(0xFE, 30850, 0, 10, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_4378)
    Sleep(200)

    def lambda_4395():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_4395)
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

    # Function_11_3158 end

    def Function_12_4419(): pass

    label("Function_12_4419")

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
        "#11P哎呀，是你们。\x02",
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0xB,
        (
            "#11P塞茜尔在\x01",
            "三楼最里面的病房。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0146
    ChrTalk(
        0xB,
        "#11P咦……？\x02",
    )

    CloseMessageWindow()
    OP_68(106400, 1000, 1500, 3000)

    def lambda_4522():

        label("loc_4522")

        TurnDirection(0x101, 0xB, 500)
        Yield()
        Jump("loc_4522")

    QueueWorkItem2(0x101, 2, lambda_4522)

    def lambda_4534():

        label("loc_4534")

        TurnDirection(0x102, 0xB, 500)
        Yield()
        Jump("loc_4534")

    QueueWorkItem2(0x102, 2, lambda_4534)

    def lambda_4546():

        label("loc_4546")

        TurnDirection(0x104, 0xB, 500)
        Yield()
        Jump("loc_4546")

    QueueWorkItem2(0x104, 2, lambda_4546)

    def lambda_4558():
        OP_96(0xFE, 0x19DFC, 0x0, 0x352, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_4558)
    Sleep(500)

    def lambda_4575():
        OP_96(0xFE, 0x1A2DE, 0x0, 0x1C2, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4575)
    Sleep(500)
    OP_63(0x103, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_45A4():
        OP_96(0xFE, 0x19884, 0x0, 0x352, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_45A4)
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
        "#0005F#11P护士长……？\x02",
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x103,
        "#0208F#6P#40W……您有什么事………？\x02",
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0149
    ChrTalk(
        0xB,
        "#11P果然没错！\x02",
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xB,
        "#11P你是缇欧吧！？\x02",
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
        "#0011F#11P哎……！？\x02",
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x102,
        "#0105F#5P为什么……\x02",
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x103,
        (
            "#0208F#6P#40W………………………………\x02\x03",

            "#0206F#40W……久疏……问候了。\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0xB,
        "#11P哈哈，果然是啊。\x02",
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0xB,
        (
            "#11P你长大了呢！\x01",
            "都长得这么漂亮了！\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xB,
        "#11P嗯，我都不敢认你了！\x02",
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
            "#5P哎，可是你怎么会和\x01",
            "这些小警察们……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xB, 0x10E, 0x190)

    #C0158
    ChrTalk(
        0xB,
        "#11P嗯～……？\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0xB, 1)

    #C0159
    ChrTalk(
        0x103,
        (
            "#0208F#6P#40W那个……\x01",
            "……有许多原因。\x02\x03",

            "#0203F#40W近期我会\x01",
            "再来打招呼……\x02\x03",

            "#0202F#40W今天要赶时间，先失陪了……\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0xB,
        "#11P嗯……\x02",
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xB,
        (
            "#11P──也是啊，\x01",
            "那下次有机会再慢慢聊吧。\x02",
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

    # Function_12_4419 end

    def Function_13_48E8(): pass

    label("Function_13_48E8")

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

    def lambda_4983():
        OP_95(0xFE, 26000, 0, -8800, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4983)

    def lambda_499D():
        OP_95(0xFE, 27600, 0, -8500, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_499D)

    def lambda_49B7():
        OP_95(0xFE, 26800, 0, -10400, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_49B7)

    def lambda_49D1():
        OP_95(0xFE, 26800, 0, -7500, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_49D1)
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
            "#0001F#5P缇欧……\x01",
            "你以前曾在这里住过院？\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0x103,
        (
            "#0208F#5P……嗯。\x02\x03",

            "大约是在六年之前。\x02\x03",

            "#0206F关于这点，其实我并没\x01",
            "打算刻意向大家隐瞒……\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0x104,
        "#0303F#5P唔……\x02",
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x101,
        (
            "#0006F#5P那个……该怎么说呢。\x02\x03",

            "#0000F不必太在意啦。\x01",
            "任何人都会有自己的\x01",
            "难言之隐……\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x103,
        "#0208F#5P……但是………\x02",
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x102)
    OP_68(27590, 1000, -9860, 1000)
    SetCameraDistance(23500, 1000)
    OP_95(0x102, 26970, 0, -9830, 2000, 0x0)
    Fade(500)

    def lambda_4B83():
        OP_A6(0xFE, 0x0, 0x1E, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_4B83)
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
        "#0104F#5P哎～\x02",
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0169
    ChrTalk(
        0x103,
        "#0205F#5P艾、艾莉前辈……？\x02",
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x102,
        (
            "#0102F#5P别摆出那种表情。\x02\x03",

            "你长得这么可爱，这样实在太浪费了哦。\x02",
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
            "#0304F#5P嗯，毕竟是活了十多年的人，\x01",
            "彼此都会有自己的秘密吧。\x02\x03",

            "#0300F更何况，从我们相遇到现在，\x01",
            "也不过才一个月左右。\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x101,
        (
            "#0004F#5P而且年龄和性别也不同……\x01",
            "兴趣多半也是南辕北辙吧。\x02\x03",

            "即使如此，我们还是像现在这样，\x01",
            "作为同伴，一起行动了……\x02\x03",

            "#0000F眼下，这样就已经足够了，不是吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x103,
        "#0208F#5P罗伊德前辈、兰迪前辈……\x02",
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
            "#0204F#5P……是呀。\x02\x03",

            "#0202F看来我似乎是\x01",
            "有点神经过敏了。\x02",
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
            "#0204F#12P……耽误了不少时间，\x01",
            "我们赶快去塞茜尔小姐那里吧。\x02\x03",

            "#0202F还要去报告调查结果呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x101,
        (
            "#0000F#5P是啊，\x01",
            "去三楼的病房看看吧。\x02",
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

    # Function_13_48E8 end

    SaveToFile()

Try(main)
