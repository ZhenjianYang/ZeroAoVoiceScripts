from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "c0250.bin",                # FileName
        "c0250",                    # MapName
        "c0250",                    # Location
        0x000E,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 14, 0, 6, 0, 7],
    )

    BuildStringList((
        "c0250",                  # 0
        "迈尔斯",                 # 1
        "雷缇",                   # 2
        "寇肯",                   # 3
        "寇肯",                   # 4
        "潘莎",                   # 5
        "隆",                     # 6
        "亨利",                   # 7
        "菲伊",                   # 8
        "菲伊",                   # 9
        "琪露露",                 # 10
        "卡缇莉娜",               # 11
        "小猫",                   # 12
    ))

    AddCharChip((
        "chr/ch20200.itc",                   # 00
        "chr/ch10300.itc",                   # 01
        "chr/ch21000.itc",                   # 02
        "chr/ch21002.itc",                   # 03
        "chr/ch22300.itc",                   # 04
        "chr/ch20600.itc",                   # 05
        "chr/ch22200.itc",                   # 06
        "chr/ch32700.itc",                   # 07
        "apl/ch50148.itc",                   # 08
        "chr/ch20500.itc",                   # 09
        "chr/ch24500.itc",                   # 0A
        "chr/ch39000.itc",                   # 0B
    ))

    DeclNpc(57950,   0,       103470,  90,   261,  0x0, 0,   0,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(51830,   0,       115930,  0,    261,  0x0, 0,   1,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(-51919,  0,       108370,  90,   261,  0x0, 0,   2,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(-51779,  150,     112519,  90,   469,  0x0, 0,   3,   0,   255, 255, 0,   14,  255,  0)
    DeclNpc(-54310,  0,       52840,   225,  261,  0x0, 0,   4,   0,   0,   3,   0,   15,  255,  0)
    DeclNpc(-58000,  0,       107489,  0,    389,  0x0, 0,   5,   0,   0,   0,   0,   18,  255,  0)
    DeclNpc(-57930,  0,       110510,  180,  389,  0x0, 0,   6,   0,   0,   0,   0,   19,  255,  0)
    DeclNpc(-54310,  0,       52840,   225,  389,  0x0, 0,   7,   0,   0,   0,   0,   20,  255,  0)
    DeclNpc(-51250,  500,     57180,   315,  469,  0x0, 0,   8,   0,   255, 255, 0,   20,  255,  0)
    DeclNpc(-57729,  0,       106739,  180,  389,  0x0, 0,   9,   0,   0,   0,   0,   21,  255,  0)
    DeclNpc(57950,   0,       103470,  90,   389,  0x0, 0,   10,  0,   0,   0,   0,   23,  255,  0)
    DeclNpc(-58200,  699,     108930,  225,  468,  0x0, 0,   11,  0,   0,   4,   255, 255, 255,  0)

    ScpFunction((
        "Function_0_298",          # 00, 0
        "Function_1_350",          # 01, 1
        "Function_2_37B",          # 02, 2
        "Function_3_3A6",          # 03, 3
        "Function_4_3D1",          # 04, 4
        "Function_5_431",          # 05, 5
        "Function_6_45C",          # 06, 6
        "Function_7_9A6",          # 07, 7
        "Function_8_A04",          # 08, 8
        "Function_9_1505",         # 09, 9
        "Function_10_317A",        # 0A, 10
        "Function_11_3800",        # 0B, 11
        "Function_12_397F",        # 0C, 12
        "Function_13_410A",        # 0D, 13
        "Function_14_42F8",        # 0E, 14
        "Function_15_4825",        # 0F, 15
        "Function_16_5995",        # 10, 16
        "Function_17_5B4F",        # 11, 17
        "Function_18_5C75",        # 12, 18
        "Function_19_6137",        # 13, 19
        "Function_20_64FE",        # 14, 20
        "Function_21_67A9",        # 15, 21
        "Function_22_69E2",        # 16, 22
        "Function_23_6C24",        # 17, 23
        "Function_24_6D04",        # 18, 24
        "Function_25_6DA3",        # 19, 25
        "Function_26_72FF",        # 1A, 26
        "Function_27_75CC",        # 1B, 27
        "Function_28_7DA7",        # 1C, 28
        "Function_29_8685",        # 1D, 29
        "Function_30_8BEE",        # 1E, 30
        "Function_31_8C1E",        # 1F, 31
        "Function_32_8C3A",        # 20, 32
    ))


    def Function_0_298(): pass

    label("Function_0_298")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_2D8"),
        (1, "loc_2E4"),
        (2, "loc_2F0"),
        (3, "loc_2FC"),
        (4, "loc_308"),
        (5, "loc_314"),
        (6, "loc_320"),
        (SWITCH_DEFAULT, "loc_32C"),
    )


    label("loc_2D8")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_338")

    label("loc_2E4")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_338")

    label("loc_2F0")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_338")

    label("loc_2FC")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_338")

    label("loc_308")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_338")

    label("loc_314")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_338")

    label("loc_320")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_338")

    label("loc_32C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_338")

    label("loc_338")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_34F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_338")

    label("loc_34F")

    Return()

    # Function_0_298 end

    def Function_1_350(): pass

    label("Function_1_350")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_37A")
    OP_94(0xFE, 0xCF80, 0x19938, 0xD890, 0x190AA, 0x3E8)
    Sleep(300)
    Jump("Function_1_350")

    label("loc_37A")

    Return()

    # Function_1_350 end

    def Function_2_37B(): pass

    label("Function_2_37B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3A5")
    OP_94(0xFE, 0xFFFF2676, 0x19C08, 0xFFFF2F22, 0x1A3CE, 0x3E8)
    Sleep(300)
    Jump("Function_2_37B")

    label("loc_3A5")

    Return()

    # Function_2_37B end

    def Function_3_3A6(): pass

    label("Function_3_3A6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3D0")
    OP_94(0xFE, 0xFFFF28BA, 0xC9A4, 0xFFFF30C6, 0xD2C8, 0x3E8)
    Sleep(300)
    Jump("Function_3_3A6")

    label("loc_3D0")

    Return()

    # Function_3_3A6 end

    def Function_4_3D1(): pass

    label("Function_4_3D1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_430")
    OP_94(0xFE, 0xFFFF1ED8, 0x1ABA8, 0xFFFF1A78, 0x1A7E8, 0x12C)
    Sleep(1200)
    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_419")
    Sleep(500)
    Jump("loc_42B")

    label("loc_419")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_42B")
    Sleep(800)

    label("loc_42B")

    Jump("Function_4_3D1")

    label("loc_430")

    Return()

    # Function_4_3D1 end

    def Function_5_431(): pass

    label("Function_5_431")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_45B")
    OP_94(0xFE, 0xFFFF2CD4, 0x1B5B2, 0xFFFF270C, 0x1A90A, 0x3E8)
    Sleep(300)
    Jump("Function_5_431")

    label("loc_45B")

    Return()

    # Function_5_431 end

    def Function_6_45C(): pass

    label("Function_6_45C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_4A1")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrPos(0xA, -54590, 0, 106800, 180)
    BeginChrThread(0xA, 0, 0, 2)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -51630, 0, 101720, 90)
    Jump("loc_9A5")

    label("loc_4A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_4EC")
    SetChrFlags(0x8, 0x80)
    SetChrPos(0x9, 57080, 0, 106510, 315)
    SetChrPos(0xA, -55660, 0, 105850, 90)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -54300, 0, 105850, 270)
    Jump("loc_9A5")

    label("loc_4EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_510")
    SetChrFlags(0x8, 0x80)
    SetChrPos(0x9, 57080, 0, 106510, 315)
    Jump("loc_9A5")

    label("loc_510")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_53E")
    SetChrFlags(0x8, 0x80)
    SetChrPos(0x9, 57080, 0, 106510, 315)
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    Jump("loc_9A5")

    label("loc_53E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_5AB")
    SetChrFlags(0x8, 0x80)
    SetChrPos(0x9, 57950, 0, 103470, 90)
    SetChrPos(0xC, -54920, 0, 51450, 90)
    BeginChrThread(0xC, 0, 0, 0)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, -53650, 0, 51450, 270)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -54530, 0, 106440, 180)
    BeginChrThread(0x11, 0, 0, 2)
    Jump("loc_9A5")

    label("loc_5AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_600")
    SetChrPos(0x9, 57080, 0, 106510, 315)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -57280, 0, 114110, 0)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, -58290, 0, 114110, 90)
    Jump("loc_9A5")

    label("loc_600")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_66C")
    SetChrPos(0x8, 54190, 0, 103940, 270)
    BeginChrThread(0x8, 0, 0, 1)
    SetChrPos(0x9, 57080, 0, 106510, 315)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -53150, 0, 112450, 0)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, -54140, 0, 112450, 0)
    Jump("loc_9A5")

    label("loc_66C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_6D2")
    SetChrPos(0x8, 54410, 0, 103050, 90)
    SetChrPos(0x9, 55730, 0, 103050, 270)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -51530, 0, 102490, 180)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, -51530, 0, 101260, 0)
    Jump("loc_9A5")

    label("loc_6D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_6EF")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xC, 0x80)
    Jump("loc_9A5")

    label("loc_6EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_756")
    SetChrPos(0x8, 57080, 0, 106510, 315)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -53130, 0, 105180, 0)
    SetChrPos(0xA, -53120, 0, 106320, 180)
    SetChrPos(0xC, -52650, 0, 54740, 45)
    BeginChrThread(0xC, 0, 0, 0)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    Jump("loc_9A5")

    label("loc_756")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_784")
    SetChrFlags(0x8, 0x80)
    SetChrPos(0x9, 57080, 0, 106510, 315)
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    Jump("loc_9A5")

    label("loc_784")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_7C9")
    SetChrFlags(0x8, 0x80)
    SetChrPos(0x9, 57080, 0, 106510, 315)
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xC, -51660, 0, 46480, 90)
    BeginChrThread(0xC, 0, 0, 0)
    Jump("loc_9A5")

    label("loc_7C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_7FC")
    SetChrFlags(0x8, 0x80)
    SetChrPos(0x9, 57080, 0, 106510, 315)
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    Jump("loc_9A5")

    label("loc_7FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_825")
    SetChrFlags(0x8, 0x80)
    SetChrPos(0x9, 57080, 0, 106510, 315)
    SetChrFlags(0xC, 0x80)
    Jump("loc_9A5")

    label("loc_825")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_85C")
    SetChrFlags(0x8, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_857")
    BeginChrThread(0xC, 0, 0, 0)
    SetChrPos(0xC, -58260, 0, 58850, 0)

    label("loc_857")

    Jump("loc_9A5")

    label("loc_85C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_930")
    SetChrFlags(0x8, 0x80)
    SetChrPos(0xA, -10020, 0, 3600, 0)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8A9")
    BeginChrThread(0xC, 0, 0, 0)
    SetChrPos(0xC, -58260, 0, 58850, 0)

    label("loc_8A9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_8E2")
    SetChrPos(0xD, -54470, 0, 110810, 315)
    SetChrPos(0xE, -57280, 0, 107430, 315)
    BeginChrThread(0xD, 0, 0, 5)
    Jump("loc_92B")

    label("loc_8E2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x2)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_926")
    SetChrPos(0xD, -57650, 0, 110300, 180)
    SetChrPos(0xE, -58450, 0, 110300, 180)
    Jump("loc_92B")

    label("loc_926")

    ClearChrFlags(0x13, 0x80)

    label("loc_92B")

    Jump("loc_9A5")

    label("loc_930")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_978")
    SetChrFlags(0x8, 0x80)
    SetChrPos(0x9, 57080, 0, 106510, 315)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_973")
    BeginChrThread(0xC, 0, 0, 0)
    SetChrPos(0xC, -58260, 0, 58850, 0)

    label("loc_973")

    Jump("loc_9A5")

    label("loc_978")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_99C")
    SetChrFlags(0x8, 0x80)
    SetChrPos(0x9, 57080, 0, 106510, 315)
    Jump("loc_9A5")

    label("loc_99C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_9A5")

    label("loc_9A5")

    Return()

    # Function_6_45C end

    def Function_7_9A6(): pass

    label("Function_7_9A6")

    OP_52(0x10, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9CA")
    OP_10(0x0, 0x0)
    OP_10(0xD, 0x1)
    Jump("loc_9D0")

    label("loc_9CA")

    OP_10(0x0, 0x1)
    OP_10(0xD, 0x0)

    label("loc_9D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9EC")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_A03")

    label("loc_9EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_A03")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_A03")

    label("loc_A03")

    Return()

    # Function_7_9A6 end

    def Function_8_A04(): pass

    label("Function_8_A04")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_AA3")

    #C0001
    ChrTalk(
        0xFE,
        "今天就是纪念庆典的最后一天了呢。\x02",
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "这个庆典本来的目的就是\x01",
            "庆祝自治州的成立以及和平。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xFE,
        (
            "今天真想悠闲地度过，\x01",
            "再好好思考一些事情啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1501")

    label("loc_AA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 7)), scpexpr(EXPR_END)), "loc_B69")
    TurnDirection(0xFE, 0x101, 0)

    #C0004
    ChrTalk(
        0xFE,
        (
            "罗伊德，找到\x01",
            "迷路的孩子了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        (
            "他的父母一定\x01",
            "也很担心吧。\x01",
            "快点帮他们寻找吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B61")

    #C0006
    ChrTalk(
        0x101,
        (
            "#0000F嗯，没关系的，所在地\x01",
            "暂且也已经找到了……\x02\x03",

            "刚才的事谢谢您了，叔叔。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B61")

    SetScenarioFlags(0x0, 0)
    Jump("loc_1501")

    label("loc_B69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_E35")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAD, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D80")

    #C0007
    ChrTalk(
        0x101,
        (
            "#0003F（迈尔斯叔叔应该去\x01",
            "　看了游行……\x01",
            "　总之先问问看吧。）\x02\x03",

            "#0000F叔叔，稍微打扰一下可以吗？\x01",
            "有些事情想要问您。\x02",
        )
    )

    CloseMessageWindow()

    #A0008
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德出示了柯林的照片，\x01",
            "并询问对方是否有什么线索。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0009
    ChrTalk(
        0xFE,
        "哎呀，这个孩子是？\x02",
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        (
            "……果然没错呢，\x01",
            "确实是我刚才遇见过的孩子。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x101,
        "#0005F真的吗……？！\x02",
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xFE,
        (
            "嗯，是在东街遇见的。\x01",
            "他险些从后面\x01",
            "撞到我。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        (
            "之后似乎是向北面\x01",
            "跑去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x160,
        (
            "#3308F从东街向北的话……\x01",
            "就是港湾区一带了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x101,
        (
            "#0003F嗯，应该是那样。\x02\x03",

            "#0000F……叔叔，谢谢您。\x01",
            "您的信息给了我们很大帮助。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xAD, 1)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 24)
    Jump("loc_E30")

    label("loc_D80")


    #C0016
    ChrTalk(
        0xFE,
        (
            "确实是我刚才遇到的\x01",
            "那个活泼的小男孩。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        (
            "我是在东街的十字路口见到他的，\x01",
            "但他之后似乎\x01",
            "又向北边跑去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        (
            "……迷路的孩子啊，还真令人担心呢……\x01",
            "罗伊德，请尽快找到他吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E30")

    Jump("loc_1501")

    label("loc_E35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_E94")

    #C0019
    ChrTalk(
        0xFE,
        "哎呀，人真是好多呢。\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        (
            "哈哈哈，我已经这么大年纪了，\x01",
            "当时都差点迷了路呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1501")

    label("loc_E94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_F3B")

    #C0021
    ChrTalk(
        0xFE,
        (
            "我们正准备\x01",
            "出去看游行呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xFE,
        (
            "哈哈，约你们去的话，\x01",
            "终究还是不太方便吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        "……工作的时候要小心哦。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F33")

    #C0024
    ChrTalk(
        0x101,
        "#0000F嗯，谢谢您了，叔叔。\x02",
    )

    CloseMessageWindow()

    label("loc_F33")

    SetScenarioFlags(0x0, 0)
    Jump("loc_1501")

    label("loc_F3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_10B4")
    TurnDirection(0xFE, 0x101, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1051")

    #C0025
    ChrTalk(
        0xFE,
        "哦哦，这不是罗伊德嘛。\x02",
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xFE,
        (
            "是吗，你们从今天开始\x01",
            "就要重新开始工作了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x101,
        (
            "#0000F嗯，因为我们也算是正式的警察啊。\x02\x03",

            "叔叔，\x01",
            "您是从今天开始休假吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xFE,
        (
            "是啊，我准备和你阿姨一起\x01",
            "好好逛逛。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        (
            "塞茜尔要是能一起去就好了，\x01",
            "可那孩子非常忙呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_10AF")

    label("loc_1051")


    #C0030
    ChrTalk(
        0xFE,
        (
            "庆典期间人那么多，还要维持秩序，\x01",
            "警察们很辛苦吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        (
            "你们也要适当休息啊，\x01",
            "可别累坏了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10AF")

    Jump("loc_1501")

    label("loc_10B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_1501")
    TurnDirection(0xFE, 0x101, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1358")

    #C0032
    ChrTalk(
        0x101,
        (
            "#0000F叔叔，\x01",
            "好久不见。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        (
            "哦？你不是……\x01",
            "以前住在隔壁的罗伊德嘛！\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        "哈哈哈，实在是吃了一惊啊！\x02",
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        (
            "虽然听说过你快回来了，……但没想到你\x01",
            "都长这么大了，简直让人认不出来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x101,
        (
            "#0012F呵呵，只是身高长了，\x01",
            "但内在还是很不成熟呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        (
            "没那回事。\x01",
            "你不是已经顺利\x01",
            "通过搜查官考试了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xFE,
        (
            "盖伊一定\x01",
            "也会为你高兴的。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x101,
        (
            "#0008F……会吗？\x02\x03",

            "……如果真是那样就好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xFE,
        "嗯，一定会的。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12CE")

    #C0041
    ChrTalk(
        0xFE,
        (
            "对了，去厨房跟你阿姨\x01",
            "打声招呼吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xFE,
        "她一定会非常高兴的。\x02",
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x101,
        (
            "#0000F哈哈哈……也是呢。\x01",
            "那我这就去。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1350")

    label("loc_12CE")


    #C0044
    ChrTalk(
        0xFE,
        (
            "我经常因为工作不在家，\x01",
            "不过你阿姨一般都在。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xFE,
        (
            "如果有什么需要帮忙的，\x01",
            "……就过去找她哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x101,
        "#0000F嗯，那又要麻烦两位了。\x02",
    )

    CloseMessageWindow()

    label("loc_1350")

    SetScenarioFlags(0x4D, 7)
    Jump("loc_1501")

    label("loc_1358")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14BB")

    #C0047
    ChrTalk(
        0xFE,
        (
            "你竟然都\x01",
            "长这么大啦……\x01",
            "哈哈，我也上年纪了。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xFE,
        "你跟塞茜尔联系过了吗？\x02",
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x101,
        (
            "#0000F嗯，用导力通讯联系过了。\x02\x03",

            "本来我想趁着这次休假\x01",
            "去见见她的……\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xFE,
        (
            "是吗。\x01",
            "嗯，那就好。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xFE,
        (
            "不管怎样，你对我们来说，就跟家人一样。\x01",
            "你回来我就放心了。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xFE,
        (
            "我经常因为工作不在家，\x01",
            "不过你阿姨一般都在。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xFE,
        (
            "如果有什么需要帮忙的，\x01",
            "……就来找你阿姨哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1501")

    label("loc_14BB")


    #C0054
    ChrTalk(
        0xFE,
        (
            "我们都把你当成家人，\x01",
            "如果有什么需要帮忙的，\x01",
            "……就来找你阿姨哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1501")

    TalkEnd(0xFE)
    Return()

    # Function_8_A04 end

    def Function_9_1505(): pass

    label("Function_9_1505")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_151E")
    Call(0, 25)
    TalkEnd(0xFE)
    Return()

    label("loc_151E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8F, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1880")

    #C0055
    ChrTalk(
        0x101,
        (
            "#0000F阿姨，好久不见了。\x02\x03",

            "#0006F……不好意思，最近我有点忙，\x01",
            "好像很久没来打招呼了。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xFE,
        "啊，这不是罗伊德嘛。\x02",
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xFE,
        (
            "听说你们最近\x01",
            "很活跃啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xFE,
        (
            "好像还登上了\x01",
            "克洛斯贝尔时代周刊吧？\x01",
            "呵呵，阿姨真为你们自豪～\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xFE,
        (
            "来来，快让阿姨\x01",
            "好好得意一下！\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x104,
        (
            "#0300F那么阿姨，\x01",
            "我就来说说我的英雄事迹吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x102,
        (
            "#0102F呵呵，\x01",
            "虽然吃了不少苦头……\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x103,
        (
            "#0202F对了，如果您有什么需要，\x01",
            "可以来找我们\x01",
            "特别任务支援科。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x101)

    #C0063
    ChrTalk(
        0x101,
        (
            "#0006F那、那个，你们……\x01",
            "该说是脸皮厚吗……\x02\x03",

            "最近对阿姨\x01",
            "是不是越来越不懂得客气了？\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x102,
        (
            "#0100F呵呵，有什么关系嘛。\x01",
            "阿姨不是塞茜尔小姐的妈妈吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x104,
        (
            "#0300F就是就是，我们还\x01",
            "时不时就来蹭个饭，\x01",
            "不是就跟家人一样吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xFE,
        (
            "对啊，罗伊德，\x01",
            "你们千万别客气啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xFE,
        (
            "……大家也要\x01",
            "再来玩哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x104,
        "#0300F好啊～！\x02",
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x102,
        "#0100F好的。\x02",
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x103,
        "#0200F……收到。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0071
    ChrTalk(
        0x101,
        (
            "#0006F（大家果然都\x01",
            "　很不客气呢……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x8F, 6)
    TalkEnd(0xFE)
    Return()

    label("loc_1880")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_188E")
    Jump("loc_3176")

    label("loc_188E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_18D6")

    #C0072
    ChrTalk(
        0xFE,
        (
            "今天要到大圣堂\x01",
            "去做祈祷。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xFE,
        (
            "得早点\x01",
            "做好准备才行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3176")

    label("loc_18D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1AA2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A37")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0074
    ChrTalk(
        0xFE,
        "啊，缇欧你……\x02",
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x103,
        "#0200F嗯，怎么了？\x02",
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xFE,
        (
            "总觉得你脸色\x01",
            "有点差呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xFE,
        "大概只是我的错觉吧。\x02",
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x103,
        (
            "#0208F……应该是昨天对『僧院』\x01",
            "的调查太累了。\x02\x03",

            "#0203F那个，我的确是\x01",
            "逞强了些。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x104,
        (
            "#0300F因为阿缇的感应能力\x01",
            "每次都能派上大用场嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x101,
        (
            "#0000F确实……\x01",
            "缇欧，别太过勉强哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x103,
        "#0202F嗯，我知道的。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1A9D")

    label("loc_1A37")


    #C0082
    ChrTalk(
        0xFE,
        (
            "虽然不知道具体怎么回事，\x01",
            "但昨天好像很辛苦啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xFE,
        (
            "疲惫的时候千万不可以勉强哦，\x01",
            "要好好休息才行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A9D")

    Jump("loc_3176")

    label("loc_1AA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1E4F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DB3")

    #C0084
    ChrTalk(
        0x104,
        (
            "#0300F您好啊，\x01",
            "塞茜尔小姐的妈妈，\x01",
            "好久不见了！\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x102,
        "#0102F好久不见。\x02",
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x101,
        (
            "#0006F阿姨，实在不好意思，\x01",
            "每次都带着一群人来打扰您。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0xFE,
        (
            "呵呵，没关系啦。\x01",
            "大家都很精神啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xFE,
        (
            "看起来今天\x01",
            "也在努力工作呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0089
    ChrTalk(
        0xFE,
        (
            "啊……那个孩子\x01",
            "是第一次来吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0xFE,
        (
            "是支援科的新成员吗？\x01",
            "呵呵，又来了个这么可爱的女孩子。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1C39")
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    label("loc_1C39")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1C7A")
    OP_63(0x109, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x109)

    label("loc_1C7A")


    #C0091
    ChrTalk(
        0x109,
        (
            "#0505F您、您是说我可、可爱吗……\x02\x03",

            "我、我其实是警备队成员，\x01",
            "今天是来向特别任务支援科\x01",
            "寻求协助的……！\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x104,
        "#0300F诺艾尔，放松放松。\x02",
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x109,
        (
            "#0505F不、不好意思，不禁就……\x02\x03",

            "#0503F因为这还是第一次\x01",
            "有人说、说我可爱。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x103,
        (
            "#0200F（……发现了诺艾尔小姐\x01",
            "　令人意外的弱点。）\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xFE,
        (
            "呵呵，果然是个\x01",
            "可爱的孩子嘛～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xCE, 0)
    Jump("loc_1E4A")

    label("loc_1DB3")


    #C0096
    ChrTalk(
        0xFE,
        (
            "原来是警备队的啊。\x01",
            "不用紧张，放轻松就好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x109,
        (
            "#0501F是……诺艾尔·希卡，\x01",
            "已经收到命令！\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x101,
        (
            "#0000F（诺艾尔上士……\x01",
            "　好像还是有点紧张啊……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E4A")

    Jump("loc_3176")

    label("loc_1E4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_1EF4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAF, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E6A")
    Call(0, 10)
    Jump("loc_1EEF")

    label("loc_1E6A")


    #C0099
    ChrTalk(
        0xFE,
        (
            "呵呵，小琪雅也\x01",
            "很喜欢看书吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xFE,
        (
            "下次给她准备一些\x01",
            "适合小孩子看的书好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xFE,
        (
            "只要和你叔叔说一声，\x01",
            "他肯定会很乐意帮忙找来的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EEF")

    Jump("loc_3176")

    label("loc_1EF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1FCF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F99")

    #C0102
    ChrTalk(
        0xFE,
        "啊，这不是罗伊德和各位嘛。\x02",
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xFE,
        (
            "在纪念庆典中已经玩够了，\x01",
            "所以今天想悠闲地度过。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xFE,
        (
            "当然啦，庆典结束时要放的礼花，\x01",
            "我还是会去看的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1FCA")

    label("loc_1F99")


    #C0105
    ChrTalk(
        0xFE,
        (
            "呵呵，偶尔跟你叔叔一起\x01",
            "悠闲度日倒也不错呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FCA")

    Jump("loc_3176")

    label("loc_1FCF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 7)), scpexpr(EXPR_END)), "loc_2075")

    #C0106
    ChrTalk(
        0xFE,
        (
            "看游行的人太多，\x01",
            "所以才和父母走散了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xFE,
        (
            "罗伊德，这就是你们警察出马的时候了，\x01",
            "快点去找找吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_206D")

    #C0108
    ChrTalk(
        0x101,
        (
            "#0000F嗯……\x01",
            "各位，我们快点吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_206D")

    SetScenarioFlags(0x0, 1)
    Jump("loc_3176")

    label("loc_2075")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_211D")

    #C0109
    ChrTalk(
        0xFE,
        (
            "哎呀，罗伊德，\x01",
            "你在找那个迷路的孩子吗……？\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xFE,
        (
            "话说回来，你叔叔他好像\x01",
            "遇到过一个小孩子。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0xFE,
        (
            "那孩子只有自己一个人，\x01",
            "我还在奇怪\x01",
            "他父母去哪里了呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3176")

    label("loc_211D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_2226")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21E1")

    #C0112
    ChrTalk(
        0xFE,
        (
            "嗯，来看游行的人\x01",
            "好多啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xFE,
        "罗伊德，你们没事吧？\x02",
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x101,
        (
            "#0012F啊哈哈，其实……\x01",
            "今天我们错过看游行了。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0xFE,
        "啊，真的吗！？\x02",
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0xFE,
        (
            "真遗憾啊……\x01",
            "今年的游行特别好看哦！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2221")

    label("loc_21E1")


    #C0117
    ChrTalk(
        0xFE,
        (
            "对了，阿姨我拍了\x01",
            "不少照片呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xFE,
        (
            "到时也送给你们\x01",
            "几张吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2221")

    Jump("loc_3176")

    label("loc_2226")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_227A")

    #C0119
    ChrTalk(
        0xFE,
        (
            "游行好像\x01",
            "快要开始了哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xFE,
        (
            "呵呵，要是塞茜尔也能\x01",
            "一起去就好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3176")

    label("loc_227A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2389")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_233A")

    #C0121
    ChrTalk(
        0xFE,
        (
            "你叔叔今天\x01",
            "出门了哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x101,
        (
            "#0005F咦，阿姨您怎么\x01",
            "没一起去啊……？\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0xFE,
        (
            "嗯，市政厅大会堂\x01",
            "那里要召开一场\x01",
            "国际研讨会。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xFE,
        (
            "呵呵，你叔叔他\x01",
            "对这种活动最没抵抗力了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2384")

    label("loc_233A")


    #C0125
    ChrTalk(
        0xFE,
        (
            "所以我就自己在家\x01",
            "等他回来。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0xFE,
        (
            "哎呀呀，我趁现在\x01",
            "给你们做点吃的吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2384")

    Jump("loc_3176")

    label("loc_2389")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_257A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2529")

    #C0127
    ChrTalk(
        0x101,
        (
            "#0000F啊，阿姨……\x02\x03",

            "#0009F昨天承蒙款待，\x01",
            "您做的饭菜真好吃。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0xFE,
        (
            "呵呵，招待不周，\x01",
            "有空再来玩哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x103,
        (
            "#0200F……罗伊德前辈\x01",
            "来了塞茜尔小姐\x01",
            "的家里呀。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x104,
        (
            "#0301F喂，罗伊德，为什么\x01",
            "没叫我们一起来啊？\x02\x03",

            "#0306F我也想跟\x01",
            "塞茜尔姐姐待在一起啊～\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0131
    ChrTalk(
        0x101,
        (
            "#0006F明明都和塞茜尔姐\x01",
            "的后辈们约会了，\x01",
            "还敢这么说……\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x102,
        "#0111F真是一点节操也没有呢……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2575")

    label("loc_2529")


    #C0133
    ChrTalk(
        0xFE,
        (
            "呵呵，等一下我要和你叔叔\x01",
            "一起去看庆典。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xFE,
        (
            "大家要加油，\x01",
            "好好工作哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2575")

    Jump("loc_3176")

    label("loc_257A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_2730")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26F3")

    #C0135
    ChrTalk(
        0xFE,
        "啊，欢迎欢迎。\x02",
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xFE,
        (
            "罗伊德，你们\x01",
            "又要去哪里了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x101,
        (
            "#0000F嗯，还有点事情\x01",
            "需要调查。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xFE,
        (
            "呵呵，看到你们每天都这么\x01",
            "努力工作，我真高兴。\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0xFE,
        (
            "下次要好好讲给我听啊，\x01",
            "阿姨很期待\x01",
            "你们的活跃表现。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x102,
        "#0100F嗯，那是我们的荣幸。\x02",
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x101,
        (
            "#0003F（彩虹剧团的事情，\x01",
            "　必须暂时保密呢……）\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x104,
        (
            "#0301F（是啊。\x01",
            "　真想快点把事情解决，\x01",
            "　回来说给阿姨听啊。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_272B")

    label("loc_26F3")


    #C0143
    ChrTalk(
        0xFE,
        (
            "下次要好好讲给我听啊，\x01",
            "阿姨很期待\x01",
            "你们的活跃表现。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_272B")

    Jump("loc_3176")

    label("loc_2730")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2913")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28BA")

    #C0144
    ChrTalk(
        0xFE,
        (
            "………………………………\x01",
            "……罗伊德？\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x101,
        "#0005F咦？怎么了，阿姨？\x02",
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xFE,
        (
            "总觉得你好像越来越\x01",
            "成熟了哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0xFE,
        (
            "呵呵，长得也跟\x01",
            "盖伊越来越像了。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x101,
        (
            "#0012F哈哈，是吗？\x01",
            "可能是因为年纪大了吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x104,
        (
            "#0304F应该是因为昨晚\x01",
            "那件事……（小声）\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x103,
        (
            "#0204F让他登上……\x01",
            "成为大人的阶梯了吧。（小声）\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 0)

    #C0151
    ChrTalk(
        0x101,
        (
            "#0011F不、不是都说过\x01",
            "完全没有那种事吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x102,
        "#0106F#2S呼……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_290E")

    label("loc_28BA")


    #C0153
    ChrTalk(
        0xFE,
        (
            "罗伊德，最近你看上去\x01",
            "好像越来越成熟了哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0xFE,
        (
            "呵呵，长得也跟\x01",
            "盖伊越来越像了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_290E")

    Jump("loc_3176")

    label("loc_2913")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_298A")

    #C0155
    ChrTalk(
        0xFE,
        (
            "下个月的纪念庆典\x01",
            "应该会很热闹吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xFE,
        (
            "不知道塞茜尔\x01",
            "会不会放假。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xFE,
        (
            "下次一定\x01",
            "要好好向她确认一下。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3176")

    label("loc_298A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_29CF")

    #C0158
    ChrTalk(
        0xFE,
        (
            "支援科的各位，\x01",
            "千万别客气。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xFE,
        "有空就常来玩哦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3176")

    label("loc_29CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_2B4A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29EB")
    Call(0, 11)
    Jump("loc_2B45")

    label("loc_29EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x70, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29FD")
    Call(0, 26)
    Jump("loc_2B45")

    label("loc_29FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AED")

    #C0160
    ChrTalk(
        0xFE,
        (
            "那孩子也长大了，\x01",
            "虽然我们并不打算\x01",
            "现在就开始对她说教，\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xFE,
        (
            "但是……她差不多也该\x01",
            "考虑考虑自己的未来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0xFE,
        (
            "对了，今天去大圣堂\x01",
            "帮她祈祷下，\x01",
            "希望她能有个好姻缘吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x101,
        (
            "#0006F（心情好复杂……\x01",
            "　心情真的好复杂啊……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2B45")

    label("loc_2AED")


    #C0164
    ChrTalk(
        0xFE,
        (
            "我今天下午\x01",
            "要去大圣堂祈祷哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0xFE,
        (
            "顺便也帮塞茜尔祈祷一下，\x01",
            "希望她能有份好姻缘吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B45")

    Jump("loc_3176")

    label("loc_2B4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_2CA0")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B66")
    Call(0, 11)
    Jump("loc_2C9B")

    label("loc_2B66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C5E")

    #C0166
    ChrTalk(
        0xFE,
        (
            "塞茜尔也真是的，整天就知道工作，\x01",
            "连周末也不回家。\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0xFE,
        (
            "我明明还没\x01",
            "把她嫁出去呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0x101,
        (
            "#0012F算了算了，阿姨……\x01",
            "塞茜尔姐姐\x01",
            "好像真的很忙。\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0xFE,
        (
            "嗯，这个我也知道。但是，\x01",
            "做母亲的偶尔也想见见她啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0xFE,
        (
            "至少也应该\x01",
            "回来吃顿饭吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2C9B")

    label("loc_2C5E")


    #C0171
    ChrTalk(
        0xFE,
        (
            "塞茜尔整天就只知道工作工作的……\x01",
            "至少周末也应该回来吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C9B")

    Jump("loc_3176")

    label("loc_2CA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_2E10")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CBC")
    Call(0, 11)
    Jump("loc_2E0B")

    label("loc_2CBC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DC3")

    #C0172
    ChrTalk(
        0xFE,
        "啊，这不是罗伊德嘛。\x02",
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0xFE,
        (
            "有段时间没见了，\x01",
            "在努力工作吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x101,
        "#0000F哈哈，算是吧。\x02",
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0x104,
        "#0300F虽然都是些无关紧要的工作。\x02",
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0xFE,
        (
            "呵呵，每个人刚开始\x01",
            "都是这样的。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0xFE,
        (
            "要好好加油哦。\x01",
            "盖伊肯定也\x01",
            "会守护你们的。\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x101,
        (
            "#0008F……嗯。\x01",
            "谢谢您，阿姨。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2E0B")

    label("loc_2DC3")


    #C0179
    ChrTalk(
        0xFE,
        (
            "你叔叔\x01",
            "也出去工作了，\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0xFE,
        (
            "在去教堂祈祷之前，\x01",
            "我得先去把衣服叠好。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E0B")

    Jump("loc_3176")

    label("loc_2E10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_3039")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FBB")
    OP_93(0xFE, 0x13B, 0x0)

    #C0181
    ChrTalk(
        0xFE,
        (
            "这孩子终于\x01",
            "平安回来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xFE,
        "空之女神啊，感谢您的庇佑。\x02",
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x102,
        "#0100F（真是虔诚呢。）\x02",
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0x101,
        "#0000F（嗯，一直都是啊。）\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x43, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2EE3")

    #C0185
    ChrTalk(
        0x101,
        (
            "#0000F（大哥去世时……\x01",
            "　阿姨也是这样……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F14")

    label("loc_2EE3")


    #C0186
    ChrTalk(
        0x101,
        (
            "#0000F（大哥殉职时……\x01",
            "　阿姨也是这样……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F14")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xFE, 0x0, 500)

    #C0187
    ChrTalk(
        0xFE,
        (
            "哎呀，不好意思，\x01",
            "不禁就忘我起来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0xFE,
        (
            "你叔叔他已经去\x01",
            "图书馆工作了。\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0xFE,
        (
            "他很喜欢图书管理员的工作，\x01",
            "所以每天很早就过去了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3034")

    label("loc_2FBB")


    #C0190
    ChrTalk(
        0xFE,
        (
            "你叔叔他已经去\x01",
            "图书馆工作了。\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0xFE,
        (
            "他很喜欢看书，\x01",
            "喜欢到因此成为图书管理员的程度哦。\x01",
            "每天出门去工作的时候都很开心。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3034")

    Jump("loc_3176")

    label("loc_3039")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_3176")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3128")

    #C0192
    ChrTalk(
        0xFE,
        (
            "自那之后，\x01",
            "已经过去三年了啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0xFE,
        (
            "塞茜尔每天都\x01",
            "说她很寂寞很寂寞。\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0xFE,
        (
            "所以我想叫大家来\x01",
            "办个聚会什么的。\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0x101,
        (
            "#0011F（嗯……看这气氛，好像阻止也没用。）\x02\x03",

            "#0006F（这份行动力……\x01",
            "　阿姨也一点都没变啊……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3176")

    label("loc_3128")


    #C0196
    ChrTalk(
        0xFE,
        (
            "罗伊德已经三年\x01",
            "没回来过了。\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0xFE,
        (
            "所以这次果然该叫大家来\x01",
            "办个聚会什么的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3176")

    TalkEnd(0xFE)
    Return()

    # Function_9_1505 end

    def Function_10_317A(): pass

    label("Function_10_317A")

    OP_93(0x9, 0x5A, 0x0)
    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_68(56890, 1000, 103430, 0)
    MoveCamera(45, 24, 0, 0)
    OP_6E(260, 0)
    SetCameraDistance(32000, 0)
    SetChrPos(0x101, 55780, 0, 103550, 90)
    SetChrPos(0xEF, 55940, 0, 104600, 135)
    SetChrPos(0x153, 55940, 0, 102750, 90)
    SetChrSubChip(0x9, 0x0)
    OP_93(0x9, 0x10E, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(750)
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_3246")

    #C0198
    ChrTalk(
        0x9,
        "哎呀，罗伊德和艾莉……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3295")

    label("loc_3246")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_3272")

    #C0199
    ChrTalk(
        0x9,
        "哎呀，罗伊德和小缇欧……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3295")

    label("loc_3272")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_3295")

    #C0200
    ChrTalk(
        0x9,
        "啊，罗伊德和兰迪……\x02",
    )

    CloseMessageWindow()

    label("loc_3295")


    #C0201
    ChrTalk(
        0x9,
        (
            "还有……哎呀呀，\x01",
            "这个可爱的孩子是……？\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x101,
        (
            "#0000F哈哈，她叫琪雅，\x01",
            "这段时间暂时\x01",
            "由我们支援科来照顾。\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0x153,
        (
            "#1110F中午好——！\x01",
            "这里有好多书呀！\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0x9,
        "你好啊。\x02",
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0x9,
        (
            "小琪雅也\x01",
            "很喜欢书吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0x9,
        (
            "我们家那位也很喜欢书哦，\x01",
            "他现在是图书馆的图书管理员。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB7, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3554")

    #C0207
    ChrTalk(
        0x153,
        (
            "#1111F图书馆～？\x02\x03",

            "#1110F啊，我知道了！\x01",
            "是可以借书的地方！\x02\x03",

            "#1109F罗伊德～\x01",
            "下次带我去图书馆吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0x101,
        (
            "#0003F嗯……这个啊……\x01",
            "要绕去那边的话，\x01",
            "好像得花不少时间呢……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_3491")

    #C0209
    ChrTalk(
        0x102,
        (
            "#0100F不过，小琪雅\x01",
            "一定会很开心吧。\x01",
            "花的时间也不多，没关系吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3526")

    label("loc_3491")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_34DD")

    #C0210
    ChrTalk(
        0x103,
        (
            "#0200F不过，琪雅\x01",
            "应该会很开心的吧……\x01",
            "带她去也不是不行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3526")

    label("loc_34DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_3526")

    #C0211
    ChrTalk(
        0x104,
        (
            "#0300F不过啊，阿琪\x01",
            "应该会很开心吧？\x01",
            "机会难得，就带她去吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3526")


    #C0212
    ChrTalk(
        0x101,
        (
            "#0000F对哦，这样一想\x01",
            "也不是不行……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3720")

    label("loc_3554")


    #C0213
    ChrTalk(
        0x153,
        (
            "#1110F图书馆～？\x01",
            "我们刚才去过了对吧！\x02\x03",

            "#1109F罗伊德～\x01",
            "琪雅又想\x01",
            "去图书馆了哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0x101,
        (
            "#0000F哈哈，但要是\x01",
            "再绕路去那边的话……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_3628")

    #C0215
    ChrTalk(
        0x102,
        (
            "#0100F哎呀，罗伊德，有什么关系啦。\x01",
            "小琪雅在图书馆时\x01",
            "那么开心呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36E1")

    label("loc_3628")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_3691")

    #C0216
    ChrTalk(
        0x103,
        (
            "#0200F……罗伊德前辈。\x01",
            "琪雅好像\x01",
            "很喜欢图书馆啊。\x02\x03",

            "你要是拒绝她，\x01",
            "会不会太残忍了一点。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36E1")

    label("loc_3691")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_36E1")

    #C0217
    ChrTalk(
        0x104,
        (
            "#0300F罗伊德，有什么关系嘛。\x01",
            "既然阿琪那么喜欢图书馆，就带她去吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36E1")

    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0218
    ChrTalk(
        0x101,
        "#0000F大家都对琪雅太溺爱了……\x02",
    )

    CloseMessageWindow()

    label("loc_3720")


    #C0219
    ChrTalk(
        0x9,
        (
            "……呵呵，总觉得\x01",
            "你们多了个幸福的烦恼呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0x9,
        (
            "小琪雅，\x01",
            "有空再来玩啊，\x01",
            "阿姨随时欢迎你。\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0x153,
        (
            "#1109F嗯，琪雅会再来玩的。\x02\x03",

            "阿姨，再见！\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0x9,
        "嗯，小琪雅再见啊。\x02",
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0x101,
        (
            "#0000F（不愧是阿姨，\x01",
            "　果然很擅长与孩子相处……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xAF, 7)
    EventEnd(0x5)
    Return()

    # Function_10_317A end

    def Function_11_3800(): pass

    label("Function_11_3800")


    #C0224
    ChrTalk(
        0xFE,
        "哎呀，这不是罗伊德嘛。\x02",
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0xFE,
        (
            "有段时间没见了，\x01",
            "在努力工作吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0x101,
        "#0000F哈哈，算是吧。\x02",
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0x104,
        "#0300F虽然都是些无关紧要的工作。\x02",
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0xFE,
        (
            "呵呵，每个人\x01",
            "刚开始都是这样的。\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0xFE,
        (
            "对了，今天阿姨\x01",
            "教你们做菜的诀窍吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0xFE,
        (
            "你们总是在拼命工作，\x01",
            "必须多吃点有营养的东西。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0231
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x19A),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "的做法被教授了。\x02",
        )
    )

    CloseMessageWindow()

    #A0232
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x19A),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "的做法已经学会了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    OP_B0(0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_397E")
    SetScenarioFlags(0x0, 1)

    label("loc_397E")

    Return()

    # Function_11_3800 end

    def Function_12_397F(): pass

    label("Function_12_397F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_3A18")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39EA")

    #C0233
    ChrTalk(
        0xFE,
        (
            "要从玛因兹翻山越岭，\x01",
            "去列曼自治州……？\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0xFE,
        "抱歉，我实在是有心无力……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3A13")

    label("loc_39EA")


    #C0235
    ChrTalk(
        0xFE,
        (
            "我这两个孩子啊……\x01",
            "全都这么调皮……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A13")

    Jump("loc_4106")

    label("loc_3A18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3A29")
    Call(0, 13)
    Jump("loc_4106")

    label("loc_3A29")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_3AD6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3AAA")

    #C0236
    ChrTalk(
        0xFE,
        (
            "塔利兹商店的小桃\x01",
            "真是个乖孩子啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0xFE,
        "她聪明伶俐，总是帮店里做事……\x02",
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0xFE,
        (
            "真想让隆\x01",
            "也好好学学。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3AD1")

    label("loc_3AAA")


    #C0239
    ChrTalk(
        0xFE,
        (
            "哎呀哎呀……真想让隆\x01",
            "也好好学学。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3AD1")

    Jump("loc_4106")

    label("loc_3AD6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_3B4C")

    #C0240
    ChrTalk(
        0xFE,
        (
            "琪露露这小家伙，\x01",
            "好像又想跑到哪里去玩呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0xFE,
        (
            "隆已经让人很头痛了，\x01",
            "琪露露这小家伙也让人伤脑筋啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4106")

    label("loc_3B4C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_3BDF")

    #C0242
    ChrTalk(
        0xFE,
        (
            "哇哈哈，好热闹的庆典啊！\x01",
            "今天去中央广场吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0xFE,
        (
            "不过……琪露露\x01",
            "不喜欢陪人出去啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0xFE,
        (
            "跟她说今天想吃什么，\x01",
            "我都会买给她好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4106")

    label("loc_3BDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_3C79")

    #C0245
    ChrTalk(
        0xFE,
        (
            "今天西街和住宅街一带的孩子们\x01",
            "要去主日学校上课。\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0xFE,
        (
            "隆如果也能\x01",
            "认真读书就好了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x90, 0)), scpexpr(EXPR_END)), "loc_3C74")

    #C0247
    ChrTalk(
        0x101,
        (
            "#0003F（……一直都在\x01",
            "　和蔡特玩呢……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C74")

    Jump("loc_4106")

    label("loc_3C79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_3D87")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D21")

    #C0248
    ChrTalk(
        0xFE,
        (
            "我将来想把生意\x01",
            "全部交给隆这小子的。\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0xFE,
        (
            "但是……这混小子\x01",
            "今天又跑去玩了。\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0xFE,
        (
            "在主日学校的成绩也完全不行。\x01",
            "……真是个不争气的儿子……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3D82")

    label("loc_3D21")


    #C0251
    ChrTalk(
        0xFE,
        (
            "本来想教点\x01",
            "生意上的基本知识给隆……\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0xFE,
        (
            "但那个冒失鬼，\x01",
            "根本一点都没把\x01",
            "我说的话听进去……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D82")

    Jump("loc_4106")

    label("loc_3D87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_3E00")
    OP_93(0xFE, 0x0, 0x0)

    #C0253
    ChrTalk(
        0xFE,
        (
            "呼，隆这混小子，\x01",
            "不会打算就这么养下去吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0xFE,
        (
            "虽然说了下不为例，\x01",
            "但他大概也没听进去吧……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4106")

    label("loc_3E00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_3ECA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E9C")

    #C0255
    ChrTalk(
        0xFE,
        (
            "我今天要去百货店\x01",
            "送货呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0xFE,
        (
            "都是些新奇的杂货，\x01",
            "应该会卖得不错吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0xFE,
        (
            "去百货店拉生意的批发商非常多……\x01",
            "我也不能落后了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3EC5")

    label("loc_3E9C")


    #C0258
    ChrTalk(
        0xFE,
        (
            "这些新奇的商品，\x01",
            "应该都能卖得不错。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3EC5")

    Jump("loc_4106")

    label("loc_3ECA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_4002")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F8B")

    #C0259
    ChrTalk(
        0xFE,
        (
            "我是大概从三年前开始\x01",
            "在克洛斯贝尔做生意的。\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0xFE,
        (
            "从事的是批发业，\x01",
            "就是给百货店这些大型商店\x01",
            "提供各种货物。\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0xFE,
        (
            "呵呵，我是共和国人，\x01",
            "所以对共和国商品很有鉴别力。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3FFD")

    label("loc_3F8B")


    #C0262
    ChrTalk(
        0xFE,
        (
            "在克洛斯贝尔做了\x01",
            "三年批发生意，\x01",
            "现在终于走上了正轨。\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0xFE,
        (
            "这多亏了和时代百货店\x01",
            "签了长期合同啊。\x01",
            "哇哈哈……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3FFD")

    Jump("loc_4106")

    label("loc_4002")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_4106")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_40BE")

    #C0264
    ChrTalk(
        0xFE,
        (
            "我今天早上打开\x01",
            "克洛斯贝尔时代周刊后……\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0xFE,
        (
            "居然发现上面登了隆这混小子\x01",
            "的报道，还附了照片。\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0xFE,
        "这、这个笨蛋儿子……！\x02",
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0xFE,
        (
            "当然，我当场就\x01",
            "狠狠训斥了他。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4106")

    label("loc_40BE")


    #C0268
    ChrTalk(
        0xFE,
        (
            "隆这个混小子，\x01",
            "虽然被我狠狠训斥了一顿，\x01",
            "但不知道有没有在认真反省。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4106")

    TalkEnd(0xFE)
    Return()

    # Function_12_397F end

    def Function_13_410A(): pass

    label("Function_13_410A")

    OP_4B(0xA, 0xFF)
    OP_4B(0x11, 0xFF)
    TurnDirection(0xA, 0x11, 0)
    TurnDirection(0x11, 0xA, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4222")

    #C0269
    ChrTalk(
        0xA,
        (
            "啊，琪露露，你回来了啊。\x01",
            "这次的旅行怎么样啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0x11,
        "……有三次差点被淹死。\x02",
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0x11,
        (
            "那片潮湿的草原地带，\x01",
            "到处都是深不见底的沼泽，\x01",
            "实在太危险了。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xA)

    #C0272
    ChrTalk(
        0xA,
        (
            "什、什么……那也太危险了吧！\x01",
            "你这孩子到底跑到多远的地方去了啊！？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_42EF")

    label("loc_4222")


    #C0273
    ChrTalk(
        0xA,
        (
            "琪露露，我果然\x01",
            "不能让你一个人出门。\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0xA,
        (
            "下次要出去的话，也把我带上吧。\x01",
            "我偶尔也该陪你\x01",
            "一起去玩玩。\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0x11,
        (
            "可以是可以……不过要走很多路哦。\x01",
            "爸爸你应该走不动吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0xA,
        (
            "你在说什么！\x01",
            "不要小看父亲的伟大哦！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_42EF")

    OP_4C(0xA, 0xFF)
    OP_4C(0x11, 0xFF)
    Return()

    # Function_13_410A end

    def Function_14_42F8(): pass

    label("Function_14_42F8")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_438C")
    Jump("loc_43D6")

    label("loc_438C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_43AC")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_43D6")

    label("loc_43AC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_43CC")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_43D6")

    label("loc_43CC")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_43D6")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_4409")
    Jump("loc_481D")

    label("loc_4409")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_4417")
    Jump("loc_481D")

    label("loc_4417")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_4425")
    Jump("loc_481D")

    label("loc_4425")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_451C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_44C7")

    #C0277
    ChrTalk(
        0xFE,
        (
            "哇哈哈……！\x01",
            "最近生意真的很不错啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0xFE,
        (
            "这个月已经和\x01",
            "三家新店签了合同。\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0xFE,
        (
            "而且都是对方找上门来的。\x01",
            "哇哈哈，实在太让人高兴了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4517")

    label("loc_44C7")


    #C0280
    ChrTalk(
        0xFE,
        (
            "这个月已经和\x01",
            "三家新店签了合同。\x02",
        )
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0xFE,
        (
            "哇哈哈……！\x01",
            "我的生意终于做出名气了！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4517")

    Jump("loc_481D")

    label("loc_451C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_45AD")
    SetChrSubChip(0xFE, 0x0)

    #C0282
    ChrTalk(
        0xFE,
        (
            "唔，订单的数量比想象中要多得多啊。\x01",
            "全部用导力列车来运吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0xFE,
        (
            "不行，那样可能会来不及。\x01",
            "在阿尔泰尔市换成\x01",
            "货车来运吧……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_481D")

    label("loc_45AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_46D0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_465B")

    #C0284
    ChrTalk(
        0xFE,
        (
            "订单票据的整理，\x01",
            "货物搬运的准备，还有账目结算的手续……\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0xFE,
        "唔，工作堆积如山啊。\x02",
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0xFE,
        (
            "……为了在\x01",
            "纪念庆典时可以休息……\x01",
            "现在要努力工作……！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_46CB")

    label("loc_465B")


    #C0287
    ChrTalk(
        0xFE,
        (
            "我好歹也是克洛斯贝尔的市民，\x01",
            "纪念庆典期间也想休息一下，好好享受享受。\x02",
        )
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0xFE,
        (
            "所以必须趁现在\x01",
            "把工作都做完了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_46CB")

    Jump("loc_481D")

    label("loc_46D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_481D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_47B8")

    #C0289
    ChrTalk(
        0xFE,
        (
            "庆典期间，大部分商店\x01",
            "应该都会举行大型促销活动吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0xFE,
        "我们这些批发商有得忙了。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)

    #C0291
    ChrTalk(
        0xFE,
        (
            "牙膏八十四箱，\x01",
            "平常的杂志也增加了两百五十本……\x02",
        )
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0xFE,
        (
            "嗯，必须得想办法搞定这些啊……\x01",
            "（噼里啪啦，噼里啪啦……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_481D")

    label("loc_47B8")


    #C0293
    ChrTalk(
        0xFE,
        (
            "……顺便说一句，这东西\x01",
            "叫做算盘。\x01",
            "是东方的手动计算器。\x02",
        )
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0xFE,
        (
            "东方出身的商人总是\x01",
            "用这个进行计算。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_481D")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_14_42F8 end

    def Function_15_4825(): pass

    label("Function_15_4825")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_484F")
    Call(0, 27)
    Return()

    label("loc_484F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x2)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4ACD")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x3)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A6B")

    #C0295
    ChrTalk(
        0x101,
        (
            "#0000F不好意思，打扰一下，\x02\x03",

            "请问你有\x01",
            "养猫吗？\x01",
            "或是知道谁养猫了吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0xFE,
        (
            "哎呀，你是想问隆\x01",
            "发现的那只小猫吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0xFE,
        (
            "之前已经跟那两人说过了，\x01",
            "我什么都不知道呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0xFE,
        (
            "虽然我不确定\x01",
            "爸爸和姐姐\x01",
            "有没有偷偷在养……\x02",
        )
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0xFE,
        (
            "不过，两个人都只对机械师\x01",
            "的工作感兴趣，对这种\x01",
            "活物应该没有兴趣吧。\x02",
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
    Sleep(1200)

    #C0300
    ChrTalk(
        0x101,
        (
            "#0006F（温蒂的妹妹……\x01",
            "　嘴巴好厉害啊……）\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0x103,
        (
            "#0200F算了，她好像是\x01",
            "真的没什么头绪。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x8, 0x1, 0x3)
    Jump("loc_4AC8")

    label("loc_4A6B")


    #C0302
    ChrTalk(
        0xFE,
        (
            "隆和亨利也来问过我了，\x01",
            "我不知道什么小猫哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0xFE,
        (
            "我觉得在贝尔海姆，\x01",
            "应该没人\x01",
            "养宠物吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4AC8")

    Jump("loc_5991")

    label("loc_4ACD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_4B84")

    #C0304
    ChrTalk(
        0xC,
        (
            "爸爸肯定是为了\x01",
            "把我引向铁路技师的世界，\x01",
            "才会把那本书借来给我看的。\x02",
        )
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0xC,
        (
            "姐姐就是因为玩着\x01",
            "爸爸买的导力玩具长大，\x01",
            "所以后来才会成为技师……\x02",
        )
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0xC,
        (
            "我才不会\x01",
            "上他的当呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5991")

    label("loc_4B84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4D01")

    #C0307
    ChrTalk(
        0x101,
        (
            "#0000F你好，潘莎，\x01",
            "今天也是你看家啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0xFE,
        (
            "啊，哥哥好像是\x01",
            "温蒂姐姐的\x01",
            "朋友吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0xFE,
        (
            "姐姐总是承蒙你们的照顾，\x01",
            "真是谢谢了。\x02",
        )
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0x102,
        (
            "#0102F呵呵，哪里，我们才总是\x01",
            "受温蒂的照顾呢。\x02\x03",

            "#0100F小妹妹，你在大扫除吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0xFE,
        (
            "嗯，对啊。\x01",
            "爸爸和姐姐\x01",
            "都不擅长打扫。\x02",
        )
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0xFE,
        (
            "大家也帮我说说她吧？\x01",
            "就说她应该培养点自理能力。\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0x101,
        (
            "#0009F哈哈哈……\x01",
            "（温蒂的妹妹\x01",
            "　真是成熟啊。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x4E, 1)
    Jump("loc_5991")

    label("loc_4D01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_4E21")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4DD9")

    #C0314
    ChrTalk(
        0xFE,
        (
            "那个，玛丽亚贝尔小姐是\x01",
            "ＩＢＣ技术部的领导者哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0xFE,
        "她对导力技术十分了解。\x02",
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0xFE,
        (
            "……………………………………\x01",
            "……………………………………\x02",
        )
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0xFE,
        (
            "这、这种大美人\x01",
            "竟然还是技师，真厉害啊！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4E1C")

    label("loc_4DD9")


    #C0318
    ChrTalk(
        0xFE,
        (
            "玛丽亚贝尔小姐真是\x01",
            "太帅了。\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0xFE,
        "完全是成熟女性的理想形象啊！\x02",
    )

    CloseMessageWindow()

    label("loc_4E1C")

    Jump("loc_5991")

    label("loc_4E21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_4EE1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4EB7")

    #C0320
    ChrTalk(
        0xFE,
        (
            "今天温蒂姐姐\x01",
            "睡懒觉了哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0xFE,
        (
            "我叫了她好几次，\x01",
            "她却念叨着什么『导力回路……』，\x01",
            "就是不起床。\x02",
        )
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0xFE,
        "真是，这怎么行啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4EDC")

    label("loc_4EB7")


    #C0323
    ChrTalk(
        0xFE,
        (
            "温蒂姐姐她\x01",
            "总是这么不争气呢～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4EDC")

    Jump("loc_5991")

    label("loc_4EE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_4FD8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F95")

    #C0324
    ChrTalk(
        0xFE,
        (
            "听说今天的经济杂志上，\x01",
            "刊登了玛丽亚贝尔小姐\x01",
            "的照片哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0xFE,
        (
            "不管那是经济杂志还是什么杂志，\x01",
            "我都必须赶快去买到手。\x02",
        )
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0xFE,
        "然后把那照片剪下来好好保存！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4FD3")

    label("loc_4F95")


    #C0327
    ChrTalk(
        0xFE,
        (
            "玛丽亚贝尔小姐\x01",
            "真是太出色了～！\x01",
            "简直就是成熟女性的典范！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4FD3")

    Jump("loc_5991")

    label("loc_4FD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_5125")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_50DB")

    #C0328
    ChrTalk(
        0xFE,
        (
            "罗伊德哥哥\x01",
            "是温蒂姐姐\x01",
            "的朋友吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0x101,
        (
            "#0000F嗯……\x01",
            "曾经住在同一间出租公寓里，\x01",
            "可以说是青梅竹马哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0xFE,
        (
            "嗯，竟然能和\x01",
            "姐姐那种人做朋友，\x01",
            "你真是不容易啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0xFE,
        (
            "今天早上她起来后，\x01",
            "带着一头睡乱的头发就去工作了。\x01",
            "真是让人难以置信。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5120")

    label("loc_50DB")


    #C0332
    ChrTalk(
        0xFE,
        "做技师的果然都很邋遢。\x02",
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0xFE,
        (
            "没化妆就出门，\x01",
            "这可是女性的大忌啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5120")

    Jump("loc_5991")

    label("loc_5125")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_518C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5140")
    Call(0, 17)
    Jump("loc_5187")

    label("loc_5140")


    #C0334
    ChrTalk(
        0xFE,
        "爸爸又要去出差了。\x02",
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0xFE,
        (
            "……不用带礼物也行，\x01",
            "快点回家就可以了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5187")

    Jump("loc_5991")

    label("loc_518C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_51D8")
    OP_93(0xFE, 0x2D, 0x0)

    #C0336
    ChrTalk(
        0xFE,
        "我说，爸爸！？\x02",
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0xFE,
        (
            "你不是答应\x01",
            "要带我去看庆典吗！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5991")

    label("loc_51D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_52F8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_526A")

    #C0338
    ChrTalk(
        0xFE,
        (
            "今天的时尚杂志，\x01",
            "封面是玛丽亚贝尔小姐哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(500)

    #C0339
    ChrTalk(
        0xFE,
        (
            "啊啊，真是太帅了！\x01",
            "这张绝对要剪下来好好保存！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_52F3")

    label("loc_526A")


    #C0340
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔第一的千金小姐，\x01",
            "既是年轻的天才女性经营家，\x01",
            "同时也拥有绝美的容貌……\x02",
        )
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0xFE,
        (
            "玛丽亚贝尔小姐的封面，\x01",
            "这一定要剪下来好好保存！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_52F3")

    Jump("loc_5991")

    label("loc_52F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_5452")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_53D8")

    #C0342
    ChrTalk(
        0xFE,
        (
            "我去买东西的时候，\x01",
            "听到所有人都在聊彩虹剧团。\x02",
        )
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0xFE,
        (
            "不过，比起伊莉娅小姐，\x01",
            "我还是比较喜欢玛丽亚贝尔小姐～\x02",
        )
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0xFE,
        (
            "玛丽亚贝尔小姐在ＩＢＣ工作，\x01",
            "被誉为克洛斯贝尔第一的千金小姐哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0xFE,
        "真是太帅了。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_544D")

    label("loc_53D8")


    #C0346
    ChrTalk(
        0xFE,
        (
            "玛丽亚贝尔小姐是\x01",
            "ＩＢＣ总裁的独生女。\x02",
        )
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0xFE,
        (
            "不但是年轻的天才女性经营家，\x01",
            "而且还拥有绝美的容貌哦。\x01",
            "实在是太帅了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_544D")

    Jump("loc_5991")

    label("loc_5452")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_54F7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_54C7")

    #C0348
    ChrTalk(
        0xFE,
        "我得去主日学校上课。\x02",
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0xFE,
        (
            "呼～真是好麻烦。\x01",
            "我想当的是模特，\x01",
            "有什么必要去学校上课啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_54F2")

    label("loc_54C7")


    #C0350
    ChrTalk(
        0xFE,
        (
            "我得去主日学校上课。\x01",
            "呼～真是好麻烦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_54F2")

    Jump("loc_5991")

    label("loc_54F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_55FA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_55B1")

    #C0351
    ChrTalk(
        0xFE,
        (
            "在克洛斯贝尔，\x01",
            "有五份时尚杂志比较有名。\x02",
        )
    )

    CloseMessageWindow()

    #C0352
    ChrTalk(
        0xFE,
        (
            "其中三份是克洛斯贝尔的杂志社出的，\x01",
            "另外两份则是帝国和共和国的杂志。\x02",
        )
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0xFE,
        (
            "这五份杂志，我每期\x01",
            "都会追着看哦～！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_55F5")

    label("loc_55B1")


    #C0354
    ChrTalk(
        0xFE,
        (
            "因为我将来\x01",
            "想要当模特。\x02",
        )
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0xFE,
        (
            "所以看时尚杂志\x01",
            "是基本中的基本哦！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_55F5")

    Jump("loc_5991")

    label("loc_55FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_57A3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5755")

    #C0356
    ChrTalk(
        0xFE,
        (
            "爸爸是\x01",
            "铁路技师。\x02",
        )
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0xFE,
        (
            "今天也出差在外。\x01",
            "好像还要两个月才能回家。\x02",
        )
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0x101,
        (
            "#0000F温蒂的爸爸\x01",
            "真是大忙人啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0xFE,
        "话说回来……\x02",
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0xFE,
        (
            "从姐姐小时候开始，\x01",
            "爸爸就拿导力玩具给她玩，\x01",
            "最后把姐姐培养成了技师。\x02",
        )
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0xFE,
        "我可得提防着点。\x02",
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
    SetScenarioFlags(0x0, 3)
    Jump("loc_579B")

    label("loc_5755")


    #C0362
    ChrTalk(
        0xFE,
        "爸爸是铁道技师。\x02",
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0xFE,
        (
            "但是，我绝对不会\x01",
            "玩爸爸给我的\x01",
            "导力玩具哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_579B")

    SetScenarioFlags(0x71, 5)
    Jump("loc_5991")

    label("loc_57A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_5939")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_57BE")
    Call(0, 16)
    Jump("loc_5934")

    label("loc_57BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_58DA")

    #C0364
    ChrTalk(
        0xFE,
        (
            "我啊，长大以后，\x01",
            "要成为模特。\x02",
        )
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0xFE,
        (
            "就算不能当模特，\x01",
            "也绝对不像姐姐那样当什么机械师。\x02",
        )
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0xFE,
        (
            "我绝对要变成\x01",
            "身材火辣的成熟女性！\x02",
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

    #C0367
    ChrTalk(
        0x104,
        "#0300F小妹妹，真是志向可嘉哦……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5934")

    label("loc_58DA")


    #C0368
    ChrTalk(
        0xFE,
        (
            "我啊，长大以后，\x01",
            "要成为模特。\x02",
        )
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0xFE,
        (
            "就算不能当模特，\x01",
            "也绝对不像姐姐那样当什么机械师。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5934")

    Jump("loc_5991")

    label("loc_5939")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_5991")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5957")
    Call(0, 16)
    SetScenarioFlags(0x0, 3)
    Jump("loc_5991")

    label("loc_5957")


    #C0370
    ChrTalk(
        0xFE,
        (
            "爸爸和姐姐\x01",
            "都不擅长打扫。\x02",
        )
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0xFE,
        (
            "所以全部\x01",
            "都得我来做！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5991")

    TalkEnd(0xFE)
    Return()

    # Function_15_4825 end

    def Function_16_5995(): pass

    label("Function_16_5995")


    #C0372
    ChrTalk(
        0xC,
        "扫地、洗衣服、洗碗……\x02",
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0xC,
        (
            "爸爸和姐姐\x01",
            "都不擅长打扫。\x02",
        )
    )

    CloseMessageWindow()

    #C0374
    ChrTalk(
        0xC,
        (
            "真是的，完全没有\x01",
            "一点生活能力……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B4E")
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0375
    ChrTalk(
        0x101,
        (
            "#0005F咦，你好像是……\x01",
            "温蒂家的小妹妹吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0376
    ChrTalk(
        0xC,
        (
            "嗯～？\x01",
            "你认识姐姐吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0377
    ChrTalk(
        0x101,
        (
            "#0000F啊，不，没什么。\x01",
            "不好意思，打扰了啊。\x02\x03",

            "#0004F（这样啊……都三年没见了，\x01",
            "　肯定已经不记得我了呢。）\x02",
        )
    )

    CloseMessageWindow()

    #C0378
    ChrTalk(
        0x104,
        (
            "#0309F咦～罗伊德，\x01",
            "你的狩猎范围很广嘛⊥\x02",
        )
    )

    CloseMessageWindow()

    #C0379
    ChrTalk(
        0x101,
        (
            "#0003F你·想·多·了。\x01",
            "别说这些会让人误解的话。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x4E, 1)

    label("loc_5B4E")

    Return()

    # Function_16_5995 end

    def Function_17_5B4F(): pass

    label("Function_17_5B4F")

    OP_4B(0xC, 0xFF)
    OP_4B(0xF, 0xFF)
    TurnDirection(0xC, 0xF, 0)
    TurnDirection(0xF, 0xC, 0)

    #C0380
    ChrTalk(
        0xF,
        (
            "潘莎，在下次出差之前，\x01",
            "我把礼物给你吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0xF,
        (
            "看，是导力车的模型，还会动哦！\x01",
            "是我自己做的～\x02",
        )
    )

    CloseMessageWindow()

    #C0382
    ChrTalk(
        0xF,
        (
            "而且啊，还可以\x01",
            "用导力波远距离操控它哦。\x01",
            "很棒吧～！\x02",
        )
    )

    CloseMessageWindow()

    #C0383
    ChrTalk(
        0xC,
        (
            "……什么啊，\x01",
            "我才不要呢～\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0384
    ChrTalk(
        0xF,
        (
            "（沉重打击）……\x01",
            "这可是划时代的玩具啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xC, 0xFF)
    OP_4C(0xF, 0xFF)
    SetScenarioFlags(0x0, 3)
    SetScenarioFlags(0x0, 5)
    Return()

    # Function_17_5B4F end

    def Function_18_5C75(): pass

    label("Function_18_5C75")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5C93")
    Call(0, 28)
    Return()

    label("loc_5C93")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x70, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5CAD")
    Call(0, 32)
    Return()

    label("loc_5CAD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_5D47")

    #C0385
    ChrTalk(
        0xFE,
        "啊，是支援科的大哥哥们。\x02",
    )

    CloseMessageWindow()

    #C0386
    ChrTalk(
        0xFE,
        (
            "庆典期间还要巡逻吗，\x01",
            "嘿嘿，真遗憾呢～！\x02",
        )
    )

    CloseMessageWindow()

    #C0387
    ChrTalk(
        0x101,
        (
            "#0000F嗯嗯。\x01",
            "……你接下来好像要出门吧，\x01",
            "可别玩得太疯哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6133")

    label("loc_5D47")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x70, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5E74")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E15")

    #C0388
    ChrTalk(
        0xFE,
        (
            "嘁，只有\x01",
            "一个星期而已呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0389
    ChrTalk(
        0xFE,
        (
            "我还想\x01",
            "多养一段时间的（小声嘟嚷）……\x02",
        )
    )

    CloseMessageWindow()

    #C0390
    ChrTalk(
        0xFE,
        (
            "算了算了。\x01",
            "大哥哥们，谢谢啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0391
    ChrTalk(
        0xFE,
        (
            "我稍微\x01",
            "对你们有点改观了哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0392
    ChrTalk(
        0x101,
        "#0003F你还真不坦率啊……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_5E6F")

    label("loc_5E15")


    #C0393
    ChrTalk(
        0xFE,
        (
            "嘁，只要爸爸同意，\x01",
            "我就可以\x01",
            "养了。\x02",
        )
    )

    CloseMessageWindow()

    #C0394
    ChrTalk(
        0xFE,
        (
            "……算了算了。\x01",
            "小猫应该是回去\x01",
            "主人那里了吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5E6F")

    Jump("loc_6133")

    label("loc_5E74")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x2)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5F14")

    #C0395
    ChrTalk(
        0xFE,
        (
            "我们其实\x01",
            "也很想养的。\x02",
        )
    )

    CloseMessageWindow()

    #C0396
    ChrTalk(
        0xFE,
        (
            "但爸爸怎么\x01",
            "都不同意。\x01",
            "亨利家好像也不能养宠物。\x02",
        )
    )

    CloseMessageWindow()

    #C0397
    ChrTalk(
        0xFE,
        (
            "所以，\x01",
            "哥哥姐姐们，就拜托你们了！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6133")

    label("loc_5F14")

    TurnDirection(0xE, 0x0, 0)
    OP_4B(0xE, 0xFF)

    #C0398
    ChrTalk(
        0xD,
        (
            "哥哥姐姐们，\x01",
            "你们的事情已经做完了吧～？\x02",
        )
    )

    CloseMessageWindow()

    #C0399
    ChrTalk(
        0xD,
        (
            "那就快点\x01",
            "帮我寻找这只小猫的主人吧～\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【接受】\x01",      # 0
            "【拒绝】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_5A()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_5FCA"),
        (1, "loc_607F"),
        (SWITCH_DEFAULT, "loc_6128"),
    )


    label("loc_5FCA")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-56430, 1100, 108630, 0)
    MoveCamera(37, 18, 0, 0)
    OP_6E(260, 0)
    SetCameraDistance(34090, 0)
    SetChrPos(0x101, -55490, 0, 108350, 270)
    SetChrPos(0x102, -54150, 0, 108180, 270)
    SetChrPos(0x103, -55490, 0, 109530, 270)
    SetChrPos(0x104, -54090, 0, 109530, 270)
    SetChrPos(0xD, -58000, 0, 107500, 90)
    SetChrPos(0xE, -57930, 0, 110500, 90)
    FadeToBright(1000, 0)
    OP_0D()
    OP_29(0x8, 0x1, 0x1)
    Call(0, 29)
    Return()

    label("loc_607F")


    #C0400
    ChrTalk(
        0x101,
        (
            "#0006F抱歉啊，我们现在有点脱不开身。\x01",
            "等有空了\x01",
            "我们再来帮你们找……\x02",
        )
    )

    CloseMessageWindow()

    #C0401
    ChrTalk(
        0xE,
        (
            "知道了，在那之前就由我们\x01",
            "来照顾它吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0402
    ChrTalk(
        0xD,
        (
            "嘁，真没办法。\x01",
            "大哥哥，\x01",
            "拜托你们早点来哦！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_6128")

    label("loc_6128")

    OP_93(0xE, 0xB4, 0x0)
    OP_4C(0xE, 0xFF)

    label("loc_6133")

    TalkEnd(0xFE)
    Return()

    # Function_18_5C75 end

    def Function_19_6137(): pass

    label("Function_19_6137")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6155")
    Call(0, 28)
    Return()

    label("loc_6155")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x70, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_616F")
    Call(0, 32)
    Return()

    label("loc_616F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x70, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6289")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6226")

    #C0403
    ChrTalk(
        0xFE,
        (
            "各位，\x01",
            "谢谢你们了！\x02",
        )
    )

    CloseMessageWindow()

    #C0404
    ChrTalk(
        0xFE,
        (
            "我们和隆的爸爸约好了，\x01",
            "等一下要好好打扫，\x01",
            "肯定会很辛苦吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0405
    ChrTalk(
        0xFE,
        (
            "虽然时间很短，不过能\x01",
            "养这只小猫咪，我真的很开心。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_6284")

    label("loc_6226")


    #C0406
    ChrTalk(
        0xFE,
        (
            "虽然时间很短，不过能\x01",
            "养这只小猫咪，我真的很开心。\x02",
        )
    )

    CloseMessageWindow()

    #C0407
    ChrTalk(
        0xFE,
        (
            "我也……好想养只\x01",
            "可爱的小猫啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6284")

    Jump("loc_64FA")

    label("loc_6289")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x2)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6306")

    #C0408
    ChrTalk(
        0xFE,
        (
            "隆的爸爸很严格的，\x01",
            "所以必须好好打扫……\x02",
        )
    )

    CloseMessageWindow()

    #C0409
    ChrTalk(
        0xFE,
        (
            "啊，各位，\x01",
            "这只小猫咪\x01",
            "就拜托了！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_64FA")

    label("loc_6306")

    TurnDirection(0xD, 0x0, 0)
    OP_4B(0xD, 0xFF)

    #C0410
    ChrTalk(
        0xE,
        (
            "各位，能帮我寻找\x01",
            "这只小猫咪的主人吗？\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【接受】\x01",      # 0
            "【拒绝】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_5A()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_6391"),
        (1, "loc_6446"),
        (SWITCH_DEFAULT, "loc_64EF"),
    )


    label("loc_6391")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-56430, 1100, 108630, 0)
    MoveCamera(37, 18, 0, 0)
    OP_6E(260, 0)
    SetCameraDistance(34090, 0)
    SetChrPos(0x101, -55490, 0, 108350, 270)
    SetChrPos(0x102, -54150, 0, 108180, 270)
    SetChrPos(0x103, -55490, 0, 109530, 270)
    SetChrPos(0x104, -54090, 0, 109530, 270)
    SetChrPos(0xD, -58000, 0, 107500, 90)
    SetChrPos(0xE, -57930, 0, 110500, 90)
    FadeToBright(1000, 0)
    OP_0D()
    OP_29(0x8, 0x1, 0x1)
    Call(0, 29)
    Return()

    label("loc_6446")


    #C0411
    ChrTalk(
        0x101,
        (
            "#0006F抱歉啊，我们现在有点脱不开身。\x01",
            "等有空了\x01",
            "我们再来帮你们找……\x02",
        )
    )

    CloseMessageWindow()

    #C0412
    ChrTalk(
        0xE,
        (
            "知道了，在那之前就由我们\x01",
            "来照顾它吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0413
    ChrTalk(
        0xD,
        (
            "嘁，真没办法。\x01",
            "大哥哥，\x01",
            "拜托你们早点来哦！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_64EF")

    label("loc_64EF")

    OP_93(0xD, 0x0, 0x0)
    OP_4C(0xD, 0xFF)

    label("loc_64FA")

    TalkEnd(0xFE)
    Return()

    # Function_19_6137 end

    def Function_20_64FE(): pass

    label("Function_20_64FE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_66C3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6689")

    #C0414
    ChrTalk(
        0xFE,
        (
            "哎呀，罗伊德，好久不见啊。\x01",
            "有在努力工作吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0415
    ChrTalk(
        0x101,
        (
            "#0000F菲伊先生……\x01",
            "久疏问候。\x02\x03",

            "您在纪念庆典期间回来了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0416
    ChrTalk(
        0xFE,
        (
            "啊哈哈……从明天开始又得去出差了，\x01",
            "这次差不多要去两个月。\x02",
        )
    )

    CloseMessageWindow()

    #C0417
    ChrTalk(
        0x101,
        "#0005F又是铁路的铺设工程吗……？\x02",
    )

    CloseMessageWindow()

    #C0418
    ChrTalk(
        0xFE,
        (
            "世界上还有许多国家的\x01",
            "导力技术比较落后。\x02",
        )
    )

    CloseMessageWindow()

    #C0419
    ChrTalk(
        0xFE,
        (
            "不只是去铺设铁路，\x01",
            "也必须对管理和安全运用的知识\x01",
            "进行宣传。\x02",
        )
    )

    CloseMessageWindow()

    #C0420
    ChrTalk(
        0xFE,
        (
            "我作为一个技术指导员，\x01",
            "不得不加油啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB0, 2)
    Jump("loc_66BE")

    label("loc_6689")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_669B")
    Call(0, 17)
    Jump("loc_66BE")

    label("loc_669B")


    #C0421
    ChrTalk(
        0xFE,
        (
            "嗯，这对潘莎来说\x01",
            "还早了点吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_66BE")

    Jump("loc_67A5")

    label("loc_66C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_67A5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6770")

    #C0422
    ChrTalk(
        0x101,
        (
            "#0005F啊，是温蒂的\x01",
            "爸爸。\x02",
        )
    )

    CloseMessageWindow()

    #C0423
    ChrTalk(
        0x102,
        "#0100F看起来……好像很累呢。\x02",
    )

    CloseMessageWindow()

    #C0424
    ChrTalk(
        0xFE,
        (
            "（小声嘟嚷）……\x01",
            "我出差刚刚才回来……\x02",
        )
    )

    CloseMessageWindow()

    #C0425
    ChrTalk(
        0xFE,
        "潘莎，今天就让我好好睡一天吧……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_67A5")

    label("loc_6770")


    #C0426
    ChrTalk(
        0xFE,
        (
            "我家柔软舒适的大床……\x01",
            "好舒服啊（小声嘟嚷）……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_67A5")

    TalkEnd(0xFE)
    Return()

    # Function_20_64FE end

    def Function_21_67A9(): pass

    label("Function_21_67A9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_6813")

    #C0427
    ChrTalk(
        0xFE,
        "……必须为旅行做好准备。\x02",
    )

    CloseMessageWindow()

    #C0428
    ChrTalk(
        0xFE,
        (
            "这次我要踏平\x01",
            "玛因兹山脉。\x02",
        )
    )

    CloseMessageWindow()

    #C0429
    ChrTalk(
        0xFE,
        "我之前就很想去那里了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_69DE")

    label("loc_6813")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_6824")
    Call(0, 13)
    Jump("loc_69DE")

    label("loc_6824")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_686C")

    #C0430
    ChrTalk(
        0xFE,
        "差不多该开始下一个旅程了。\x02",
    )

    CloseMessageWindow()

    #C0431
    ChrTalk(
        0xFE,
        "……接着要去哪里呢？\x02",
    )

    CloseMessageWindow()
    Jump("loc_69DE")

    label("loc_686C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_68D8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6887")
    Call(0, 22)
    Jump("loc_68D3")

    label("loc_6887")


    #C0432
    ChrTalk(
        0xFE,
        (
            "今天和卡缇莉娜\x01",
            "约好去郊外散步。\x02",
        )
    )

    CloseMessageWindow()

    #C0433
    ChrTalk(
        0xFE,
        (
            "……带她去一个\x01",
            "风景很棒的地方吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_68D3")

    Jump("loc_69DE")

    label("loc_68D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_692F")
    OP_93(0xFE, 0x0, 0x0)

    #C0434
    ChrTalk(
        0xFE,
        "嗯，游行车队真华丽啊……\x02",
    )

    CloseMessageWindow()

    #C0435
    ChrTalk(
        0xFE,
        "看上去，就像是要踏上旅途一样。\x02",
    )

    CloseMessageWindow()
    Jump("loc_69DE")

    label("loc_692F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_6940")
    Call(0, 22)
    Jump("loc_69DE")

    label("loc_6940")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_694E")
    Jump("loc_69DE")

    label("loc_694E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_695C")
    Jump("loc_69DE")

    label("loc_695C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_69DE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_69C3")

    #C0436
    ChrTalk(
        0xFE,
        (
            "好久没回家了，\x01",
            "……街上竟然这么喧闹。\x02",
        )
    )

    CloseMessageWindow()

    #C0437
    ChrTalk(
        0xFE,
        (
            "真的好吵……\x01",
            "所以说人类……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_69DE")

    label("loc_69C3")

    OP_93(0xFE, 0xB4, 0x0)

    #C0438
    ChrTalk(
        0xFE,
        "不管了，睡觉。\x02",
    )

    CloseMessageWindow()

    label("loc_69DE")

    TalkEnd(0xFE)
    Return()

    # Function_21_67A9 end

    def Function_22_69E2(): pass

    label("Function_22_69E2")

    OP_4B(0x11, 0xFF)
    OP_4B(0x12, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_6A84")
    OP_93(0x11, 0x0, 0x0)
    OP_93(0x12, 0x5A, 0x0)

    #C0439
    ChrTalk(
        0x12,
        "琪露露做的饭菜很棒啊……\x02",
    )

    CloseMessageWindow()

    #C0440
    ChrTalk(
        0x11,
        "因为找不到旅店时就只能露宿野外啊。\x02",
    )

    CloseMessageWindow()

    #C0441
    ChrTalk(
        0x11,
        "快点吃完，然后出去玩吧。\x02",
    )

    CloseMessageWindow()

    #C0442
    ChrTalk(
        0x12,
        "嗯、嗯，好的。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    SetScenarioFlags(0x0, 7)
    Jump("loc_6C1B")

    label("loc_6A84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_6C1B")
    TurnDirection(0x11, 0x12, 0)
    TurnDirection(0x12, 0x11, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6B8F")

    #C0443
    ChrTalk(
        0x11,
        "隆他们也出去了，我们来玩吧。\x02",
    )

    CloseMessageWindow()

    #C0444
    ChrTalk(
        0x12,
        "好啊，不过要玩什么呢？\x02",
    )

    CloseMessageWindow()

    #C0445
    ChrTalk(
        0x11,
        (
            "我收集了很多\x01",
            "的纪念品。\x02",
        )
    )

    CloseMessageWindow()

    #C0446
    ChrTalk(
        0x11,
        (
            "这个小瓶子里的沙子，\x01",
            "是从共和国的沙滩上收集的哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x12, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0447
    ChrTalk(
        0x12,
        (
            "……琪露露还是老样子啊，\x01",
            "喜欢摆弄些奇怪的东西。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_6C1B")

    label("loc_6B8F")


    #C0448
    ChrTalk(
        0x11,
        (
            "这是旧导力列车上的金属片，\x01",
            "是贝尔加德门的人给我的。\x02",
        )
    )

    CloseMessageWindow()

    #C0449
    ChrTalk(
        0x11,
        (
            "这是在利贝尔的飞行船上\x01",
            "所使用的导力灯的零件。\x02",
        )
    )

    CloseMessageWindow()

    #C0450
    ChrTalk(
        0x12,
        "呵呵，都是些奇怪的东西呢。\x02",
    )

    CloseMessageWindow()

    label("loc_6C1B")

    OP_4C(0x11, 0xFF)
    OP_4C(0x12, 0xFF)
    Return()

    # Function_22_69E2 end

    def Function_23_6C24(): pass

    label("Function_23_6C24")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_6CA1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6C42")
    Call(0, 22)
    Jump("loc_6C9C")

    label("loc_6C42")


    #C0451
    ChrTalk(
        0xFE,
        (
            "不愧是经常\x01",
            "独自出去旅行的人啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0452
    ChrTalk(
        0xFE,
        (
            "但连调味技巧都如此完美，\x01",
            "倒还真是有些意外呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6C9C")

    Jump("loc_6D00")

    label("loc_6CA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_6CF4")
    OP_93(0xFE, 0x0, 0x0)

    #C0453
    ChrTalk(
        0xFE,
        "今年的游行队伍里有好多车啊。\x02",
    )

    CloseMessageWindow()

    #C0454
    ChrTalk(
        0xFE,
        "琪露露也觉得很壮观吧？\x02",
    )

    CloseMessageWindow()
    Jump("loc_6D00")

    label("loc_6CF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_6D00")
    Call(0, 22)

    label("loc_6D00")

    TalkEnd(0xFE)
    Return()

    # Function_23_6C24 end

    def Function_24_6D04(): pass

    label("Function_24_6D04")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6DA2")
    OP_29(0x46, 0x1, 0xB)

    #C0455
    ChrTalk(
        0x101,
        (
            "#0003F（这样就把\x01",
            "　西街巡查一遍了……）\x02\x03",

            "#0001F（……大家的调查情况\x01",
            "　不知如何了。）\x02",
        )
    )

    CloseMessageWindow()

    #C0456
    ChrTalk(
        0x160,
        "#3308F（…………………………）\x02",
    )

    CloseMessageWindow()
    OP_D0(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0xB9, 7)

    label("loc_6DA2")

    Return()

    # Function_24_6D04 end

    def Function_25_6DA3(): pass

    label("Function_25_6DA3")

    EventBegin(0x0)
    Fade(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_6E2A")
    OP_68(56910, 1000, 104970, 0)
    MoveCamera(45, 24, 0, 0)
    OP_6E(260, 0)
    SetCameraDistance(28000, 0)
    SetChrPos(0x101, 56750, 0, 104300, 0)
    SetChrPos(0x102, 57300, 0, 103300, 0)
    SetChrPos(0x103, 56100, 0, 103300, 0)
    SetChrPos(0x104, 56750, 0, 102300, 0)
    Jump("loc_6E9C")

    label("loc_6E2A")

    OP_68(51830, 1200, 115000, 0)
    MoveCamera(45, 24, 0, 0)
    OP_6E(260, 0)
    SetCameraDistance(28000, 0)
    SetChrPos(0x101, 51830, 0, 114500, 0)
    SetChrPos(0x102, 51300, 0, 113500, 0)
    SetChrPos(0x103, 52300, 0, 113650, 0)
    SetChrPos(0x104, 51830, 0, 112500, 0)

    label("loc_6E9C")

    OP_93(0x9, 0xB4, 0x0)
    SetChrSubChip(0x9, 0x0)
    OP_0D()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0457
    ChrTalk(
        0x9,
        "#1P哎？\x02",
    )

    CloseMessageWindow()

    #C0458
    ChrTalk(
        0x9,
        "#1P哎呀呀！这不是……\x02",
    )

    CloseMessageWindow()

    #C0459
    ChrTalk(
        0x101,
        (
            "#0012F哈哈哈……\x01",
            "阿姨，我回来了。\x02\x03",

            "不好意思，\x01",
            "这么晚才来跟您打招呼。\x02",
        )
    )

    CloseMessageWindow()

    #C0460
    ChrTalk(
        0x9,
        (
            "#1P这不是罗伊德嘛……！\x01",
            "没事没事，回来就好！\x02",
        )
    )

    CloseMessageWindow()

    #C0461
    ChrTalk(
        0x9,
        (
            "#1P我听说\x01",
            "你顺利当上警察了……\x02",
        )
    )

    CloseMessageWindow()

    #C0462
    ChrTalk(
        0x9,
        (
            "#1P……工作的地方怎么样啊。\x01",
            "开始工作了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0463
    ChrTalk(
        0x101,
        (
            "#0004F嗯，还可以……\x01",
            "算是个很轻松的好地方吧。\x02\x03",

            "#0000F科长也很少管我们。\x02",
        )
    )

    CloseMessageWindow()

    #C0464
    ChrTalk(
        0x9,
        (
            "#1P哎呀哎呀，是吗？\x01",
            "听起来好像是一个很开心的地方啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0465
    ChrTalk(
        0x9,
        (
            "#1P先不说这些，能看到你这么精神\x01",
            "地回来，我就很开心了。\x01",
            "这都要感谢空之女神啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0466
    ChrTalk(
        0x9,
        (
            "#1P……罗伊德，宿舍生活\x01",
            "要是有什么不便，\x01",
            "要随时跟阿姨说啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0467
    ChrTalk(
        0x9,
        "#1P阿姨会马上冲去你们宿舍的！\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0468
    ChrTalk(
        0x101,
        (
            "#0012F那个，我已经不是小孩子了。\x01",
            "警察学校也是寄宿制的，\x01",
            "所以我都习惯了。\x02",
        )
    )

    CloseMessageWindow()

    #C0469
    ChrTalk(
        0x9,
        (
            "#1P……罗伊德，这可不行哦！\x01",
            "你好不容易回来了，\x01",
            "得让阿姨照顾照顾你啊！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1200)

    #C0470
    ChrTalk(
        0x101,
        (
            "#0006F抱、抱歉了，阿姨……\x01",
            "下次我带些点心\x01",
            "再过来看您吧……！\x02",
        )
    )

    CloseMessageWindow()

    #C0471
    ChrTalk(
        0x104,
        "#0300F（罗伊德完全被压制住了啊。）\x02",
    )

    CloseMessageWindow()

    #C0472
    ChrTalk(
        0x103,
        (
            "#0200F（这阿姨外表虽然很温柔，\x01",
            "　没想到行动力十足啊。）\x02\x03",

            "（……他们似乎\x01",
            "　没有血缘关系呢……）\x02",
        )
    )

    CloseMessageWindow()

    #C0473
    ChrTalk(
        0x102,
        (
            "#0100F（呵呵，不过就像一家人哦。\x01",
            "　……我都有点羡慕了。）\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_72E8")
    SetChrPos(0x0, 56750, 0, 105300, 0)
    Jump("loc_72F9")

    label("loc_72E8")

    SetChrPos(0x0, 51830, 0, 114500, 0)

    label("loc_72F9")

    SetScenarioFlags(0x4E, 0)
    EventEnd(0x5)
    Return()

    # Function_25_6DA3 end

    def Function_26_72FF(): pass

    label("Function_26_72FF")

    EventBegin(0x0)
    Fade(500)
    OP_68(51830, 1200, 115000, 0)
    MoveCamera(45, 24, 0, 0)
    OP_6E(260, 0)
    SetCameraDistance(28000, 0)
    SetChrPos(0x101, 51830, 0, 114500, 0)
    SetChrPos(0x102, 51300, 0, 113500, 0)
    SetChrPos(0x103, 52300, 0, 113650, 0)
    SetChrPos(0x104, 51830, 0, 112350, 0)
    OP_93(0x9, 0xB4, 0x0)
    SetChrSubChip(0x9, 0x0)
    OP_0D()

    #C0474
    ChrTalk(
        0x101,
        (
            "#0005F对了，阿姨……\x01",
            "我昨天去见塞茜尔姐姐了。\x02\x03",

            "#0000F虽然她完全没怎么变，\x01",
            "但是太久没见，\x01",
            "我有点害羞呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0475
    ChrTalk(
        0x9,
        "啊，真的吗……\x02",
    )

    CloseMessageWindow()

    #C0476
    ChrTalk(
        0x9,
        (
            "……然后呢，怎么样？\x01",
            "她身边有没有什么好男人啊！？\x02",
        )
    )

    CloseMessageWindow()

    #C0477
    ChrTalk(
        0x101,
        (
            "#0005F咦……\x01",
            "那、那个我倒不大清楚……\x01",
            "（不如说我希望没有……）\x02",
        )
    )

    CloseMessageWindow()

    #C0478
    ChrTalk(
        0x9,
        (
            "呼，那孩子也差不多\x01",
            "该考虑考虑将来的事了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0479
    ChrTalk(
        0x9,
        (
            "……要不我帮她\x01",
            "准备一次相亲吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_98(0x104, 0x0, 0x0, 0xFA, 0x3E8, 0x0)

    #C0480
    ChrTalk(
        0x104,
        (
            "#0309F（嗯？相亲！？\x01",
            "　那我绝对要\x01",
            "　赶快报名，然后……！）\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x104, 500)

    #C0481
    ChrTalk(
        0x102,
        "#0111F（兰迪，你啊……）\x02",
    )

    CloseMessageWindow()

    #C0482
    ChrTalk(
        0x101,
        (
            "#0012F哈哈、哈哈哈……\x01",
            "（开玩笑的吧……）\x02",
        )
    )

    CloseMessageWindow()

    #C0483
    ChrTalk(
        0x103,
        (
            "#0200F罗伊德前辈……\x01",
            "你的声音哑得有些不自然哦。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 51830, 0, 114500, 0)
    SetScenarioFlags(0x70, 5)
    EventEnd(0x5)
    Return()

    # Function_26_72FF end

    def Function_27_75CC(): pass

    label("Function_27_75CC")

    EventBegin(0x0)
    Fade(500)
    OP_68(-58260, 1000, 57850, 0)
    MoveCamera(46, 24, 0, 0)
    OP_6E(260, 0)
    SetCameraDistance(32000, 0)
    SetChrPos(0x101, -57760, 0, 57480, 0)
    SetChrPos(0x102, -58760, 0, 57230, 0)
    SetChrPos(0x103, -57760, 0, 55980, 0)
    SetChrPos(0x104, -58760, 0, 55730, 0)
    SetChrSubChip(0xC, 0x0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E, 1)), scpexpr(EXPR_END)), "loc_7749")

    #C0484
    ChrTalk(
        0x101,
        (
            "#11P#0000F（菲伊先生好像不在啊……\x01",
            "　要不问下小潘莎吧。）\x02\x03",

            "……你好，潘莎。\x01",
            "菲伊先生去工作了吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0xC, 0xFF)
    OP_63(0xC, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    OP_93(0xC, 0xB4, 0x1F4)

    #C0485
    ChrTalk(
        0xC,
        (
            "#5P啊，是温蒂姐姐\x01",
            "的朋友。\x02",
        )
    )

    CloseMessageWindow()

    #C0486
    ChrTalk(
        0xC,
        "#5P你好，有什么事吗？\x02",
    )

    CloseMessageWindow()

    #C0487
    ChrTalk(
        0x101,
        (
            "#11P#0000F嗯，有点事\x01",
            "想问一下\x01",
            "菲伊叔叔……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7884")

    label("loc_7749")


    #C0488
    ChrTalk(
        0x101,
        (
            "#11P#0000F（菲伊先生好像不在啊……\x01",
            "　要不问下这孩子吧。）\x02\x03",

            "#0005F啊，你好像是……\x01",
            "菲伊先生家的\x01",
            "那个小妹妹吧？\x02\x03",

            "虽然是温蒂的妹妹，\x01",
            "但长得完全不像呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0xC, 0xFF)
    OP_63(0xC, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    OP_93(0xC, 0xB4, 0x1F4)

    #C0489
    ChrTalk(
        0xC,
        (
            "#5P啊……大哥哥好像\x01",
            "是温蒂姐姐的\x01",
            "朋友吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0490
    ChrTalk(
        0x101,
        (
            "#11P#0002F哈哈，你还记得我啊。\x02\x03",

            "有点事想问\x01",
            "一下菲伊叔叔……\x01",
            "他去工作了吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7884")


    #C0491
    ChrTalk(
        0xC,
        "#5P爸爸出差去了。\x02",
    )

    CloseMessageWindow()

    #C0492
    ChrTalk(
        0xC,
        "#5P还有两个月才能回来哦。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x71, 5)), scpexpr(EXPR_END)), "loc_7901")

    #C0493
    ChrTalk(
        0x101,
        (
            "#11P#0003F啊，好像是听说过呢……\x01",
            "………真没办法……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_792B")

    label("loc_7901")


    #C0494
    ChrTalk(
        0x101,
        "#11P#0003F这、这样啊，那没办法了……\x02",
    )

    CloseMessageWindow()

    label("loc_792B")


    #C0495
    ChrTalk(
        0x104,
        (
            "#12P#0306F也不能随便就\x01",
            "搜别人的家。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0496
    ChrTalk(
        0xC,
        "#5P你们在找什么吗？\x02",
    )

    CloseMessageWindow()

    #C0497
    ChrTalk(
        0x102,
        (
            "#12P#0100F我们是来拿\x01",
            "你爸爸借走的\x01",
            "那本书的。\x02",
        )
    )

    CloseMessageWindow()

    #C0498
    ChrTalk(
        0x103,
        "#11P#0200F……你有听他说起过吗？\x02",
    )

    CloseMessageWindow()

    #C0499
    ChrTalk(
        0xC,
        "#5P嗯……\x02",
    )

    CloseMessageWindow()

    #C0500
    ChrTalk(
        0xC,
        (
            "#5P莫非，\x01",
            "是我正在读的这本书吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0501
    ChrTalk(
        0x101,
        (
            "#11P#0005F啊……\x01",
            "能拿来让我们看看吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0502
    ChrTalk(
        0xC,
        "#5P请随便看。\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    #A0503
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "潘莎把自己拿着的书\x01",
            "递给了罗伊德他们。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0504
    ChrTalk(
        0x101,
        (
            "#11P#0000F……有图书馆的印章，\x01",
            "应该就是这本书了。\x02",
        )
    )

    CloseMessageWindow()

    #C0505
    ChrTalk(
        0xC,
        "#5P啊，这样啊。\x02",
    )

    CloseMessageWindow()

    #C0506
    ChrTalk(
        0xC,
        (
            "#5P爸爸也真是的，\x01",
            "竟然没还书\x01",
            "就去出差了……\x02",
        )
    )

    CloseMessageWindow()

    #C0507
    ChrTalk(
        0xC,
        (
            "#5P大哥哥，既然这样，\x01",
            "这本书你就拿走吧～\x02",
        )
    )

    CloseMessageWindow()

    #C0508
    ChrTalk(
        0x101,
        (
            "#11P#0005F可以吗？\x01",
            "你不是正在读吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0509
    ChrTalk(
        0x103,
        (
            "#11P#0200F申请一下的话，\x01",
            "应该可以延长返还期限吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0510
    ChrTalk(
        0xC,
        "#5P没关系。\x02",
    )

    CloseMessageWindow()

    #C0511
    ChrTalk(
        0xC,
        (
            "#5P我只是闲着没事才看的，\x01",
            "这本书其实很无聊。\x02",
        )
    )

    CloseMessageWindow()

    #C0512
    ChrTalk(
        0xC,
        "#5P你看下书名吧。\x02",
    )

    CloseMessageWindow()

    #C0513
    ChrTalk(
        0x101,
        (
            "#11P#0000F嗯，是什么啊……\x01",
            "《铁道爱好者的推荐》……\x02",
        )
    )

    CloseMessageWindow()

    #C0514
    ChrTalk(
        0x104,
        "#12P#0300F听标题就能莫名地感觉到，这绝对是本面向发烧友的书。\x02",
    )

    CloseMessageWindow()

    #C0515
    ChrTalk(
        0xC,
        (
            "#5P爸爸应该\x01",
            "是想把我引向铁路技师的世界，\x01",
            "所以才借来这本书的吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0516
    ChrTalk(
        0xC,
        (
            "#5P我才不会上他的当。\x01",
            "大哥哥，你们\x01",
            "快把它拿走吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0517
    ChrTalk(
        0x101,
        (
            "#11P#0000F嗯、嗯，好的。\x01",
            "非常感谢你的协助。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0518
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x2D5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x2D5, 1)
    OP_29(0x5, 0x1, 0x2)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x3)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7D85")
    OP_29(0x5, 0x1, 0x1F)

    label("loc_7D85")

    SetChrPos(0x0, -58260, 0, 57480, 0)
    OP_93(0xC, 0x0, 0x0)
    OP_4C(0xC, 0xFF)
    SetScenarioFlags(0x0, 4)
    EventEnd(0x5)
    Return()

    # Function_27_75CC end

    def Function_28_7DA7(): pass

    label("Function_28_7DA7")

    OP_4B(0xD, 0xFF)
    OP_4B(0xE, 0xFF)
    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-56430, 1100, 108630, 0)
    MoveCamera(37, 18, 0, 0)
    OP_6E(260, 0)
    SetCameraDistance(34090, 0)
    OP_4B(0x13, 0xFF)
    SetChrPos(0x101, -55690, 0, 108350, 270)
    SetChrPos(0x102, -54350, 0, 108180, 270)
    SetChrPos(0x103, -55690, 0, 109530, 270)
    SetChrPos(0x104, -54390, 0, 109530, 270)
    SetChrPos(0xD, -58000, 0, 107500, 0)
    SetChrPos(0xE, -57930, 0, 110500, 180)
    FadeToBright(1000, 0)
    OP_0D()
    OP_93(0xD, 0x5A, 0x1F4)
    OP_93(0xE, 0x5A, 0x1F4)
    Sleep(300)

    #C0519
    ChrTalk(
        0xD,
        "#12P啊，这不是支援科的哥哥姐姐们吗！？\x02",
    )

    CloseMessageWindow()

    #C0520
    ChrTalk(
        0xE,
        (
            "#6P各位……\x01",
            "那个，好久不见了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0521
    ChrTalk(
        0x101,
        (
            "#11P#0000F是啊，有一个星期了吧。\x02\x03",

            "#0005F那么……你们在做什么呢？\x01",
            "那只小猫咪是……？\x02",
        )
    )

    CloseMessageWindow()

    #C0522
    ChrTalk(
        0x102,
        (
            "#11P#0105F好小的小猫咪啊。\x01",
            "估计只有半岁吧。\x02\x03",

            "#0100F这是你们养的吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0523
    ChrTalk(
        0xE,
        (
            "#6P不是的，其实是……\x01",
            "我们在西街发现的。\x02",
        )
    )

    CloseMessageWindow()

    #C0524
    ChrTalk(
        0xE,
        "#6P好像是迷路了。\x02",
    )

    CloseMessageWindow()

    #C0525
    ChrTalk(
        0xD,
        (
            "#12P刚被发现的时候，它还很虚弱，\x01",
            "我们就喂了点吃的给它。\x02",
        )
    )

    CloseMessageWindow()

    #C0526
    ChrTalk(
        0xD,
        (
            "#12P所以才变得这么有精神呢～\x01",
            "很棒吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1200)

    #C0527
    ChrTalk(
        0xE,
        "#6P啊哈哈，不过………\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xE, 0xD, 500)
    Sleep(300)

    #C0528
    ChrTalk(
        0xE,
        (
            "#6P喂，隆，要不就把那件事\x01",
            "委托给支援科的各位吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xE, 500)
    Sleep(300)

    #C0529
    ChrTalk(
        0xD,
        "#12P咦？那个吗？\x02",
    )

    CloseMessageWindow()

    #C0530
    ChrTalk(
        0xE,
        "#6P因为，只靠我们的话……\x02",
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
    Sleep(1200)

    #C0531
    ChrTalk(
        0x104,
        "#0305F#11P那个？是指什么啊？\x02",
    )

    CloseMessageWindow()
    OP_93(0xD, 0x5A, 0x1F4)
    OP_93(0xE, 0x5A, 0x1F4)

    #C0532
    ChrTalk(
        0xE,
        (
            "#6P那个，其实，\x01",
            "我们有件事想拜托大家……\x02",
        )
    )

    CloseMessageWindow()

    #C0533
    ChrTalk(
        0xE,
        "#6P可以听我们说吗？\x02",
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(300)
    SetChrName("")

    #A0534
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "隆和亨利把发现小猫\x01",
            "的经过详细说给了罗伊德他们听。\x02",
        )
    )

    CloseMessageWindow()

    #A0535
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "然后……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(1000, 0)
    OP_0D()

    #C0536
    ChrTalk(
        0x103,
        (
            "#0205F#11P你们是想要\x01",
            "我们帮忙寻找小猫的主人吧……？\x02",
        )
    )

    CloseMessageWindow()

    #C0537
    ChrTalk(
        0xE,
        (
            "#6P嗯，其实我们发现它的时候，\x01",
            "它脖子上戴着项圈。\x02",
        )
    )

    CloseMessageWindow()

    #C0538
    ChrTalk(
        0xE,
        (
            "#6P因为当时看它好像很难受，\x01",
            "就帮它摘下来了。\x01",
            "所以我想它应该是有主人的吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0539
    ChrTalk(
        0xD,
        (
            "#12P而且它好像都不愿意\x01",
            "亲近我们。\x02",
        )
    )

    CloseMessageWindow()

    #C0540
    ChrTalk(
        0x101,
        (
            "#11P#0003F是吗……确实，如果它有主人，\x01",
            "那主人现在应该很担心吧……\x02\x03",

            "#0001F而且为了小猫好，也应该把它送回去呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0541
    ChrTalk(
        0x102,
        (
            "#11P#0100F关于它的主人，\x01",
            "你们有什么线索吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0542
    ChrTalk(
        0xD,
        (
            "#12P嗯～我想想看哦，\x01",
            "我和亨利猜想\x01",
            "它的主人或许是个小孩子。\x02",
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

    #C0543
    ChrTalk(
        0xE,
        "#6P因为它戴着的项圈是手工做的，\x02",
    )

    CloseMessageWindow()

    #C0544
    ChrTalk(
        0xE,
        (
            "#6P而且比起大人，\x01",
            "更像是跟我们差不多大的\x01",
            "小孩子做的。\x02",
        )
    )

    CloseMessageWindow()

    #C0545
    ChrTalk(
        0x104,
        (
            "#0303F#11P嗯，这样的话，\x01",
            "询问对象就该以\x01",
            "小孩子们为主了……\x02\x03",

            "好像要花不少时间啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)

    #C0546
    ChrTalk(
        0x104,
        "#0300F#11P罗伊德，要怎么做？\x02",
    )

    CloseMessageWindow()

    #C0547
    ChrTalk(
        0x101,
        "#11P#0003F我想想啊……\x02",
    )

    CloseMessageWindow()
    OP_29(0x8, 0x4, 0x2)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【接受】\x01",      # 0
            "【拒绝】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_5A()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_8594"),
        (1, "loc_859E"),
        (SWITCH_DEFAULT, "loc_8652"),
    )


    label("loc_8594")

    OP_29(0x8, 0x1, 0x2)
    Call(0, 29)
    Return()

    label("loc_859E")


    #C0548
    ChrTalk(
        0x101,
        (
            "#11P#0006F抱歉啊，我们现在脱不开身，\x01",
            "等有空了，\x01",
            "再来帮你们找……\x02",
        )
    )

    CloseMessageWindow()

    #C0549
    ChrTalk(
        0xE,
        (
            "#6P知道了，在那之前就由我们\x01",
            "来照顾它吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0550
    ChrTalk(
        0xD,
        (
            "#12P嘁，真没办法。\x01",
            "大哥哥，\x01",
            "拜托你们早点来哦！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_29(0x8, 0x1, 0x0)
    Jump("loc_8652")

    label("loc_8652")

    Fade(500)
    SetChrPos(0x0, -55530, 0, 109140, 270)
    OP_93(0xD, 0x0, 0x0)
    OP_93(0xE, 0xB4, 0x0)
    OP_4C(0x13, 0xFF)
    OP_4C(0xD, 0xFF)
    OP_4C(0xE, 0xFF)
    EventEnd(0x5)
    Return()

    # Function_28_7DA7 end

    def Function_29_8685(): pass

    label("Function_29_8685")

    SetChrFlags(0xD, 0x40)
    OP_4B(0x13, 0xFF)

    #C0551
    ChrTalk(
        0x101,
        (
            "#11P#0000F好吧，虽然去乌尔斯拉医院的\x01",
            "计划会有点耽搁……\x01",
            "但还是帮忙找找小猫的主人吧。\x02\x03",

            "不过首先得\x01",
            "带上小猫一起去找。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    TurnDirection(0x103, 0x101, 500)
    TurnDirection(0x104, 0x101, 500)
    Sleep(200)

    #C0552
    ChrTalk(
        0x103,
        (
            "#0200F罗伊德前辈，这小猫\x01",
            "并没有什么体力……\x02",
        )
    )

    CloseMessageWindow()

    #C0553
    ChrTalk(
        0x102,
        (
            "#11P#0105F让它跟着走，\x01",
            "会不会太残忍了点啊？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_87DC():

        label("loc_87DC")

        TurnDirection(0xFE, 0x101, 300)
        Yield()
        Jump("loc_87DC")

    QueueWorkItem2(0xE, 1, lambda_87DC)

    def lambda_87EE():

        label("loc_87EE")

        TurnDirection(0xFE, 0x101, 300)
        Yield()
        Jump("loc_87EE")

    QueueWorkItem2(0x103, 1, lambda_87EE)

    def lambda_8800():

        label("loc_8800")

        TurnDirection(0xFE, 0x101, 300)
        Yield()
        Jump("loc_8800")

    QueueWorkItem2(0x104, 1, lambda_8800)

    def lambda_8812():

        label("loc_8812")

        TurnDirection(0xFE, 0x101, 300)
        Yield()
        Jump("loc_8812")

    QueueWorkItem2(0x102, 1, lambda_8812)
    BeginChrThread(0x101, 1, 0, 30)
    OP_68(-55760, 500, 110100, 3000)

    #C0554
    ChrTalk(
        0x101,
        (
            "#11P#0004F没事，我有办法。\x02\x03",

            "#0000F先把它交给我好吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0555
    ChrTalk(
        0xD,
        "#6P嗯……\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 1)
    BeginChrThread(0xD, 1, 0, 31)
    Sleep(300)

    def lambda_8891():
        OP_95(0xFE, -58000, 0, 107500, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8891)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0x0, 0x1F4)
    Sleep(500)
    OP_6F(0x1)
    EndChrThread(0xE, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x102, 0x1)

    #C0556
    ChrTalk(
        0x101,
        "#11P#0009F好的，过来过来……\x02",
    )

    CloseMessageWindow()
    Sound(823, 0, 100, 0)
    Sleep(200)
    TurnDirection(0x13, 0x101, 300)
    Sleep(800)
    OP_95(0x13, -58010, 700, 108520, 300, 0x0)
    OP_93(0x13, 0xB4, 0x1F4)
    Sleep(1000)
    Sound(804, 0, 100, 0)
    Fade(500)
    SetChrFlags(0x13, 0x80)
    OP_0D()
    FadeToDark(300, 0, 100)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0557
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德抱起小猫，\x01",
            "轻轻放进上衣里面。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)

    #C0558
    ChrTalk(
        0x101,
        (
            "#11P#0000F嗯，这样应该\x01",
            "就没问题了。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)
    Sleep(300)

    #C0559
    ChrTalk(
        0x101,
        (
            "#5P#0000F怎么样，我想现在就能\x01",
            "安全地移动了。\x02",
        )
    )

    CloseMessageWindow()

    #C0560
    ChrTalk(
        0x104,
        "#0309F#11P哦哦，挺不错的啊。\x02",
    )

    CloseMessageWindow()

    #C0561
    ChrTalk(
        0x103,
        "#0200F#11P还挺有办法呢。\x02",
    )

    CloseMessageWindow()

    #C0562
    ChrTalk(
        0x102,
        (
            "#11P#0100F呵呵，出乎意料\x01",
            "地顺利啊。\x02\x03",

            "那么，这次询问的对象\x01",
            "……就主要以孩子们为中心，\x01",
            "没错吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x102, 500)
    TurnDirection(0xD, 0x102, 500)

    #C0563
    ChrTalk(
        0xE,
        "#6P嗯，还有……\x02",
    )

    CloseMessageWindow()

    #C0564
    ChrTalk(
        0xE,
        (
            "#6P小猫是在住宅街附近\x01",
            "发现的，说不定\x01",
            "是从对面误闯进来的……\x02",
        )
    )

    CloseMessageWindow()

    #C0565
    ChrTalk(
        0x101,
        (
            "#11P#0003F总而言之，\x01",
            "应该是在住宅区一带……\x02\x03",

            "#0000F好，目标是有小孩的家庭，\x01",
            "一家一家去问吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0566
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【寻找小猫的饲主】\x07\x00",
            "开始！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C7(0x0, 0x1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -55530, 0, 109140, 180)
    SetChrPos(0xD, -57650, 0, 110300, 180)
    SetChrPos(0xE, -58450, 0, 110300, 180)
    OP_4C(0xD, 0xFF)
    OP_4C(0xE, 0xFF)
    ClearChrFlags(0xD, 0x40)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_29_8685 end

    def Function_30_8BEE(): pass

    label("Function_30_8BEE")

    OP_95(0x101, -56270, 0, 107500, 1000, 0x0)
    OP_95(0x101, -57120, 0, 107500, 1000, 0x0)
    OP_93(0x101, 0x10E, 0x1F4)
    Return()

    # Function_30_8BEE end

    def Function_31_8C1E(): pass

    label("Function_31_8C1E")

    OP_95(0xD, -57290, 0, 106710, 1000, 0x0)
    OP_93(0xD, 0x0, 0x1F4)
    Return()

    # Function_31_8C1E end

    def Function_32_8C3A(): pass

    label("Function_32_8C3A")

    EventBegin(0x0)
    Fade(500)
    OP_4B(0xD, 0xFF)
    OP_4B(0xE, 0xFF)
    OP_68(-54300, 700, 110230, 0)
    MoveCamera(45, 24, 0, 0)
    OP_6E(260, 0)
    SetCameraDistance(31500, 0)
    SetChrPos(0x101, -54200, 0, 108980, 0)
    SetChrPos(0x102, -55340, 0, 107320, 0)
    SetChrPos(0x103, -55340, 0, 108980, 0)
    SetChrPos(0x104, -54200, 0, 107320, 0)
    SetChrPos(0xD, -53900, 0, 110740, 180)
    SetChrPos(0xE, -55030, 0, 110700, 180)
    OP_0D()

    #C0567
    ChrTalk(
        0xD,
        "#5P哦，大哥哥们。\x02",
    )

    CloseMessageWindow()

    #C0568
    ChrTalk(
        0xD,
        (
            "#5P怎么样了～\x01",
            "找到小猫的主人了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0569
    ChrTalk(
        0x101,
        (
            "#0000F嗯，当然了。\x02\x03",

            "虽然费了点周折，\x01",
            "但小猫现在已经\x01",
            "毫发无伤地回到主人身边了哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0570
    ChrTalk(
        0xD,
        (
            "#5P这、这样啊……\x01",
            "…………………\x02",
        )
    )

    CloseMessageWindow()

    #C0571
    ChrTalk(
        0xE,
        (
            "#5P太好了，\x01",
            "只靠我们的话，\x01",
            "估计会照顾不好小猫的。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xE, 0xD, 300)
    Sleep(300)

    #C0572
    ChrTalk(
        0xE,
        (
            "#5P……隆？\x01",
            "莫非你舍不得了？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0xD, 0xE, 500)

    #C0573
    ChrTalk(
        0xD,
        "#11P我、我才没有！\x02",
    )

    CloseMessageWindow()
    OP_93(0xD, 0x0, 0x1F4)
    Sleep(300)

    #C0574
    ChrTalk(
        0xD,
        (
            "#11P亨利，\x01",
            "快点收拾完，\x01",
            "咱们好出去玩啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0575
    ChrTalk(
        0xE,
        "#5P嗯，也是啊。\x02",
    )

    CloseMessageWindow()
    OP_93(0xE, 0xB4, 0x1F4)
    Sleep(300)

    #C0576
    ChrTalk(
        0xE,
        (
            "#5P各位，\x01",
            "谢谢你们了！\x02",
        )
    )

    CloseMessageWindow()

    #C0577
    ChrTalk(
        0x104,
        "#12P#0309F嗯，真是个坦率有礼的好孩子啊。\x02",
    )

    CloseMessageWindow()

    #C0578
    ChrTalk(
        0x102,
        (
            "#12P#0100F如果还有什么困难，\x01",
            "记得联络支援科哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -54960, 0, 107860, 0)
    SetChrPos(0xD, -54470, 0, 110810, 315)
    SetChrPos(0xE, -57280, 0, 107430, 315)
    OP_4C(0xD, 0xFF)
    OP_4C(0xE, 0xFF)
    SetScenarioFlags(0x70, 2)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_32_8C3A end

    SaveToFile()

Try(main)
