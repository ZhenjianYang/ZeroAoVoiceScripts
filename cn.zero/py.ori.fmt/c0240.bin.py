from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "c0240.bin",                # FileName
        "c0240",                    # MapName
        "c0240",                    # Location
        0x000F,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 15, 0, 6, 0, 7],
    )

    BuildStringList((
        "c0240",                  # 0
        "萨米",                   # 1
        "金德尔",                 # 2
        "金德尔",                 # 3
        "布里吉塔",               # 4
        "卢威克老人",             # 5
        "卢威克老人",             # 6
        "奥丽加夫人",             # 7
        "奥丽加夫人",             # 8
        "搜查官",                 # 9
        "搜查官",                 # 10
        "伊莉娅",                 # 11
        "伊莉娅",                 # 12
        "莉夏",                   # 13
        "修利",                   # 14
    ))

    AddCharChip((
        "chr/ch25600.itc",                   # 00
        "chr/ch21800.itc",                   # 01
        "chr/ch21802.itc",                   # 02
        "chr/ch21600.itc",                   # 03
        "chr/ch21602.itc",                   # 04
        "chr/ch20100.itc",                   # 05
        "chr/ch20102.itc",                   # 06
        "chr/ch20300.itc",                   # 07
        "chr/ch27600.itc",                   # 08
        "chr/ch27800.itc",                   # 09
        "apl/ch50386.itc",                   # 0A
        "chr/ch05200.itc",                   # 0B
        "chr/ch10000.itc",                   # 0C
        "chr/ch05102.itc",                   # 0D
    ))

    DeclNpc(9060,    10000,   18000,   45,   257,  0x0, 0,   0,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(3170,    1049,    60459,   90,   385,  0x0, 0,   1,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(-2009,   1149,    60479,   270,  341,  0x0, 0,   2,   0,   255, 255, 0,   10,  255,  0)
    DeclNpc(8470,    1019,    62380,   0,    257,  0x0, 0,   7,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(-45650,  1019,    60169,   180,  257,  0x0, 0,   3,   0,   0,   3,   0,   12,  255,  0)
    DeclNpc(-48700,  1200,    60400,   270,  469,  0x0, 0,   4,   0,   255, 255, 0,   13,  255,  0)
    DeclNpc(-39810,  1029,    62639,   0,    385,  0x0, 0,   5,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(7030,    150,     6969,    180,  341,  0x0, 0,   6,   0,   255, 255, 0,   16,  255,  0)
    DeclNpc(1539,    10000,   19700,   180,  385,  0x0, 0,   8,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(50069,   1049,    62479,   0,    401,  0x0, 0,   9,   0,   0,   0,   0,   18,  255,  0)
    DeclNpc(59099,   1549,    53029,   90,   469,  0x0, 0,   10,  0,   255, 255, 0,   19,  255,  0)
    DeclNpc(59099,   1549,    53029,   90,   503,  0x0, 0,   10,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(58290,   1029,    62500,   0,    389,  0x0, 0,   11,  0,   0,   0,   0,   20,  255,  0)
    DeclNpc(51930,   1049,    60970,   135,  389,  0x0, 0,   12,  0,   0,   0,   0,   21,  255,  0)

    DeclEvent(0x0000, 0, 24,  49.79999923706055,     51.150001525878906,    0.029999999329447746,  9.0,                   [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000001788139343,   0.0,                   -16.600000381469727,   -25.575000762939453,   -0.0060000005178153515, 1.0])

    DeclActor(0,       10000,   20600,   1000,    0,       11000,   20600,   0x007C, 0,  33, 0x0000)
    DeclActor(50350,   1050,    60430,   2000,    50350,   2000,    60430,   0x007C, 0,  34, 0x0000)
    DeclActor(58690,   1000,    52860,   3000,    58690,   2000,    52860,   0x007C, 0,  35, 0x0000)

    ScpFunction((
        "Function_0_3B4",          # 00, 0
        "Function_1_46C",          # 01, 1
        "Function_2_497",          # 02, 2
        "Function_3_4C2",          # 03, 3
        "Function_4_4ED",          # 04, 4
        "Function_5_518",          # 05, 5
        "Function_6_543",          # 06, 6
        "Function_7_8B9",          # 07, 7
        "Function_8_B4F",          # 08, 8
        "Function_9_21BF",         # 09, 9
        "Function_10_22E2",        # 0A, 10
        "Function_11_34CA",        # 0B, 11
        "Function_12_4224",        # 0C, 12
        "Function_13_5170",        # 0D, 13
        "Function_14_52FD",        # 0E, 14
        "Function_15_53B9",        # 0F, 15
        "Function_16_5680",        # 10, 16
        "Function_17_621C",        # 11, 17
        "Function_18_64B8",        # 12, 18
        "Function_19_65DD",        # 13, 19
        "Function_20_6A9B",        # 14, 20
        "Function_21_6D09",        # 15, 21
        "Function_22_6F25",        # 16, 22
        "Function_23_7124",        # 17, 23
        "Function_24_7A9F",        # 18, 24
        "Function_25_7DD2",        # 19, 25
        "Function_26_8AD8",        # 1A, 26
        "Function_27_8B2E",        # 1B, 27
        "Function_28_8B4A",        # 1C, 28
        "Function_29_8B66",        # 1D, 29
        "Function_30_A9E3",        # 1E, 30
        "Function_31_AA10",        # 1F, 31
        "Function_32_AA36",        # 20, 32
        "Function_33_AA65",        # 21, 33
        "Function_34_AAB1",        # 22, 34
        "Function_35_AC92",        # 23, 35
        "Function_36_ADDD",        # 24, 36
    ))


    def Function_0_3B4(): pass

    label("Function_0_3B4")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_3F4"),
        (1, "loc_400"),
        (2, "loc_40C"),
        (3, "loc_418"),
        (4, "loc_424"),
        (5, "loc_430"),
        (6, "loc_43C"),
        (SWITCH_DEFAULT, "loc_448"),
    )


    label("loc_3F4")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_454")

    label("loc_400")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_454")

    label("loc_40C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_454")

    label("loc_418")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_454")

    label("loc_424")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_454")

    label("loc_430")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_454")

    label("loc_43C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_454")

    label("loc_448")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_454")

    label("loc_454")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_46B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_454")

    label("loc_46B")

    Return()

    # Function_0_3B4 end

    def Function_1_46C(): pass

    label("Function_1_46C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_496")
    OP_94(0xFE, 0xFFFFF858, 0x2A44, 0x866, 0x311A, 0x3E8)
    Sleep(300)
    Jump("Function_1_46C")

    label("loc_496")

    Return()

    # Function_1_46C end

    def Function_2_497(): pass

    label("Function_2_497")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4C1")
    OP_94(0xFE, 0x852, 0xF01E, 0x1036, 0xE830, 0x3E8)
    Sleep(300)
    Jump("Function_2_497")

    label("loc_4C1")

    Return()

    # Function_2_497 end

    def Function_3_4C2(): pass

    label("Function_3_4C2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4EC")
    OP_94(0xFE, 0xFFFF4C46, 0xE4C0, 0xFFFF592A, 0xF078, 0x3E8)
    Sleep(300)
    Jump("Function_3_4C2")

    label("loc_4EC")

    Return()

    # Function_3_4C2 end

    def Function_4_4ED(): pass

    label("Function_4_4ED")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_517")
    OP_94(0xFE, 0xFFFF646A, 0xCA3A, 0xFFFF688E, 0xD386, 0x3E8)
    Sleep(300)
    Jump("Function_4_4ED")

    label("loc_517")

    Return()

    # Function_4_4ED end

    def Function_5_518(): pass

    label("Function_5_518")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_542")
    OP_94(0xFE, 0xDEF8, 0xD82C, 0xEBE6, 0xE2A4, 0x3E8)
    Sleep(300)
    Jump("Function_5_518")

    label("loc_542")

    Return()

    # Function_5_518 end

    def Function_6_543(): pass

    label("Function_6_543")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_556")
    SetChrFlags(0xC, 0x80)
    Jump("loc_892")

    label("loc_556")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_564")
    Jump("loc_892")

    label("loc_564")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_577")
    SetChrFlags(0xB, 0x80)
    Jump("loc_892")

    label("loc_577")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_596")
    SetChrPos(0xB, 11480, 1000, 54590, 0)
    Jump("loc_892")

    label("loc_596")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_5CA")
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 59490, 700, 52910, 315)
    OP_A7(0x12, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Jump("loc_892")

    label("loc_5CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_5E7")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xF, 0x80)
    Jump("loc_892")

    label("loc_5E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_62B")
    SetChrPos(0x9, -990, 5000, 14750, 90)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrPos(0xB, 400, 5000, 14750, 270)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xF, 0x80)
    Jump("loc_892")

    label("loc_62B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_65E")
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrPos(0xB, 4720, 1000, 60520, 270)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xF, 0x80)
    Jump("loc_892")

    label("loc_65E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_72F")
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xF, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_68F")
    SetChrPos(0x8, 1420, 5000, 17800, 45)

    label("loc_68F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x3)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6F6")
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xC, -46140, 1030, 59110, 0)
    SetChrPos(0xE, -45740, 1030, 60980, 180)
    BeginChrThread(0xC, 0, 0, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x7)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6F6")
    SetChrFlags(0xC, 0x10)
    SetChrFlags(0xE, 0x10)

    label("loc_6F6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_72A")
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x12, 52530, 1050, 60070, 270)
    SetChrChipByIndex(0x12, 0xD)
    SetChrSubChip(0x12, 0x0)

    label("loc_72A")

    Jump("loc_892")

    label("loc_72F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_747")
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xF, 0x80)
    Jump("loc_892")

    label("loc_747")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_796")
    SetChrPos(0x8, -210, 5000, 12250, 180)
    BeginChrThread(0x8, 0, 0, 1)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xF, -49990, 1200, 61760, 180)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    Jump("loc_892")

    label("loc_796")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_7DC")
    SetChrPos(0x8, -210, 5000, 12250, 180)
    BeginChrThread(0x8, 0, 0, 1)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 58830, 1000, 56350, 180)
    BeginChrThread(0x11, 0, 0, 5)
    Jump("loc_892")

    label("loc_7DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_801")
    SetChrPos(0xC, -39220, 1000, 52790, 90)
    BeginChrThread(0xC, 0, 0, 4)
    Jump("loc_892")

    label("loc_801")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_80F")
    Jump("loc_892")

    label("loc_80F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_839")
    SetChrPos(0xB, 3570, 1000, 60560, 269)
    BeginChrThread(0xB, 0, 0, 2)
    SetChrFlags(0xA, 0x80)
    Jump("loc_892")

    label("loc_839")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_84C")
    SetChrFlags(0xB, 0x80)
    Jump("loc_892")

    label("loc_84C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_87B")
    SetChrPos(0xC, -49940, 1050, 63990, 0)
    BeginChrThread(0xC, 0, 0, 0)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    Jump("loc_892")

    label("loc_87B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_889")
    Jump("loc_892")

    label("loc_889")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_892")

    label("loc_892")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_8A6")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 22)
    Jump("loc_8B8")

    label("loc_8A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_8B8")
    ClearScenarioFlags(0x5C, 1)
    SetScenarioFlags(0x1, 3)
    Event(0, 29)

    label("loc_8B8")

    Return()

    # Function_6_543 end

    def Function_7_8B9(): pass

    label("Function_7_8B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_8CE")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x1, 3)

    label("loc_8CE")

    OP_52(0x12, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_904")
    OP_52(0x12, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_63(0x12, 0x0, 2000, 0x1C, 0x21, 0xFA, 0x0)

    label("loc_904")

    ClearMapObjFlags(0x2, 0x10)
    OP_66(0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_91C")
    Jump("loc_9AE")

    label("loc_91C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_92A")
    Jump("loc_9AE")

    label("loc_92A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_942")
    SetMapObjFlags(0x2, 0x10)
    OP_65(0x0, 0x1)
    Jump("loc_9AE")

    label("loc_942")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_950")
    Jump("loc_9AE")

    label("loc_950")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_975")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x3)"), scpexpr(EXPR_END)), "loc_970")
    SetMapObjFlags(0x2, 0x10)
    OP_65(0x0, 0x1)

    label("loc_970")

    Jump("loc_9AE")

    label("loc_975")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_983")
    Jump("loc_9AE")

    label("loc_983")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_99B")
    SetMapObjFlags(0x2, 0x10)
    OP_65(0x0, 0x1)
    Jump("loc_9AE")

    label("loc_99B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_9AE")
    SetMapObjFlags(0x2, 0x10)
    OP_65(0x0, 0x1)

    label("loc_9AE")

    SetMapObjFrame(0xFF, "huku_nugippa", 0x0, 0x1)
    SetMapObjFrame(0xFF, "model5", 0x0, 0x1)
    SetMapObjFrame(0xFF, "bed_event", 0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_9EF")
    Jump("loc_A7A")

    label("loc_9EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_A34")
    SetMapObjFrame(0xFF, "bed_event", 0x1, 0x1)
    SetMapObjFrame(0xFF, "huku_nugippa", 0x1, 0x1)
    SetMapObjFrame(0xFF, "bed_normal", 0x0, 0x1)
    Jump("loc_A7A")

    label("loc_A34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_A42")
    Jump("loc_A7A")

    label("loc_A42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_A7A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A7A")
    SetMapObjFrame(0xFF, "huku_nugippa", 0x1, 0x1)
    SetMapObjFrame(0xFF, "model5", 0x1, 0x1)

    label("loc_A7A")

    OP_65(0x1, 0x1)
    OP_65(0x2, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AA7")
    OP_66(0x1, 0x1)
    OP_66(0x2, 0x1)

    label("loc_AA7")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x9)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_ACE")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_ACE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AF0")
    OP_1B(0x8, 0x0, 0x24)

    label("loc_AF0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B0F")
    OP_10(0x0, 0x0)
    OP_10(0x8, 0x1)
    OP_10(0x7, 0x0)
    OP_10(0x9, 0x1)
    Jump("loc_B1B")

    label("loc_B0F")

    OP_10(0x0, 0x1)
    OP_10(0x8, 0x0)
    OP_10(0x7, 0x1)
    OP_10(0x9, 0x0)

    label("loc_B1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B37")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_B4E")

    label("loc_B37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_B4E")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_B4E")

    label("loc_B4E")

    Return()

    # Function_7_8B9 end

    def Function_8_B4F(): pass

    label("Function_8_B4F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x3)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_FC7")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F3D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BD2")

    #C0001
    ChrTalk(
        0x101,
        (
            "#0001F（好，开始询问线索吧。）\x02\x03",

            "#0000F打扰一下，\x01",
            "能占用您一点时间吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BD2")

    SetScenarioFlags(0x1, 2)
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德等人就跟踪狂一事\x01",
            "向对方进行了询问。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()

    #C0003
    ChrTalk(
        0xFE,
        (
            "……你说的是跟踪狂那件事啊。\x01",
            "我作为这里的管理员，\x01",
            "警惕性一直很高。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x102,
        (
            "#0100F您亲眼见到过\x01",
            "跟踪狂吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        (
            "我每天\x01",
            "都会到这里看看，\x01",
            "但基本没见过呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        "只有前些天看到过一次。\x02",
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "是个把帽檐压得很低的少年，\x01",
            "因为他很快就走掉了，\x01",
            "所以我也没有看得太清楚。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x103,
        "#0200F您还能想起其它特征吗？\x02",
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        "这个嘛……\x02",
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        (
            "非要说的话，\x01",
            "完全没有特征……也算是特征吧。\x02",
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

    #C0011
    ChrTalk(
        0xFE,
        (
            "也不知是不是因为他穿着太过朴素，\x01",
            "反正我是一点特别的印象都没有。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x104,
        "#0303F呃，竟然会这样……\x02",
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x101,
        (
            "#0000F不过，从莉夏那里听来的情报\x01",
            "似乎没错……\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x1D, 0x1, 0x4)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x5)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x6)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x7)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F38")

    #C0014
    ChrTalk(
        0x101,
        (
            "#0000F好，调查就到此结束吧。\x02\x03",

            "先回伊莉娅小姐的房间，\x01",
            "整理一下目前的情报好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x104,
        "#0300F好的，差不多也该拟定对策了！！\x02",
    )

    CloseMessageWindow()
    ModifyEventFlags(1, 0, 0x80)
    OP_29(0x1D, 0x1, 0x9)

    label("loc_F38")

    Jump("loc_FC2")

    label("loc_F3D")


    #C0016
    ChrTalk(
        0xFE,
        (
            "我看到的是一个\x01",
            "帽檐压得很低的少年，\x01",
            "没能看清他的长相。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        (
            "另外，我记得\x01",
            "他的穿着打扮非常普通。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        "我连一点特别的印象都没有。\x02",
    )

    CloseMessageWindow()

    label("loc_FC2")

    Jump("loc_21BB")

    label("loc_FC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_10BA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_105A")

    #C0019
    ChrTalk(
        0xFE,
        "好了，该工作了……\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        (
            "这也是为了把工资攒起来，\x01",
            "去看伊莉娅小姐的表演……\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        (
            "要是能买到下个月左右\x01",
            "的门票就好了～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_10B5")

    label("loc_105A")


    #C0022
    ChrTalk(
        0xFE,
        (
            "无论是做垃圾分类还是打扫水沟，\x01",
            "都是为了能见到伊莉娅小姐……\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        "好了，再努力一下吧。\x02",
    )

    CloseMessageWindow()

    label("loc_10B5")

    Jump("loc_21BB")

    label("loc_10BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_11E5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1178")

    #C0024
    ChrTalk(
        0xFE,
        (
            "前段时间，我第一次看到\x01",
            "住在三楼的人，虽然只是个背影。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xFE,
        (
            "因为她正往外走，\x01",
            "所以也没怎么看清楚……\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xFE,
        (
            "不过，是个感觉很\x01",
            "普通的人。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xFE,
        "虽然她的金发很漂亮。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_11E0")

    label("loc_1178")


    #C0028
    ChrTalk(
        0xFE,
        (
            "不过，对于爱打扮的女性来说，\x01",
            "也没什么大不了的。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        (
            "嗯，从背影来看，\x01",
            "是个很普通的人呢，真意外啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11E0")

    Jump("loc_21BB")

    label("loc_11E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_12B1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_126C")

    #C0030
    ChrTalk(
        0xFE,
        "好了，工作工作……\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        (
            "还得攒钱去看\x01",
            "彩虹剧团的表演呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xFE,
        (
            "我可是为了去看那个，\x01",
            "才会这么努力工作呢！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_12AC")

    label("loc_126C")


    #C0033
    ChrTalk(
        0xFE,
        "这一切都是为了能见到伊莉娅小姐……\x02",
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        "今天也要努力工作！\x02",
    )

    CloseMessageWindow()

    label("loc_12AC")

    Jump("loc_21BB")

    label("loc_12B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1422")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13C0")

    #C0035
    ChrTalk(
        0xFE,
        (
            "那个住在三楼的人，最近似乎\x01",
            "留小孩在家里过夜呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xFE,
        (
            "我没和住在三楼的那位打过照面，\x01",
            "但时常能见到那个孩子。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        (
            "戴着帽子，十三四岁左右，\x01",
            "是个挺好看的小孩子。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    #C0038
    ChrTalk(
        0xFE,
        (
            "…………咦？\x01",
            "说起来，之前好像在哪里\x01",
            "见过那个孩子呢……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_141D")

    label("loc_13C0")


    #C0039
    ChrTalk(
        0xFE,
        (
            "嗯～好像在哪里\x01",
            "见到过那个孩子……\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xFE,
        (
            "……呃，算了。\x01",
            "身为管理员，\x01",
            "管太多闲事也不好啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_141D")

    Jump("loc_21BB")

    label("loc_1422")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_15B6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14CD")

    #C0041
    ChrTalk(
        0xFE,
        "唔……！！\x02",
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xFE,
        "伊莉娅小姐实在是太棒了！\x02",
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xFE,
        (
            "另外……扮演『月之姬』\x01",
            "的那个演员也很厉害。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xFE,
        (
            "听说她还只是个新人，\x01",
            "但我已经完全迷上她了！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_15B1")

    label("loc_14CD")


    #C0045
    ChrTalk(
        0xFE,
        (
            "不过……伊莉娅小姐\x01",
            "究竟住在什么地方呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xFE,
        (
            "要是能知道她的住址，\x01",
            "我愿意一直追随到世界尽头！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBF, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_15B1")
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0047
    ChrTalk(
        0x101,
        (
            "#0005F（她好像完全没注意住在三楼的就是\x01",
            "  伊莉娅小姐……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15B1")

    Jump("loc_21BB")

    label("loc_15B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_15C4")
    Jump("loc_21BB")

    label("loc_15C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_169B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_162E")

    #C0048
    ChrTalk(
        0xFE,
        (
            "在刚才的那场游行中，\x01",
            "还有导力车在队伍里呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xFE,
        "世界变得越来越先进了啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1696")

    label("loc_162E")


    #C0050
    ChrTalk(
        0xFE,
        (
            "在我小时候，一说起游行，\x01",
            "只能想到花车而已呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xFE,
        (
            "……一想到这些，便不由自主地\x01",
            "感慨岁月的流逝啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1696")

    Jump("loc_21BB")

    label("loc_169B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1787")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1722")

    #C0052
    ChrTalk(
        0xFE,
        (
            "住户们今天好像\x01",
            "全都出门了……\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xFE,
        "不过，这样也好。\x02",
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xFE,
        (
            "免得一不小心听到\x01",
            "大家谈论观看新剧公演的感受。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1782")

    label("loc_1722")


    #C0055
    ChrTalk(
        0xFE,
        (
            "我明天要去看\x01",
            "彩虹剧团的新剧。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xFE,
        (
            "在那之前，绝对不要向我透露剧情哦。\x01",
            "我想体会那种新鲜感！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1782")

    Jump("loc_21BB")

    label("loc_1787")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1859")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1819")

    #C0057
    ChrTalk(
        0xFE,
        (
            "不管大家有多兴奋欢乐，\x01",
            "我都得把管理员的工作完成才行！\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xFE,
        (
            "这样就能在庆典的\x01",
            "最后一天休假，去看\x01",
            "彩虹剧团的表演了！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1854")

    label("loc_1819")


    #C0059
    ChrTalk(
        0xFE,
        (
            "好啦，开始打扫……\x01",
            "这也是为了最后一天的休假而努力啊！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1854")

    Jump("loc_21BB")

    label("loc_1859")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1975")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1926")

    #C0060
    ChrTalk(
        0xFE,
        (
            "彩虹剧团的\x01",
            "新剧终于公演了……\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xFE,
        (
            "我买到的票是\x01",
            "纪念庆典最后一天的。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xFE,
        (
            "所以，在我亲眼欣赏过之前，\x01",
            "我决定不跟任何人说话。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xFE,
        (
            "要是一不小心知道了剧情，\x01",
            "魅力不就减半了嘛。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1970")

    label("loc_1926")

    OP_63(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0064
    ChrTalk(
        0xFE,
        (
            "好啦，不要再和我说话了！\x01",
            "严禁透露剧情哦！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1970")

    Jump("loc_21BB")

    label("loc_1975")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_1B01")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A85")

    #C0065
    ChrTalk(
        0xFE,
        (
            "（紧张）……\x01",
            "啊啊，我现在就开始心跳加快啦……\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xFE,
        (
            "马上就要到纪念庆典了……\x01",
            "到时就能看到伊莉娅小姐炫目的身影了……！\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xFE,
        (
            "我今年也能看到舞台上的\x01",
            "伊莉娅小姐……⊥⊥⊥\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xFE,
        (
            "…………哎呀，有什么事吗？\x01",
            "如果有事的话，\x01",
            "可以和我——管理员萨米说。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1AFC")

    label("loc_1A85")


    #C0069
    ChrTalk(
        0xFE,
        (
            "说起来，去三楼的那些人，\x01",
            "现在不知道走了没有。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xFE,
        (
            "三楼的那位住户今天也出门了。\x01",
            "她总是出门，\x01",
            "我都没和她见过面呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AFC")

    Jump("loc_21BB")

    label("loc_1B01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1C34")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BC8")

    #C0071
    ChrTalk(
        0xFE,
        (
            "从早上起，就有客人\x01",
            "来找住在三楼的住户。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xFE,
        (
            "……但是，感觉有点奇怪呢。\x01",
            "那些人散发出一种居高临下的气场，\x01",
            "连我这个管理员都不让靠近那个房间。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xFE,
        (
            "莫非那些人\x01",
            "是警察吗？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1C2F")

    label("loc_1BC8")


    #C0074
    ChrTalk(
        0xFE,
        (
            "……其实，我之前\x01",
            "就觉得三楼的住户\x01",
            "有点怪怪的。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xFE,
        (
            "因为她白天总是不在，\x01",
            "我连一次也没有见过她呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C2F")

    Jump("loc_21BB")

    label("loc_1C34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_1D5A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CF2")

    #C0076
    ChrTalk(
        0xFE,
        "三楼的住户今天也出门了。\x02",
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xFE,
        (
            "算了，也好……\x01",
            "反正我明天就能进去打扫了。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xFE,
        (
            "三楼的住户让我\x01",
            "每个月进去打扫房间一次。\x01",
            "这可是只有在高级公寓才能享受到的待遇哟。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1D55")

    label("loc_1CF2")


    #C0079
    ChrTalk(
        0xFE,
        (
            "我不太了解\x01",
            "住在三楼的人……\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xFE,
        (
            "不过可以肯定\x01",
            "是个年轻女性。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xFE,
        (
            "因为她总是\x01",
            "把内衣晾出来嘛。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D55")

    Jump("loc_21BB")

    label("loc_1D5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1E23")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DDD")

    #C0082
    ChrTalk(
        0xFE,
        (
            "好不容易买到了\x01",
            "彩虹剧团下个月的票。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xFE,
        "虽然只是Ｂ等座位！\x02",
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xFE,
        (
            "人也太多了！\x01",
            "我好不容易才抢到的～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1E1E")

    label("loc_1DDD")


    #C0085
    ChrTalk(
        0xFE,
        (
            "不过，这样就能见到伊莉娅小姐了～\x01",
            "呵呵，我都已经等不及了～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E1E")

    Jump("loc_21BB")

    label("loc_1E23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_1E76")

    #C0086
    ChrTalk(
        0xFE,
        (
            "住在三楼的人\x01",
            "今天也是一大早就出门了。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0xFE,
        "她到底是什么来头呢～\x02",
    )

    CloseMessageWindow()
    Jump("loc_21BB")

    label("loc_1E76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_1F69")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F26")

    #C0088
    ChrTalk(
        0xFE,
        (
            "我很在意垃圾处理工作的，\x01",
            "不做好分类可不行啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xFE,
        "不过……市里的垃圾回收还真是很随便呢。\x02",
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0xFE,
        (
            "经常把分类好的垃圾\x01",
            "混在一起收走。\x01",
            "真是气死我了！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1F64")

    label("loc_1F26")


    #C0091
    ChrTalk(
        0xFE,
        "我对垃圾分类很在意的。\x02",
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0xFE,
        "你们也要多注意垃圾的分类哟。\x02",
    )

    CloseMessageWindow()

    label("loc_1F64")

    Jump("loc_21BB")

    label("loc_1F69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_2061")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FFE")

    #C0093
    ChrTalk(
        0xFE,
        "喂喂，听说了吗？\x02",
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xFE,
        (
            "彩虹剧团新剧的门票\x01",
            "马上就要发售了。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xFE,
        (
            "我期待已久的伊莉娅小姐的英姿……⊥\x01",
            "啊，绝对要买到啊！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_205C")

    label("loc_1FFE")


    #C0096
    ChrTalk(
        0xFE,
        (
            "马上就要发售彩虹剧团\x01",
            "新剧的门票了。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0xFE,
        (
            "为了与伊莉娅小姐相见，\x01",
            "就算熬夜排队也要购买～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_205C")

    Jump("loc_21BB")

    label("loc_2061")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_214B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_210F")

    #C0098
    ChrTalk(
        0xFE,
        "住在三楼的人总是不在家。\x02",
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xFE,
        (
            "好像每天一大早就出去工作，\x01",
            "直到很晚才会回来……\x01",
            "连我也一次都没见过她呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xFE,
        (
            "不过她倒是每个月\x01",
            "都会按时交房租。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2146")

    label("loc_210F")


    #C0101
    ChrTalk(
        0xFE,
        (
            "住在三楼的人总是不在家。\x01",
            "连我也一次都没见过她呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2146")

    Jump("loc_21BB")

    label("loc_214B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_21BB")

    #C0102
    ChrTalk(
        0xFE,
        (
            "呀，您好。\x01",
            "我是这里的管理员萨米。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xFE,
        (
            "请问您要找哪位？\x01",
            "卢威克先生住在一楼，\x01",
            "金德尔先生则在二楼。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21BB")

    TalkEnd(0xFE)
    Return()

    # Function_8_B4F end

    def Function_9_21BF(): pass

    label("Function_9_21BF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_21D0")
    Jump("loc_22DE")

    label("loc_21D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_21DE")
    Jump("loc_22DE")

    label("loc_21DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_21EC")
    Jump("loc_22DE")

    label("loc_21EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_21FA")
    Jump("loc_22DE")

    label("loc_21FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_2208")
    Jump("loc_22DE")

    label("loc_2208")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2216")
    Jump("loc_22DE")

    label("loc_2216")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_225D")

    #C0104
    ChrTalk(
        0xFE,
        "……真是太精彩了。\x02",
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xFE,
        (
            "今年的游行\x01",
            "实在是值得称赞。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22DE")

    label("loc_225D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_22DE")

    #C0106
    ChrTalk(
        0xFE,
        (
            "手头的工作已经都做完了，\x01",
            "我正要和妻子一起去看游行。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xFE,
        (
            "这可是为了克洛斯贝尔而举办的庆典。\x01",
            "我们也得玩得开心些啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22DE")

    TalkEnd(0xFE)
    Return()

    # Function_9_21BF end

    def Function_10_22E2(): pass

    label("Function_10_22E2")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2376")
    Jump("loc_23C0")

    label("loc_2376")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2396")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_23C0")

    label("loc_2396")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_23B6")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_23C0")

    label("loc_23B6")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_23C0")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x3)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2794")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x5)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2703")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2465")

    #C0108
    ChrTalk(
        0x101,
        (
            "#0001F（好，开始询问线索吧。）\x02\x03",

            "#0000F不好意思，\x01",
            "能占用您一点时间吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2465")

    SetScenarioFlags(0x1, 2)
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0109
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德等人就跟踪狂一事\x01",
            "向对方进行了询问。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()

    #C0110
    ChrTalk(
        0xFE,
        (
            "跟踪狂吗……\x01",
            "我听到过一些传言。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0xFE,
        (
            "我平时总待在家里，\x01",
            "也没亲眼见过，\x01",
            "但是听到过可疑的声音。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0xFE,
        (
            "就是从楼上传来\x01",
            "一种很奇怪的声音。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xFE,
        (
            "我记得住在三楼的人，\x01",
            "白天应该是不在家的。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x101,
        "#0000F那是什么时候的事呢？\x02",
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0xFE,
        "大概是纪念庆典刚开始的时候吧。\x02",
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0xFE,
        "也就这两三天的事。\x02",
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x102,
        (
            "#0108F（潜入伊莉娅小姐的房间，\x01",
            "  到底做了些什么呢？）\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x101,
        (
            "#0001F（……是啊。\x01",
            "  房间里也没有任何\x01",
            "  被人弄乱的痕迹……）\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x1D, 0x1, 0x5)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x5)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x6)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x7)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_26FE")

    #C0119
    ChrTalk(
        0x101,
        (
            "#0000F好，调查就到此结束吧。\x02\x03",

            "先回伊莉娅小姐的房间，\x01",
            "整理一下目前的情报好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x104,
        "#0300F好的，差不多也该拟定对策了！！\x02",
    )

    CloseMessageWindow()
    ModifyEventFlags(1, 0, 0x80)
    OP_29(0x1D, 0x1, 0x9)

    label("loc_26FE")

    Jump("loc_278F")

    label("loc_2703")


    #C0121
    ChrTalk(
        0xFE,
        (
            "从楼上传来了可疑的声音，\x01",
            "也就这两三天的事吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0xFE,
        (
            "我还以为楼上的人\x01",
            "在纪念庆典的时候\x01",
            "没出门呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0xFE,
        (
            "难道……那就是\x01",
            "传闻中的跟踪狂吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_278F")

    Jump("loc_34C2")

    label("loc_2794")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_281F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27F1")

    #C0124
    ChrTalk(
        0xFE,
        "……克洛斯贝尔的混蛋议员们……\x02",
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0xFE,
        "真不像话，绝对不能原谅！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_281A")

    label("loc_27F1")


    #C0126
    ChrTalk(
        0xFE,
        (
            "应该把这些无能的议员\x01",
            "全给炒了鱿鱼！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_281A")

    Jump("loc_34C2")

    label("loc_281F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_28B6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2891")

    #C0127
    ChrTalk(
        0xFE,
        "混账，竟然说设计得太自我了……？\x02",
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0xFE,
        (
            "他们为什么就是不懂\x01",
            "其中所蕴含的艺术性……！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_28B1")

    label("loc_2891")


    #C0129
    ChrTalk(
        0xFE,
        "帝国派的那群混蛋议员……！\x02",
    )

    CloseMessageWindow()

    label("loc_28B1")

    Jump("loc_34C2")

    label("loc_28B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_29BB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_295A")

    #C0130
    ChrTalk(
        0xFE,
        (
            "建造新市政厅大楼的预算\x01",
            "目前已经冻结了。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xFE,
        (
            "……议员们为了工程发包的问题，\x01",
            "彼此争论不休……\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xFE,
        (
            "要是今年能重新\x01",
            "开始建造就好了……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_29B6")

    label("loc_295A")


    #C0133
    ChrTalk(
        0xFE,
        (
            "我对那栋大楼\x01",
            "有着自己的坚持。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xFE,
        (
            "今天准备审议这项工程的预算……\x01",
            "连我都紧张起来了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29B6")

    Jump("loc_34C2")

    label("loc_29BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2AA1")
    SetChrSubChip(0xFE, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A2C")

    #C0135
    ChrTalk(
        0xFE,
        (
            "能在市长选举之前\x01",
            "盖完这栋建筑吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xFE,
        (
            "最近的客户\x01",
            "总是提出无理的要求啊……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2A9C")

    label("loc_2A2C")


    #C0137
    ChrTalk(
        0xFE,
        (
            "四个月之后的市长选举期间\x01",
            "确实是举行落成典礼的最佳时期……\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xFE,
        (
            "但工期实在是赶不及啊，\x01",
            "必须要去提提意见……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A9C")

    Jump("loc_34C2")

    label("loc_2AA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_2B97")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B43")

    #C0139
    ChrTalk(
        0xFE,
        (
            "从纪念庆典开始，\x01",
            "工作就接二连三地涌来……\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xFE,
        (
            "看到自己设计的大楼正式动工，\x01",
            "虽然感到很开心，\x01",
            "但这么忙下去的话，我也会吃不消啊……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2B92")

    label("loc_2B43")


    #C0141
    ChrTalk(
        0xFE,
        "我是绝对不会妥协的。\x02",
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xFE,
        (
            "很抱歉……我的工作已经排满了，\x01",
            "不再继续接单了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B92")

    Jump("loc_34C2")

    label("loc_2B97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2C53")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C1F")

    #C0143
    ChrTalk(
        0xFE,
        (
            "唉呀，请不要\x01",
            "妨碍我啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0xFE,
        (
            "我今天打算把剩下的工作\x01",
            "都解决掉。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0xFE,
        (
            "……要是动作够快，\x01",
            "傍晚就会有空了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2C4E")

    label("loc_2C1F")


    #C0146
    ChrTalk(
        0xFE,
        (
            "……赶紧把工作解决掉，傍晚\x01",
            "去陪老婆好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C4E")

    Jump("loc_34C2")

    label("loc_2C53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_2CB0")

    #C0147
    ChrTalk(
        0xFE,
        "哎呀，有什么事吗？\x02",
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0xFE,
        (
            "抱歉，我还有设计的工作要做，\x01",
            "很抱歉，没空招待你。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34C2")

    label("loc_2CB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_2CBE")
    Jump("loc_34C2")

    label("loc_2CBE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2CCC")
    Jump("loc_34C2")

    label("loc_2CCC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2D23")

    #C0149
    ChrTalk(
        0xFE,
        "工作还没有做完呢。\x02",
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xFE,
        (
            "……虽然对不住老婆，\x01",
            "但我现在真是走不开啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34C2")

    label("loc_2D23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2D73")

    #C0151
    ChrTalk(
        0xFE,
        "怎么搞的，外面好吵啊……\x02",
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xFE,
        "这样的话，我都无法集中精神啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_34C2")

    label("loc_2D73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_2DD3")

    #C0153
    ChrTalk(
        0xFE,
        (
            "好了，就差一点，\x01",
            "就能完成这幢大楼的设计图了……\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0xFE,
        (
            "得尽早拿给\x01",
            "客户过目啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34C2")

    label("loc_2DD3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2E77")

    #C0155
    ChrTalk(
        0xFE,
        (
            "我的祖父和父亲\x01",
            "都是有名的建筑师。\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔的市政厅\x01",
            "就是我祖父设计的。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xFE,
        (
            "说起来，那幢建筑\x01",
            "也已经有六十个年头了……\x01",
            "真是令人感慨万千啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34C2")

    label("loc_2E77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_2F75")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F26")

    #C0158
    ChrTalk(
        0xFE,
        (
            "听说黑手党鲁巴彻的那些家伙\x01",
            "正在强买土地……\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xFE,
        (
            "所谓强买土地，就是指为了得到建筑用地\x01",
            "而强行驱逐居民的违法行为。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0xFE,
        "真是群品行恶劣的家伙啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2F70")

    label("loc_2F26")


    #C0161
    ChrTalk(
        0xFE,
        (
            "听说鲁巴彻的那群人\x01",
            "正在强买土地。\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0xFE,
        (
            "警察们就不能想办法\x01",
            "去管管吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F70")

    Jump("loc_34C2")

    label("loc_2F75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_30B8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_305D")

    #C0163
    ChrTalk(
        0xFE,
        (
            "为了下个月做准备，克洛斯贝尔市里\x01",
            "所有的工地都加快了建设进程，\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xFE,
        (
            "因为下个月将要举办七十周年的创立纪念庆典……\x01",
            "克洛斯贝尔市将受到世界各国的瞩目。\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0xFE,
        (
            "身为大楼的设计者，\x01",
            "这可是最好的自我展示机会呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_30B3")

    label("loc_305D")


    #C0166
    ChrTalk(
        0xFE,
        (
            "下个月将会有很多大楼的\x01",
            "落成典礼吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0xFE,
        (
            "感觉这里简直成了\x01",
            "世界顶级的繁荣之都啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30B3")

    Jump("loc_34C2")

    label("loc_30B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_30C6")
    Jump("loc_34C2")

    label("loc_30C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_31E4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3183")

    #C0168
    ChrTalk(
        0xFE,
        (
            "你知道米修拉姆\x01",
            "开了一个主题公园吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0xFE,
        (
            "据说，那个主题公园的主体部分\x01",
            "是由ＩＢＣ的事业部负责的。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0xFE,
        (
            "似乎还采用了\x01",
            "最新的建筑技术……\x01",
            "我也好想去见识一下呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_31DF")

    label("loc_3183")


    #C0171
    ChrTalk(
        0xFE,
        (
            "我设计过很多酒店，\x01",
            "但还一次都没有去过主题公园。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0xFE,
        (
            "嗯……好想看看\x01",
            "他们的设计作品呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31DF")

    Jump("loc_34C2")

    label("loc_31E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_325E")

    #C0173
    ChrTalk(
        0xFE,
        (
            "呼，专心于设计，\x01",
            "一不小心就熬夜了。\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0xFE,
        (
            "不过这么一来，客人也会满意了吧。\x01",
            "呵呵，好期待明天的说明会啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34C2")

    label("loc_325E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_3378")
    SetChrSubChip(0xFE, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_332A")

    #C0175
    ChrTalk(
        0xFE,
        (
            "不过……那些家伙还真是令人头疼。\x01",
            "竟然完全无视\x01",
            "我的设计图……\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0xFE,
        (
            "让我设计新市政厅大楼的人\x01",
            "不就是他们吗！\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0xFE,
        (
            "我要去抗议……\x01",
            "擅自改变设计式样这种事\x01",
            "……我绝对不认可！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3373")

    label("loc_332A")


    #C0178
    ChrTalk(
        0xFE,
        (
            "混蛋，这种破东西\x01",
            "叫什么改善方案啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0xFE,
        "太差劲了，实在是太差劲了！\x02",
    )

    CloseMessageWindow()

    label("loc_3373")

    Jump("loc_34C2")

    label("loc_3378")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_34C2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3458")

    #C0180
    ChrTalk(
        0xFE,
        (
            "正在建造的新市政厅大楼\x01",
            "是个高达四十层的超高建筑。\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0xFE,
        (
            "那可是一幢充满了\x01",
            "前所未有的崭新理念，\x01",
            "走在时代最前端的建筑物。\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xFE,
        (
            "我负责设计大楼的\x01",
            "外观和办公区。\x01",
            "呵呵，真想赶快看到它完成时的样子啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_34C2")

    label("loc_3458")


    #C0183
    ChrTalk(
        0xFE,
        (
            "新建的市政厅大楼是高达四十层的\x01",
            "超高层建筑物。\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0xFE,
        (
            "设计它可真是一件大工程啊……\x01",
            "好期待它建成的那天。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34C2")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_10_22E2 end

    def Function_11_34CA(): pass

    label("Function_11_34CA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x3)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_37F3")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x6)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37A5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_354D")

    #C0185
    ChrTalk(
        0x101,
        (
            "#0001F（好，开始询问线索吧。）\x02\x03",

            "#0000F打扰一下，\x01",
            "能占用您一点时间吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_354D")

    SetScenarioFlags(0x1, 2)
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0186
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德等人就跟踪狂一事\x01",
            "向对方进行了询问。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()

    #C0187
    ChrTalk(
        0xFE,
        (
            "跟踪狂吗？\x01",
            "真可怕啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0xFE,
        (
            "不过我没有见过呢。\x01",
            "我经常出门去买东西，\x01",
            "但是一次也没见过……\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0x103,
        (
            "#0200F买东西……\x01",
            "时间一般是上午或晚上吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0xFE,
        (
            "嗯，是的。\x01",
            "我基本都是在固定的时间出门。\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0x102,
        "#0105F（正好是出入人员比较多的时间段呢。）\x02",
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0x101,
        (
            "#0001F（嗯，看起来，跟踪狂\x01",
            "  好像不会在那种时间出现……）\x02\x03",

            "（似乎是个很小心谨慎的家伙啊。）\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x1D, 0x1, 0x6)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x5)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x6)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x7)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_37A0")

    #C0193
    ChrTalk(
        0x101,
        (
            "#0000F好，调查就到此结束吧。\x02\x03",

            "先回伊莉娅小姐的房间，\x01",
            "整理一下目前的情报好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0x104,
        "#0300F好的，差不多也该拟定对策了！！\x02",
    )

    CloseMessageWindow()
    ModifyEventFlags(1, 0, 0x80)
    OP_29(0x1D, 0x1, 0x9)

    label("loc_37A0")

    Jump("loc_37EE")

    label("loc_37A5")


    #C0195
    ChrTalk(
        0xFE,
        "跟踪狂可真是吓人啊。\x02",
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0xFE,
        (
            "虽然我在出门买东西的时候\x01",
            "从没有看到过……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37EE")

    Jump("loc_4220")

    label("loc_37F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_3846")

    #C0197
    ChrTalk(
        0xFE,
        "今天给他泡杯红茶好了。\x02",
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0xFE,
        (
            "喝杯红茶，\x01",
            "也许就能稍微放松一点吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4220")

    label("loc_3846")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3932")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38EE")

    #C0199
    ChrTalk(
        0xFE,
        (
            "新市政厅大楼的预算\x01",
            "最后似乎还是没能通过。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0xFE,
        (
            "在议员的听证会上，\x01",
            "被他们批评为\x01",
            "这项工程太过铺张浪费……\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0xFE,
        "我老公为此发了很大的火呢。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_392D")

    label("loc_38EE")


    #C0202
    ChrTalk(
        0xFE,
        (
            "这可真令人困扰啊……\x01",
            "我老公是那种对工作毫不懈怠的类型……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_392D")

    Jump("loc_4220")

    label("loc_3932")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_3940")
    Jump("loc_4220")

    label("loc_3940")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_3989")

    #C0203
    ChrTalk(
        0xFE,
        (
            "最近接到了\x01",
            "很多的设计工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0xFE,
        "整理文件也挺累人呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4220")

    label("loc_3989")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_3A4E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39EE")

    #C0205
    ChrTalk(
        0xFE,
        (
            "我老公最近\x01",
            "工作非常繁忙。\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0xFE,
        (
            "……都不太跟我说话了，\x01",
            "真有点寂寞呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3A49")

    label("loc_39EE")


    #C0207
    ChrTalk(
        0xFE,
        "哎呀，不应该在意这种事情啦。\x02",
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0xFE,
        (
            "为了能让他顺利工作，\x01",
            "我得去给他沏上一杯温热的红茶。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A49")

    Jump("loc_4220")

    label("loc_3A4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_3AA0")

    #C0209
    ChrTalk(
        0xFE,
        (
            "今晚我准备做\x01",
            "一顿丰盛的大餐。\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0xFE,
        (
            "呵呵，不好好\x01",
            "准备可不行呀。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4220")

    label("loc_3AA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_3B36")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3AF1")

    #C0211
    ChrTalk(
        0xFE,
        "矮个子的男孩吗……？\x02",
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0xFE,
        "嗯，我没什么印象呢……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3B31")

    label("loc_3AF1")


    #C0213
    ChrTalk(
        0xFE,
        (
            "我们也去看了\x01",
            "游行……\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0xFE,
        (
            "不好意思，现在\x01",
            "一点印象也没有。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B31")

    Jump("loc_4220")

    label("loc_3B36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_3B83")

    #C0215
    ChrTalk(
        0xFE,
        (
            "呵呵，今年的游行活动\x01",
            "真是太棒了。\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0xFE,
        "留下了美好的回忆。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4220")

    label("loc_3B83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_3C04")
    OP_4B(0x9, 0xFF)
    TurnDirection(0xB, 0x9, 0)

    #C0217
    ChrTalk(
        0x9,
        "咳咳，也该走了。\x02",
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0x9,
        (
            "要是不去看游行的话，\x01",
            "跟客户们的话题也会减少的。\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0xFE,
        (
            "呵呵……\x01",
            "嗯，走吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    Jump("loc_4220")

    label("loc_3C04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3C67")

    #C0220
    ChrTalk(
        0xFE,
        "我老公就是这种一心工作的人。\x02",
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0xFE,
        (
            "我倒是不在乎啦，\x01",
            "只是希望他偶尔也能休息一下。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4220")

    label("loc_3C67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_3CBE")

    #C0222
    ChrTalk(
        0xFE,
        (
            "哎呀，欢迎光临。\x01",
            "这里是金德尔设计事务所。\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0xFE,
        "今天我们也照常营业。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4220")

    label("loc_3CBE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_3CCC")
    Jump("loc_4220")

    label("loc_3CCC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3DCD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D7D")

    #C0224
    ChrTalk(
        0xFE,
        (
            "ＩＢＣ集团的建筑公司\x01",
            "是我们这里的熟客。\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0xFE,
        (
            "工地的负责人\x01",
            "来拜访过很多次，\x01",
            "跟我老公的关系不错呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0xFE,
        (
            "不过每次都会喝酒，\x01",
            "真让人担心他的身体啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3DC8")

    label("loc_3D7D")


    #C0227
    ChrTalk(
        0xFE,
        (
            "建筑公司的人总是\x01",
            "拉我老公一起喝酒。\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0xFE,
        "希望他能多注意自己的身体呢。\x02",
    )

    CloseMessageWindow()

    label("loc_3DC8")

    Jump("loc_4220")

    label("loc_3DCD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_3E23")

    #C0229
    ChrTalk(
        0xFE,
        (
            "今天打算做老公\x01",
            "最爱吃的炖牛肉。\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0xFE,
        (
            "呵呵，我得赶快去\x01",
            "准备材料了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4220")

    label("loc_3E23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_3E8A")

    #C0231
    ChrTalk(
        0xFE,
        (
            "彩虹剧团的伊莉娅小姐\x01",
            "非常有人气呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0xFE,
        (
            "因为萨米小姐\x01",
            "总是说起她，\x01",
            "连我都记下来了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4220")

    label("loc_3E8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_3F65")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F2F")

    #C0233
    ChrTalk(
        0xFE,
        (
            "得在老公回来之前\x01",
            "把室内打扫干净。\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0xFE,
        (
            "老公他……现在应该\x01",
            "正在中央广场的餐厅里\x01",
            "谈公事吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0xFE,
        (
            "呵呵……这个死脑筋，\x01",
            "工作倒还挺忙的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3F60")

    label("loc_3F2F")


    #C0236
    ChrTalk(
        0xFE,
        (
            "好啦，我得趁着他不在家，\x01",
            "赶紧把房间收拾好。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F60")

    Jump("loc_4220")

    label("loc_3F65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_3F73")
    Jump("loc_4220")

    label("loc_3F73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_4048")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4008")

    #C0237
    ChrTalk(
        0xFE,
        (
            "我老公又熬了一夜呢。\x01",
            "一旦开始设计新建筑，\x01",
            "就总是这样子……\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0xFE,
        (
            "呵呵，真拿他没办法啊。\x01",
            "没办法，我给他\x01",
            "泡杯热红茶吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4043")

    label("loc_4008")


    #C0239
    ChrTalk(
        0xFE,
        (
            "我老公非常爱喝红茶呢。\x01",
            "每次熬夜之后，我都会泡给他喝。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4043")

    Jump("loc_4220")

    label("loc_4048")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_4121")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_40D0")

    #C0240
    ChrTalk(
        0xFE,
        (
            "我老公只要一集中精神，\x01",
            "就完全注意不到周围的事了。\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0xFE,
        (
            "有时候还会\x01",
            "突然大吼出声……\x01",
            "请千万不要放在心上。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_411C")

    label("loc_40D0")


    #C0242
    ChrTalk(
        0xFE,
        (
            "我老公只要一集中精神，\x01",
            "就完全注意不到周围的事了。\x01",
            "请千万不要放在心上。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_411C")

    Jump("loc_4220")

    label("loc_4121")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_4220")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_41D8")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0243
    ChrTalk(
        0xFE,
        (
            "啊……不好意思。\x01",
            "我正在做饭呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0xFE,
        (
            "这里是金德尔设计事务所。\x01",
            "如果是工作方面的事情，\x01",
            "就请跟我老公谈吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0xFE,
        "他现在好像正好有空。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4220")

    label("loc_41D8")


    #C0246
    ChrTalk(
        0xFE,
        (
            "这里是金德尔设计事务所。\x01",
            "如果是工作方面的事情，\x01",
            "就请跟我老公谈吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4220")

    TalkEnd(0xFE)
    Return()

    # Function_11_34CA end

    def Function_12_4224(): pass

    label("Function_12_4224")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x3)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_480B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x7)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4797")
    OP_4B(0xC, 0xFF)
    OP_4B(0xE, 0xFF)

    #C0247
    ChrTalk(
        0xC,
        (
            "哎呀呀，还想去外面\x01",
            "吃午饭呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0xE,
        (
            "但早上都已经准备好了，\x01",
            "这也没办法啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0xE,
        "你就别抱怨啦。\x02",
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0x101,
        (
            "#0003F（感觉气氛不太妙啊……）\x02\x03",

            "#0000F打、打扰一下。\x01",
            "能占用您一点时间吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    TurnDirection(0xC, 0x0, 400)
    TurnDirection(0xE, 0x0, 400)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0251
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德等人就跟踪狂一事\x01",
            "向对方进行了询问。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()

    #C0252
    ChrTalk(
        0xC,
        "哦？跟踪狂吗？\x02",
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0xC,
        (
            "哎呀，这可真吓人啊。\x01",
            "这种事情应该赶快通知警察啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0xE,
        (
            "不过，也许还是找游击士更好吧？\x01",
            "因为警察很难请得动嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x101,
        (
            "#0000F呃，这个……\x01",
            "请问您有什么印象吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0xE,
        "嗯，我想想……\x02",
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0xE,
        (
            "我总是坐在玄关的\x01",
            "沙发上休息。\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0xE,
        (
            "但从没见过\x01",
            "什么可疑的人呢，\x01",
            "会不会是你们搞错了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_458D")
    OP_63(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1200)

    #C0259
    ChrTalk(
        0x104,
        "#0305F……………………！？\x02",
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0x101,
        (
            "#0003F（从没见过犯人\x01",
            "  从正门进来吗……）\x02\x03",

            "（这到底是怎么回事……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_46C5")

    label("loc_458D")

    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    #C0261
    ChrTalk(
        0x104,
        "#0305F……竟然会这样………！\x02",
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0x102,
        (
            "#0103F（从没见过犯人\x01",
            "  从正门进来……）\x02\x03",

            "（也就是说，果然是从\x01",
            "  那条路线潜入的吗？）\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0x103,
        (
            "#0200F（是指后门吧。\x01",
            "  可能性似乎很高。）\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0x101,
        (
            "#0001F（……稍后制定对策的时候，\x01",
            "  重点注意一下这里吧。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xBD, 4)

    label("loc_46C5")

    OP_29(0x1D, 0x1, 0x7)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x5)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x6)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x7)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4780")

    #C0265
    ChrTalk(
        0x101,
        (
            "#0000F好，调查就到此结束吧。\x02\x03",

            "先回伊莉娅小姐的房间，\x01",
            "整理一下目前的情报好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0x104,
        "#0300F好的，差不多也该拟定对策了！！\x02",
    )

    CloseMessageWindow()
    ModifyEventFlags(1, 0, 0x80)
    OP_29(0x1D, 0x1, 0x9)

    label("loc_4780")

    OP_4C(0xC, 0xFF)
    OP_4C(0xE, 0xFF)
    ClearChrFlags(0xC, 0x10)
    ClearChrFlags(0xE, 0x10)
    Jump("loc_4806")

    label("loc_4797")


    #C0267
    ChrTalk(
        0xFE,
        "呵呵，跟踪狂真是很可怕啊。\x02",
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0xFE,
        "赶快把这件事通报给警察吧。\x02",
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0x101,
        (
            "#0001F（这个人好像\x01",
            "  没有任何线索呢……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4806")

    Jump("loc_516C")

    label("loc_480B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_4819")
    Jump("loc_516C")

    label("loc_4819")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_48DE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48A8")

    #C0270
    ChrTalk(
        0xFE,
        (
            "我在后巷的一家古董店里\x01",
            "找到了好东西呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0xFE,
        "我们的结婚纪念日马上就要到了。\x02",
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0xFE,
        (
            "呵呵，\x01",
            "我老伴应该会很高兴吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_48D9")

    label("loc_48A8")


    #C0273
    ChrTalk(
        0xFE,
        (
            "我老伴的性格很刁蛮，\x01",
            "要讨她欢心可不容易了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_48D9")

    Jump("loc_516C")

    label("loc_48DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_49D3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_49A5")

    #C0274
    ChrTalk(
        0xFE,
        (
            "能过上现在这种安稳的生活，\x01",
            "全靠我年轻时努力工作啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0xFE,
        (
            "多亏了议员的\x01",
            "退休金给得很多啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0xFE,
        (
            "但是我老伴可固执了。\x01",
            "就算我说要买下那个当做礼物，\x01",
            "她大概也不会同意吧……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_49CE")

    label("loc_49A5")


    #C0277
    ChrTalk(
        0xFE,
        (
            "唉，真是头疼啊。\x01",
            "我老伴可固执了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_49CE")

    Jump("loc_516C")

    label("loc_49D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_4A95")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A61")

    #C0278
    ChrTalk(
        0xFE,
        (
            "我老伴不让我重新\x01",
            "装修房子。\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0xFE,
        (
            "还不都是因为她\x01",
            "觉得麻烦，\x01",
            "所以我才代为负责的吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0xFE,
        "真是个任性的家伙啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4A90")

    label("loc_4A61")


    #C0281
    ChrTalk(
        0xFE,
        (
            "哼，我家那位不但人很懒，\x01",
            "而且还很任性呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A90")

    Jump("loc_516C")

    label("loc_4A95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_4B75")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B14")
    TurnDirection(0xFE, 0x153, 0)

    #C0282
    ChrTalk(
        0xFE,
        "哎呀，真是个可爱的小姑娘啊。\x02",
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0xFE,
        (
            "刚搬到西街的吗？\x01",
            "算啦，总而言之，随时都可以过来玩哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4B70")

    label("loc_4B14")


    #C0284
    ChrTalk(
        0xFE,
        (
            "我又改换了一下\x01",
            "家里的装饰。\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0xFE,
        (
            "嗯，统一换成了明亮的颜色，\x01",
            "和纪念庆典的气氛很相配吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B70")

    Jump("loc_516C")

    label("loc_4B75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_4B83")
    Jump("loc_516C")

    label("loc_4B83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_4B91")
    Jump("loc_516C")

    label("loc_4B91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_4B9F")
    Jump("loc_516C")

    label("loc_4B9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_4BAD")
    Jump("loc_516C")

    label("loc_4BAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_4BBB")
    Jump("loc_516C")

    label("loc_4BBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_4BC9")
    Jump("loc_516C")

    label("loc_4BC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_4C48")

    #C0286
    ChrTalk(
        0xFE,
        (
            "好了，房间也收拾得差不多了……\x01",
            "泡杯茶好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0xFE,
        (
            "我老伴整天沉迷于自己的爱好。\x01",
            "这些事情也只能\x01",
            "由我来负责了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_516C")

    label("loc_4C48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_4CA7")

    #C0288
    ChrTalk(
        0xFE,
        (
            "打扫壁橱的时候，\x01",
            "东西全都掉下来了……\x02",
        )
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0xFE,
        "哎呀呀，过后收拾起来会很辛苦呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_516C")

    label("loc_4CA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_4D6E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D23")

    #C0290
    ChrTalk(
        0xFE,
        (
            "纪念庆典就快到了，\x01",
            "每天心情都很好呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0xFE,
        (
            "这气氛让我也坐不住了，\x01",
            "去买张新地毯\x01",
            "铺上好了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4D69")

    label("loc_4D23")


    #C0292
    ChrTalk(
        0xFE,
        (
            "纪念庆典一来，\x01",
            "我也想换个心情呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0xFE,
        (
            "打扫打扫房间\x01",
            "也挺不错的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D69")

    Jump("loc_516C")

    label("loc_4D6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_4E7F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E06")

    #C0294
    ChrTalk(
        0xFE,
        (
            "我在调整家具摆放时，\x01",
            "发现炉子上生了锈。\x02",
        )
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0xFE,
        (
            "所以就按照原来的尺寸，\x01",
            "换了个新炉子。\x02",
        )
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0xFE,
        (
            "正好有大小合适的，\x01",
            "真是太好了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4E7A")

    label("loc_4E06")


    #C0297
    ChrTalk(
        0xFE,
        (
            "而且……我听店员说，\x01",
            "这种新型炉子的火力要比以前的强很多。\x02",
        )
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0xFE,
        (
            "而且也没有令人心烦的锈迹了。\x01",
            "呵呵，真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E7A")

    Jump("loc_516C")

    label("loc_4E7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_4F2B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4EED")

    #C0299
    ChrTalk(
        0xFE,
        (
            "桌子现在没有摆在\x01",
            "屋子的正中间。\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0xFE,
        (
            "这可不行……\x01",
            "我得重新再\x01",
            "好好量一下尺寸。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4F26")

    label("loc_4EED")


    #C0301
    ChrTalk(
        0xFE,
        (
            "桌子现在的位置让我不太舒服。\x01",
            "我得把它稍微移动一下。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F26")

    Jump("loc_516C")

    label("loc_4F2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_4FF2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4FAA")

    #C0302
    ChrTalk(
        0xFE,
        "噢噢，今天早上是个大晴天。\x02",
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0xFE,
        (
            "下次自治州议会上的讨论，\x01",
            "若也能像这天空一样爽朗，\x01",
            "该有多好啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4FED")

    label("loc_4FAA")


    #C0304
    ChrTalk(
        0xFE,
        "好了，该给植物浇浇水了。\x02",
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0xFE,
        (
            "我老伴对这些东西\x01",
            "一点也不用心。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4FED")

    Jump("loc_516C")

    label("loc_4FF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_50C0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5076")

    #C0306
    ChrTalk(
        0xFE,
        (
            "老伴从早到晚，\x01",
            "一直在做她喜欢的手工。\x01",
            "一点也不干家务。\x02",
        )
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0xFE,
        (
            "哎呀哎呀，这样的老伴\x01",
            "真是让人发愁啊……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_50BB")

    label("loc_5076")


    #C0308
    ChrTalk(
        0xFE,
        (
            "我老伴整天\x01",
            "沉迷于自己的兴趣。\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0xFE,
        "她从以前开始就一直这么任性。\x02",
    )

    CloseMessageWindow()

    label("loc_50BB")

    Jump("loc_516C")

    label("loc_50C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_516C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5126")

    #C0310
    ChrTalk(
        0xFE,
        (
            "嗯，为了转换心情，\x01",
            "我新买了些高级家具。\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0xFE,
        "摆设差不多就这个样子吧。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_516C")

    label("loc_5126")


    #C0312
    ChrTalk(
        0xFE,
        (
            "我刚把屋里的装潢\x01",
            "重新更换了一下。\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0xFE,
        (
            "一起来喝杯茶吗？\x01",
            "呵呵……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_516C")

    TalkEnd(0xFE)
    Return()

    # Function_12_4224 end

    def Function_13_5170(): pass

    label("Function_13_5170")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5204")
    Jump("loc_524E")

    label("loc_5204")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5224")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_524E")

    label("loc_5224")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5244")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_524E")

    label("loc_5244")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_524E")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_52F5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_528E")
    Call(0, 14)
    Jump("loc_52F5")

    label("loc_528E")


    #C0314
    ChrTalk(
        0xFE,
        (
            "能像这样过上\x01",
            "宽裕的日子，\x01",
            "全都是因为有我的退休金……\x02",
        )
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0xFE,
        (
            "老伴啊，难道你\x01",
            "已经忘记这一点了吗……？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_52F5")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_13_5170 end

    def Function_14_52FD(): pass

    label("Function_14_52FD")

    SetChrSubChip(0xD, 0x0)
    SetChrSubChip(0xF, 0x0)

    #C0316
    ChrTalk(
        0xF,
        (
            "……我说你啊，\x01",
            "你知道该怎么泡红茶吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0xD,
        (
            "不就是把热水浇到茶叶上吗？\x01",
            "你看，这不是泡好了吗。\x02",
        )
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0xF,
        (
            "太难喝了，\x01",
            "这种东西怎么能喝得下去啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0xD,
        "…………………………………\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    SetScenarioFlags(0x0, 4)
    Return()

    # Function_14_52FD end

    def Function_15_53B9(): pass

    label("Function_15_53B9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x3)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5559")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x7)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_53F0")
    Call(0, 12)
    Return()

    label("loc_53F0")


    #C0320
    ChrTalk(
        0xFE,
        (
            "我总是坐在玄关的\x01",
            "沙发上休息。\x02",
        )
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0xFE,
        (
            "但从没见过什么\x01",
            "可疑的人呢，\x01",
            "会不会是你们搞错了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x8)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBD, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5554")

    #C0322
    ChrTalk(
        0x104,
        "#0303F（……原来如此，真有一套啊。）\x02",
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0x102,
        (
            "#0100F（从没见过跟踪狂\x01",
            "  从玄关进来……）\x02\x03",

            "（也就是说，果然是从\x01",
            "  那条路线进来的吗？）\x02",
        )
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0x103,
        (
            "#0200F（是指后门吧。\x01",
            "  很有可能呢。）\x02",
        )
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0x101,
        (
            "#0001F（…………稍后制定对策的时候，\x01",
            "  重点注意一下这里吧。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xBD, 4)

    label("loc_5554")

    Jump("loc_567C")

    label("loc_5559")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_5665")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5615")

    #C0326
    ChrTalk(
        0xFE,
        (
            "我老伴直到五年前，\x01",
            "都是个议员。\x02",
        )
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0xFE,
        (
            "虽然他只是个呆呆地\x01",
            "听着其他议员发表意见，\x01",
            "自己没什么主见的议员而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0xFE,
        (
            "不过呢……\x01",
            "退休金倒是不少，\x01",
            "这点值得表扬呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5660")

    label("loc_5615")


    #C0329
    ChrTalk(
        0xFE,
        (
            "我老伴也就是个凑数的议员，\x01",
            "好在退休金挺多。\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0xFE,
        "也就这点还值得表扬。\x02",
    )

    CloseMessageWindow()

    label("loc_5660")

    Jump("loc_567C")

    label("loc_5665")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_5673")
    Jump("loc_567C")

    label("loc_5673")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_567C")

    label("loc_567C")

    TalkEnd(0xFE)
    Return()

    # Function_15_53B9 end

    def Function_16_5680(): pass

    label("Function_16_5680")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5714")
    Jump("loc_575E")

    label("loc_5714")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5734")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_575E")

    label("loc_5734")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5754")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_575E")

    label("loc_5754")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_575E")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_5844")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_580A")

    #C0331
    ChrTalk(
        0xFE,
        (
            "我老伴\x01",
            "买了部导力车……\x02",
        )
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0xFE,
        "又瞒着我乱花钱……！\x02",
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0xFE,
        (
            "真是自作主张啊，\x01",
            "我都不知道该说他什么好了……！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_583F")

    label("loc_580A")


    #C0334
    ChrTalk(
        0xFE,
        (
            "我都不知道要怎么说他\x01",
            "那铺张浪费的坏习惯了……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_583F")

    Jump("loc_6214")

    label("loc_5844")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_5954")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_58F9")

    #C0335
    ChrTalk(
        0xFE,
        (
            "我老伴为了庆祝结婚纪念日，\x01",
            "送给我一个吊坠呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0xFE,
        "…………………………………\x02",
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0xFE,
        (
            "呼，那个人也是\x01",
            "有些优点的啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0xFE,
        "再怎么说，也是我看中的男人啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_594F")

    label("loc_58F9")


    #C0339
    ChrTalk(
        0xFE,
        (
            "当年啊，\x01",
            "他还真是个不错的好青年呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0xFE,
        (
            "呵呵，现在似乎也能\x01",
            "看到一点当年的影子。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_594F")

    Jump("loc_6214")

    label("loc_5954")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_59F4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_59C0")

    #C0341
    ChrTalk(
        0xFE,
        (
            "我老伴又想给家里\x01",
            "添置大件呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0xFE,
        (
            "真是的……\x01",
            "这次又准备\x01",
            "买个吊灯回来吗……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_59EF")

    label("loc_59C0")


    #C0343
    ChrTalk(
        0xFE,
        (
            "我真受不了他那\x01",
            "喜欢装饰房间的无聊癖好啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_59EF")

    Jump("loc_6214")

    label("loc_59F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_5AE4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5AA6")

    #C0344
    ChrTalk(
        0xFE,
        (
            "自治州议会的会期\x01",
            "似乎又要拖延下去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0xFE,
        (
            "……跟我老伴还是议员的时候相比，\x01",
            "真是没有一点变化啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0xFE,
        (
            "就会给人们添麻烦，\x01",
            "总是发表一些任性的主张。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5ADF")

    label("loc_5AA6")


    #C0347
    ChrTalk(
        0xFE,
        (
            "我老伴现在会是这种性格，\x01",
            "肯定也是因为议员当太久了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5ADF")

    Jump("loc_6214")

    label("loc_5AE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_5BE7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B94")

    #C0348
    ChrTalk(
        0xFE,
        (
            "在克洛斯贝尔的上流社会里，\x01",
            "有不少人都爱好手工。\x02",
        )
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0xFE,
        (
            "麦克道尔市长的夫人\x01",
            "生前也十分擅长做手工呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0xFE,
        (
            "我会有这种爱好，\x01",
            "可能也是受了她的影响吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5BE2")

    label("loc_5B94")


    #C0351
    ChrTalk(
        0xFE,
        (
            "麦克道尔市长的夫人\x01",
            "生前特别擅长做手工。\x02",
        )
    )

    CloseMessageWindow()

    #C0352
    ChrTalk(
        0xFE,
        (
            "不过她已经\x01",
            "过世很长时间了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5BE2")

    Jump("loc_6214")

    label("loc_5BE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_5BF5")
    Jump("loc_6214")

    label("loc_5BF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_5C03")
    Jump("loc_6214")

    label("loc_5C03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_5C11")
    Jump("loc_6214")

    label("loc_5C11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_5C1F")
    Jump("loc_6214")

    label("loc_5C1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_5C2D")
    Jump("loc_6214")

    label("loc_5C2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_5C9F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C48")
    Call(0, 14)
    Jump("loc_5C9A")

    label("loc_5C48")


    #C0353
    ChrTalk(
        0xFE,
        (
            "连泡红茶的方法\x01",
            "也搞不太清楚。\x02",
        )
    )

    CloseMessageWindow()

    #C0354
    ChrTalk(
        0xFE,
        (
            "明明都不太会做家务，\x01",
            "还真是很有积极性啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5C9A")

    Jump("loc_6214")

    label("loc_5C9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_5D80")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D2D")

    #C0355
    ChrTalk(
        0xFE,
        (
            "今天早上\x01",
            "有几个男人走进来。\x02",
        )
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0xFE,
        (
            "也不说话，\x01",
            "直接就上了三楼……\x02",
        )
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0xFE,
        (
            "感觉不像是普通人啊，\x01",
            "到底是来干什么的呢？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5D7B")

    label("loc_5D2D")


    #C0358
    ChrTalk(
        0xFE,
        (
            "那些男人啊，\x01",
            "根本就不像是要来\x01",
            "公寓找朋友玩的样子。\x02",
        )
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0xFE,
        "到底是什么人啊？\x02",
    )

    CloseMessageWindow()

    label("loc_5D7B")

    Jump("loc_6214")

    label("loc_5D80")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_5E50")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E16")

    #C0360
    ChrTalk(
        0xFE,
        (
            "我老伴又\x01",
            "做了些多余的事……\x02",
        )
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0xFE,
        (
            "扫除这种事，\x01",
            "只要拜托萨米就好了嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0xFE,
        (
            "哼，就是因为做了不擅长的事，\x01",
            "才会搞成这样。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5E4B")

    label("loc_5E16")


    #C0363
    ChrTalk(
        0xFE,
        (
            "他总是做这些多余的事，\x01",
            "我真不知道该说什么才好。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5E4B")

    Jump("loc_6214")

    label("loc_5E50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_5F3C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5EE1")

    #C0364
    ChrTalk(
        0xFE,
        (
            "我啊，每年在纪念庆典的时候，\x01",
            "都会制作杯垫呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0xFE,
        "到今年也有二十年了。\x02",
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0xFE,
        (
            "没想到能坚持这么久，\x01",
            "真令人感慨啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5F37")

    label("loc_5EE1")


    #C0367
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔到今年\x01",
            "也已经是七十周岁了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0368
    ChrTalk(
        0xFE,
        (
            "年纪是越来越大了啊……\x01",
            "真令人感慨。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5F37")

    Jump("loc_6214")

    label("loc_5F3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_5FA9")

    #C0369
    ChrTalk(
        0xFE,
        (
            "我老伴在导力商店\x01",
            "买了新的导力炉回来。\x02",
        )
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0xFE,
        "又背着我乱花钱……\x02",
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0xFE,
        "就不会干点别的事了吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_6214")

    label("loc_5FA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_602E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_600A")

    #C0372
    ChrTalk(
        0xFE,
        (
            "哎呀呀……\x01",
            "我老伴的坏毛病又发作了。\x02",
        )
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0xFE,
        (
            "这下子\x01",
            "也没法做饭了啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_6029")

    label("loc_600A")


    #C0374
    ChrTalk(
        0xFE,
        (
            "唉，今天也\x01",
            "到外面吃算了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6029")

    Jump("loc_6214")

    label("loc_602E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_603C")
    Jump("loc_6214")

    label("loc_603C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_6130")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_60E3")

    #C0375
    ChrTalk(
        0xFE,
        (
            "这间公寓啊，\x01",
            "可以让管理员\x01",
            "来帮忙打扫房间的。\x02",
        )
    )

    CloseMessageWindow()

    #C0376
    ChrTalk(
        0xFE,
        (
            "我们家也拜托萨米\x01",
            "帮忙打扫房间和洗衣服。\x02",
        )
    )

    CloseMessageWindow()

    #C0377
    ChrTalk(
        0xFE,
        (
            "这么一来，\x01",
            "我就有时间做自己想做的事了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_612B")

    label("loc_60E3")


    #C0378
    ChrTalk(
        0xFE,
        (
            "近些日子啊，\x01",
            "买东西也能送货上门了……\x01",
            "生活真是变得越来越便利了啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_612B")

    Jump("loc_6214")

    label("loc_6130")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_6214")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_61C0")

    #C0379
    ChrTalk(
        0xFE,
        (
            "我老伴又开始\x01",
            "折腾屋里的装潢了。\x02",
        )
    )

    CloseMessageWindow()

    #C0380
    ChrTalk(
        0xFE,
        (
            "每到这时候，\x01",
            "就把我赶到屋子外面……\x02",
        )
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0xFE,
        (
            "真是的，我都没办法\x01",
            "安心做手工了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_6214")

    label("loc_61C0")


    #C0382
    ChrTalk(
        0xFE,
        (
            "我老伴退休以后，\x01",
            "好像闲得不行呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0383
    ChrTalk(
        0xFE,
        (
            "他那些浪费米拉的爱好，\x01",
            "真是令人头疼啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6214")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_16_5680 end

    def Function_17_621C(): pass

    label("Function_17_621C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8F, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_638D")

    #C0384
    ChrTalk(
        0xFE,
        (
            "嗯，你们就是达德利\x01",
            "提过的那群家伙吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0385
    ChrTalk(
        0xFE,
        (
            "……你们妨碍了保安工作，\x01",
            "请赶快离开。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0386
    ChrTalk(
        0x101,
        "#0005F哎……？\x02",
    )

    CloseMessageWindow()

    #C0387
    ChrTalk(
        0xFE,
        (
            "……这里是\x01",
            "伊莉娅·普拉提耶的家。\x02",
        )
    )

    CloseMessageWindow()

    #C0388
    ChrTalk(
        0xFE,
        (
            "她的个人安全\x01",
            "由我们一科来保护。\x02",
        )
    )

    CloseMessageWindow()

    #C0389
    ChrTalk(
        0x104,
        (
            "#0305F（搜查一科……\x01",
            "  这么快就开始行动了吗？）\x02",
        )
    )

    CloseMessageWindow()

    #C0390
    ChrTalk(
        0x101,
        "#0003F（真、真是名不虚传……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x8F, 1)
    Jump("loc_64B4")

    label("loc_638D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_639B")
    Jump("loc_64B4")

    label("loc_639B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_6405")

    #C0391
    ChrTalk(
        0xFE,
        (
            "……伊莉娅·普拉提耶\x01",
            "由我们一科来贴身保护。\x02",
        )
    )

    CloseMessageWindow()

    #C0392
    ChrTalk(
        0xFE,
        (
            "特别任务支援科，\x01",
            "请不要给我们添麻烦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_64B4")

    label("loc_6405")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_64B4")

    #C0393
    ChrTalk(
        0xFE,
        (
            "……从恐吓信上的内容来看，\x01",
            "犯人很有可能趁伊莉娅·普拉提耶\x01",
            "在舞台上表演时进行袭击。\x02",
        )
    )

    CloseMessageWindow()

    #C0394
    ChrTalk(
        0xFE,
        (
            "但是，这并不意味着其它时候就一定安全。\x01",
            "一科将会进行\x01",
            "滴水不漏的保护工作。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_64B4")

    TalkEnd(0xFE)
    Return()

    # Function_17_621C end

    def Function_18_64B8(): pass

    label("Function_18_64B8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_64C9")
    Jump("loc_65D9")

    label("loc_64C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_6539")

    #C0395
    ChrTalk(
        0xFE,
        (
            "嗯，屋外也很危险……\x01",
            "有可能从外面进行狙击。\x02",
        )
    )

    CloseMessageWindow()

    #C0396
    ChrTalk(
        0xFE,
        (
            "在伊莉娅小姐回来之前，\x01",
            "先把周围清查一遍吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_65D9")

    label("loc_6539")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_65D9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6585")

    #C0397
    ChrTalk(
        0xFE,
        "没有窃听器……\x02",
    )

    CloseMessageWindow()

    #C0398
    ChrTalk(
        0xFE,
        (
            "至少房间里面\x01",
            "是安全的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_65D9")

    label("loc_6585")

    TurnDirection(0xFE, 0x0, 0)

    #C0399
    ChrTalk(
        0xFE,
        "……特别任务支援科？\x02",
    )

    CloseMessageWindow()

    #C0400
    ChrTalk(
        0xFE,
        (
            "哼，伊莉娅小姐就由我们\x01",
            "搜查一科负责贴身保护。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_65D9")

    TalkEnd(0xFE)
    Return()

    # Function_18_64B8 end

    def Function_19_65DD(): pass

    label("Function_19_65DD")

    TalkBegin(0x12)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_6938")
    OP_64(0x12)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_66C9")

    #C0401
    ChrTalk(
        0x12,
        (
            "呼啊……呼啊啊……\x02\x03",

            "嗯嗯……嗯～……！\x02",
        )
    )

    CloseMessageWindow()

    #C0402
    ChrTalk(
        0x153,
        (
            "#1110F那么漂亮的大姐姐，\x01",
            "打的呼噜竟然这么响！\x02",
        )
    )

    CloseMessageWindow()

    #C0403
    ChrTalk(
        0x101,
        "#0006F（稍稍有点性感的感觉，真让人困扰啊……）\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_66C4")

    #C0404
    ChrTalk(
        0x104,
        "#0309F（今天果然是个超级幸运日……！）\x02",
    )

    CloseMessageWindow()

    label("loc_66C4")

    Jump("loc_6921")

    label("loc_66C9")


    #C0405
    ChrTalk(
        0x12,
        "呼啊……呼啊……\x02",
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    OP_63(0x153, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_64(0x153)

    #C0406
    ChrTalk(
        0x153,
        (
            "#1110F哇……\x01",
            "好响的呼噜呀！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_6781")

    #C0407
    ChrTalk(
        0x101,
        (
            "#0006F房间还是\x01",
            "和以前一样乱……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_67AA")

    label("loc_6781")


    #C0408
    ChrTalk(
        0x101,
        (
            "#0006F而且，这房间\x01",
            "还真是好乱啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_67AA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_67FE")

    #C0409
    ChrTalk(
        0x102,
        (
            "#0100F和公演时舞台上那种\x01",
            "扣人心弦的紧张氛围完全不同呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_691B")

    label("loc_67FE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6846")

    #C0410
    ChrTalk(
        0x103,
        (
            "#0200F她还是一如往常，\x01",
            "莫名地有些大叔气质呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_691B")

    label("loc_6846")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_691B")

    #C0411
    ChrTalk(
        0x104,
        (
            "#0304F呵……这才是天下无敌的\x01",
            "伊莉娅·普拉提耶啊。\x02\x03",

            "#0309F没想到，竟然能亲眼看到\x01",
            "她的睡姿，今天真是太幸运了！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0412
    ChrTalk(
        0x153,
        "#1111F？？？\x02",
    )

    CloseMessageWindow()

    #C0413
    ChrTalk(
        0x101,
        "#0003F呃，琪雅听不懂也没关系的。\x02",
    )

    CloseMessageWindow()

    label("loc_691B")

    SetScenarioFlags(0xBF, 3)
    SetScenarioFlags(0x0, 6)

    label("loc_6921")

    OP_63(0x12, 0x0, 2000, 0x1C, 0x21, 0xFA, 0x0)
    Jump("loc_6A97")

    label("loc_6938")

    OP_4B(0x15, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_69E7")

    #C0414
    ChrTalk(
        0x12,
        (
            "#1700F好了，修利。\x01",
            "首先要教给你的是\x01",
            "训练的固定规矩哦。\x02\x03",

            "#1709F你要在早上五点以前\x01",
            "把我叫起来！\x02\x03",

            "#1705F啊……没有别的床了，一起睡吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0415
    ChrTalk(
        0x15,
        "才不要！！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_6A93")

    label("loc_69E7")


    #C0416
    ChrTalk(
        0x15,
        (
            "比起那个，给我讲讲关于舞台表演的事情吧，\x01",
            "关于那部新剧的……\x02",
        )
    )

    CloseMessageWindow()

    #C0417
    ChrTalk(
        0x12,
        (
            "#1702F啊，舞台表演方面的事吗？\x01",
            "好呀，我这就和你说！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    #C0418
    ChrTalk(
        0x15,
        "………………！（拼命点头）\x02",
    )

    CloseMessageWindow()

    label("loc_6A93")

    OP_4C(0x15, 0xFF)

    label("loc_6A97")

    TalkEnd(0x12)
    Return()

    # Function_19_65DD end

    def Function_20_6A9B(): pass

    label("Function_20_6A9B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB8, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6C20")

    #C0419
    ChrTalk(
        0x14,
        (
            "#1802F各位，今天\x01",
            "真是给你们添麻烦了……\x02\x03",

            "#1809F非常感谢大家。\x01",
            "能圆满收场，真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0420
    ChrTalk(
        0x102,
        (
            "#0109F我们也没想到\x01",
            "事情的发展会是这样。\x02",
        )
    )

    CloseMessageWindow()

    #C0421
    ChrTalk(
        0x14,
        (
            "#1804F是啊……\x02\x03",

            "#1810F……我也有点理解\x01",
            "那孩子的心情。\x02\x03",

            "我在遇到伊莉娅小姐之前，\x01",
            "也曾经迷失了方向……\x02",
        )
    )

    CloseMessageWindow()

    #C0422
    ChrTalk(
        0x101,
        "#0005F莉夏……？\x02",
    )

    CloseMessageWindow()

    #C0423
    ChrTalk(
        0x14,
        (
            "#1804F啊，不……\x01",
            "没什么。\x02\x03",

            "#1802F修利和伊莉娅小姐\x01",
            "似乎住在一起了。\x01",
            "以后有空时，请再来探望她们吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB8, 4)
    Jump("loc_6D05")

    label("loc_6C20")


    #C0424
    ChrTalk(
        0x14,
        (
            "#1808F修利似乎也\x01",
            "经历了不少事情，\x01",
            "也许没那么容易就能相处融洽。\x02\x03",

            "#1802F不过，我也会一起帮忙……\x01",
            "肯定没问题的。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6D02")

    #C0425
    ChrTalk(
        0x101,
        (
            "#0000F是吗……\x01",
            "那么她们两个人\x01",
            "就拜托你啦，莉夏。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x14, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    #C0426
    ChrTalk(
        0x14,
        "#1809F嗯，交给我吧！\x02",
    )

    CloseMessageWindow()

    label("loc_6D02")

    SetScenarioFlags(0x0, 7)

    label("loc_6D05")

    TalkEnd(0xFE)
    Return()

    # Function_20_6A9B end

    def Function_21_6D09(): pass

    label("Function_21_6D09")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0xC)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6EB0")

    #C0427
    ChrTalk(
        0x101,
        (
            "#0002F看起来，\x01",
            "情况好像还挺顺利的啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0428
    ChrTalk(
        0xFE,
        "哼，也没什么……\x02",
    )

    CloseMessageWindow()

    #C0429
    ChrTalk(
        0xFE,
        (
            "就是说了些话嘛。\x01",
            "和演出有关的事，我都很感兴趣。\x01",
            "……光听就觉得很有趣了。\x02",
        )
    )

    CloseMessageWindow()

    #C0430
    ChrTalk(
        0x102,
        (
            "#0100F（果然对表演\x01",
            "  很有兴趣啊。）\x02",
        )
    )

    CloseMessageWindow()

    #C0431
    ChrTalk(
        0x104,
        (
            "#0304F（这不是也挺像个\x01",
            "  女孩子的嘛。）\x02",
        )
    )

    CloseMessageWindow()

    #C0432
    ChrTalk(
        0x103,
        "#0202F（是啊。）\x02",
    )

    CloseMessageWindow()

    #C0433
    ChrTalk(
        0xFE,
        "啊，还有……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x15, 0x101, 500)

    #C0434
    ChrTalk(
        0xFE,
        (
            "你叫罗伊德吧？\x01",
            "给我记住了。\x02",
        )
    )

    CloseMessageWindow()

    #C0435
    ChrTalk(
        0xFE,
        (
            "我绝对不会\x01",
            "忘记那次的仇恨！\x02",
        )
    )

    CloseMessageWindow()

    #C0436
    ChrTalk(
        0x101,
        (
            "#0012F唔……那件事啊。\x01",
            "（真希望她能忘掉啊……）\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x1D, 0x1, 0xC)
    Jump("loc_6F21")

    label("loc_6EB0")


    #C0437
    ChrTalk(
        0xFE,
        (
            "伊莉娅……小姐，\x01",
            "讲的事情都特别有趣。\x01",
            "光是听听，都觉得十分兴奋……\x02",
        )
    )

    CloseMessageWindow()

    #C0438
    ChrTalk(
        0xFE,
        (
            "……不过她平时是个\x01",
            "特别邋遢的人呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6F21")

    TalkEnd(0xFE)
    Return()

    # Function_21_6D09 end

    def Function_22_6F25(): pass

    label("Function_22_6F25")

    EventBegin(0x0)
    Sound(103, 0, 100, 0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-170, 1280, 390, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22000, 0)
    SetChrPos(0x101, -600, 0, 150, 0)
    SetChrPos(0x102, 600, 0, 150, 0)
    SetChrPos(0x103, -600, 0, -1500, 0)
    SetChrPos(0x104, 600, 0, -1500, 0)

    def lambda_6FAF():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_6FAF)

    def lambda_6FC4():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_6FC4)

    def lambda_6FD9():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_6FD9)

    def lambda_6FEE():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_6FEE)
    OP_68(50, 1280, 1520, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(2000)

    #C0439
    ChrTalk(
        0x101,
        (
            "#5P#0005F『雷森别墅』的\x01",
            "顶层……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_68(1520, 11280, 18040, 3000)
    MoveCamera(45, 16, 0, 3000)
    Sleep(3200)

    #C0440
    ChrTalk(
        0x101,
        (
            "#0000F那里就是伊莉娅小姐\x01",
            "的房间吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(50, 1280, 1520, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22000, 0)
    OP_0D()

    #C0441
    ChrTalk(
        0x103,
        (
            "#6P#0200F先去房间里\x01",
            "检查一下吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0442
    ChrTalk(
        0x101,
        "#5P#0000F嗯，去看看吧。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 10, 30, 990, 0)
    OP_29(0x1D, 0x1, 0x2)
    OP_C7(0x0, 0x1000)
    EventEnd(0x5)
    Return()

    # Function_22_6F25 end

    def Function_23_7124(): pass

    label("Function_23_7124")

    EventBegin(0x0)
    Fade(500)
    OP_68(-270, 11270, 18770, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(20500, 0)
    SetChrPos(0x101, -800, 10000, 19000, 0)
    SetChrPos(0x102, 200, 10000, 19000, 0)
    SetChrPos(0x103, -800, 10000, 17700, 0)
    SetChrPos(0x104, 200, 10000, 17700, 0)
    OP_0D()
    Sound(810, 0, 100, 0)
    Sleep(300)
    SetChrName("")

    #A0443
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "门上了锁。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0444
    ChrTalk(
        0x101,
        "#5P#0000F好了，钥匙在……\x02",
    )

    CloseMessageWindow()
    OP_95(0x101, -140, 10030, 20150, 1000, 0x0)
    OP_93(0x101, 0x0, 0x1F4)
    Sleep(400)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(600)

    #C0445
    ChrTalk(
        0x104,
        "#12P#0305F罗伊德，怎么了吗？\x02",
    )

    CloseMessageWindow()

    #C0446
    ChrTalk(
        0x101,
        "#11P#0005F啊……\x02",
    )

    CloseMessageWindow()
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1300)

    #C0447
    ChrTalk(
        0x101,
        "#11P#0001F有被人撬开过的痕迹。\x02",
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(12)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(15)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0448
    ChrTalk(
        0x101,
        (
            "#11P#0003F只在钥匙孔边留有一点痕迹……\x01",
            "那个人的手法似乎很高超啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0449
    ChrTalk(
        0x103,
        (
            "#6P#0200F看起来，的确是\x01",
            "进入过房间啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0450
    ChrTalk(
        0x102,
        (
            "#12P#0101F果然……\x01",
            "必须要赶快把他抓到。\x02",
        )
    )

    CloseMessageWindow()

    #C0451
    ChrTalk(
        0x101,
        (
            "#5P#0001F是啊，再这么下去，\x01",
            "也不利于跟踪狂\x01",
            "改过自新呢……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    Sound(809, 0, 100, 0)
    Sleep(500)
    ClearMapObjFlags(0x2, 0x10)
    OP_71(0x2, 0x0, 0xA, 0x0, 0x0)
    Sound(103, 0, 100, 0)
    OP_79(0x2)
    OP_93(0x101, 0xB4, 0x190)
    Sleep(300)

    #C0452
    ChrTalk(
        0x101,
        (
            "#5P#0001F各位，全力\x01",
            "进行调查吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0453
    ChrTalk(
        0x104,
        "#12P#0300F好！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapObjFlags(0x2, 0x10)
    OP_65(0x0, 0x1)
    OP_68(49380, 1280, 51150, 0)
    MoveCamera(45, 28, 0, 0)
    OP_6E(560, 0)
    SetCameraDistance(14880, 0)
    SetChrPos(0x101, 49100, 0, 50000, 0)
    SetChrPos(0x102, 50200, 0, 50000, 0)
    SetChrPos(0x103, 49100, 0, 49000, 0)
    SetChrPos(0x104, 50200, 0, 49000, 0)

    def lambda_74AF():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_74AF)

    def lambda_74C4():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_74C4)

    def lambda_74D9():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_74D9)

    def lambda_74EE():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_74EE)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(2000)

    #C0454
    ChrTalk(
        0x104,
        (
            "#12P#0300F真不愧是高级公寓的顶层，\x01",
            "房间真不错啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0455
    ChrTalk(
        0x101,
        (
            "#5P#0000F嗯，真不愧是伊莉娅小姐，\x01",
            "能一个人住在\x01",
            "这么宽敞的房间里……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    #C0456
    ChrTalk(
        0x101,
        (
            "#5P#0005F哎，房间里\x01",
            "好像稍微有点乱啊？\x02",
        )
    )

    CloseMessageWindow()
    OP_68(50860, 1280, 60190, 2200)
    Sleep(2600)
    Fade(500)
    OP_68(59700, 1280, 53950, 0)
    MoveCamera(53, 26, 0, 0)
    OP_68(59740, 1280, 53790, 2600)
    MoveCamera(37, 26, 0, 2600)
    Sleep(3000)

    #C0457
    ChrTalk(
        0x103,
        (
            "#0200F葡萄酒杯、脱下之后\x01",
            "随便乱丢的衣服……\x02\x03",

            "#0203F这应该不是跟踪狂所为，\x01",
            "而是她自己搞的吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0458
    ChrTalk(
        0x102,
        (
            "#0100F这么一说，伊莉娅小姐\x01",
            "确实有种女中豪杰的气质……\x01",
            "这房间与她本人的感觉倒是挺相称的。\x02",
        )
    )

    CloseMessageWindow()

    #C0459
    ChrTalk(
        0x104,
        (
            "#0306F唉，对于她的崇拜者来说，\x01",
            "大概会难以接受吧……\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(50120, 1280, 51750, 0)
    MoveCamera(41, 26, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21500, 0)
    OP_93(0x0, 0x5A, 0x0)
    OP_93(0x1, 0x5A, 0x0)
    OP_93(0x2, 0x5A, 0x0)
    OP_93(0x3, 0x5A, 0x0)
    OP_0D()
    Sleep(300)

    def lambda_7771():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7771)

    def lambda_777E():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_777E)

    def lambda_778B():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_778B)

    def lambda_7798():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7798)
    Sleep(300)

    #C0460
    ChrTalk(
        0x101,
        (
            "#5P#0001F总之，\x01",
            "先调查犯人的行踪吧。\x02\x03",

            "#0003F这次的首要目的当然是\x01",
            "把犯人捉住，并将他带到\x01",
            "伊莉娅小姐的面前……\x02\x03",

            "#0001F不过，在前期调查时\x01",
            "最好也要谨慎行事。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1400)

    #C0461
    ChrTalk(
        0x102,
        (
            "#11P#0103F关于这次的跟踪狂事件，\x01",
            "我们只掌握到了一点模糊的目击情报而已。\x02\x03",

            "#0100F如果不将其当场抓获的话，\x01",
            "犯人完全可以一口咬定不是自己所为。\x02",
        )
    )

    CloseMessageWindow()

    #C0462
    ChrTalk(
        0x104,
        (
            "#12P#0306F原来如此，\x01",
            "这可真有点麻烦啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0463
    ChrTalk(
        0x103,
        (
            "#6P#0200F也就是说，为了确保能将犯人抓获归案，\x01",
            "一定要预先确定犯人的体貌特征、行动模式，\x01",
            "以及侵入路线等事项，对吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0464
    ChrTalk(
        0x101,
        (
            "#5P#0000F是啊，总之先向这间公寓\x01",
            "内的住户询问一下吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0465
    ChrTalk(
        0x104,
        (
            "#12P#0300F同时也要搞清楚\x01",
            "公寓的内部结构。\x02\x03",

            "在问话的同时，\x01",
            "顺便在公寓内检查一圈吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 49850, 30, 51640, 0)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xC, -46140, 1030, 59110, 0)
    SetChrPos(0xE, -45740, 1030, 60980, 180)
    BeginChrThread(0xC, 0, 0, 0)
    SetChrFlags(0xC, 0x10)
    SetChrFlags(0xE, 0x10)
    OP_29(0x1D, 0x1, 0x3)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_23_7124 end

    def Function_24_7A9F(): pass

    label("Function_24_7A9F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(49570, 1280, 52340, 0)
    MoveCamera(44, 25, 0, 0)
    OP_6E(420, 0)
    SetCameraDistance(21470, 0)
    SetChrPos(0x101, 48900, 0, 53200, 135)
    SetChrPos(0x102, 50400, 0, 53200, 225)
    SetChrPos(0x103, 48900, 0, 51800, 45)
    SetChrPos(0x104, 50400, 0, 51800, 315)
    Sleep(500)
    FadeToBright(2000, 0)
    OP_0D()

    #C0466
    ChrTalk(
        0x101,
        (
            "#5P#0003F犯人的特征，侵入公寓的路线……\x01",
            "基本已经搞清楚了。\x02",
        )
    )

    CloseMessageWindow()

    #C0467
    ChrTalk(
        0x103,
        (
            "#6P#0200F是啊。\x02\x03",

            "犯人是戴着帽子的少年，\x01",
            "行动好像十分谨慎。\x02",
        )
    )

    CloseMessageWindow()

    #C0468
    ChrTalk(
        0x102,
        (
            "#11P#0101F而且最近似乎多次\x01",
            "出入过这个房间。\x02\x03",

            "#0103F……但据伊莉娅小姐所说，\x01",
            "她好像并没有丢失什么东西……\x02",
        )
    )

    CloseMessageWindow()

    #C0469
    ChrTalk(
        0x104,
        (
            "#12P#0306F不过跟踪狂这种人基本上\x01",
            "都没有什么明确的目的吧？\x02\x03",

            "#0301F此外，我们了解到的情报还有……\x01",
            "犯人恐怕是从\x01",
            "公寓的后门潜入进来的。\x02",
        )
    )

    CloseMessageWindow()

    #C0470
    ChrTalk(
        0x101,
        (
            "#5P#0003F好，就以上述情报为基础，\x01",
            "准备伏击他吧。\x02\x03",

            "#0000F各位，能听我说一下吗？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7CFA():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7CFA)
    Sleep(10)

    def lambda_7D0A():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7D0A)
    Sleep(300)

    #C0471
    ChrTalk(
        0x103,
        (
            "#12P#0205F罗伊德前辈，\x01",
            "你又想出什么计划了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0472
    ChrTalk(
        0x101,
        (
            "#0000F对方虽然只是个少年，\x01",
            "但我们绝不能掉以轻心。\x02\x03",

            "为了确保能顺利将他捉拿归案，\x01",
            "我们应该制定一个计划。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 25)
    Return()

    # Function_24_7A9F end

    def Function_25_7DD2(): pass

    label("Function_25_7DD2")

    EventBegin(0x0)
    OP_68(-9520, 1270, 4050, 0)
    MoveCamera(45, 13, 0, 0)
    OP_6E(320, 0)
    SetCameraDistance(22920, 0)
    SetChrPos(0x8, 10310, 10000, 17660, 45)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x15, 0x8000)
    OP_52(0x15, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    LoadChrToIndex("chr/ch10100.itc", 0x1E)
    SetChrChipByIndex(0x15, 0x1E)
    SetChrSubChip(0x15, 0x0)
    OP_4B(0x15, 0xFF)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x103, 0x80)
    SetChrFlags(0x104, 0x80)
    SetChrFlags(0x15, 0x80)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    PlayBGM("ed7302", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x12E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetCameraDistance(25420, 3000)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1300)
    OP_68(9410, 11270, 15790, 6000)
    MoveCamera(45, 18, 0, 6000)
    OP_6E(320, 6000)
    SetCameraDistance(28920, 6000)
    Sleep(6800)
    OP_4B(0x8, 0xFF)

    #C0473
    ChrTalk(
        0x8,
        (
            "#5P好啦，\x01",
            "走廊已经打扫完毕。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    OP_93(0x8, 0xE1, 0x1F4)
    Sleep(300)

    #C0474
    ChrTalk(
        0x8,
        (
            "#5P不好，因为明天有游行，\x01",
            "丢垃圾的时间\x01",
            "改到其它时段了。\x02",
        )
    )

    CloseMessageWindow()

    #C0475
    ChrTalk(
        0x8,
        (
            "#5P我得去金德尔先生家\x01",
            "通知一声。\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x8, 1, 0, 26)
    Sleep(4500)
    OP_68(-5680, 1250, 6550, 4200)
    MoveCamera(45, 22, 0, 4200)
    OP_6E(320, 4200)
    SetCameraDistance(31420, 4200)
    SetChrPos(0x15, -5900, 30, 6280, 180)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x15, 0x4)
    OP_6F(0x1)
    Sleep(300)

    #N0476
    NpcTalk(
        0x15,
        "少年",
        "#5P………………………………\x02",
    )

    CloseMessageWindow()
    OP_95(0x15, -7610, 30, 4530, 1900, 0x1)
    OP_95(0x15, -9430, 20, 4530, 1900, 0x1)

    def lambda_7FFF():
        OP_95(0xFE, -9430, 1150, 6880, 1900, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_7FFF)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-270, 11270, 18770, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(20500, 0)
    SetChrPos(0x15, 2800, 10000, 18580, 270)

    def lambda_8063():
        OP_95(0xFE, -250, 10000, 18580, 1700, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_8063)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(700)
    EndChrThread(0x15, 0x1)
    OP_95(0x15, -250, 10020, 19710, 1700, 0x0)
    Sleep(300)

    #N0477
    NpcTalk(
        0x15,
        "少年",
        "#5P………………………………\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    #A0478
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "少年取出了铁丝，\x01",
            "熟练地将其插入到钥匙孔中。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(833, 0, 100, 0)
    Sleep(1000)
    Sound(809, 0, 100, 0)
    Sleep(500)
    ClearMapObjFlags(0x2, 0x10)
    OP_71(0x2, 0x0, 0xA, 0x0, 0x0)
    Sound(103, 0, 100, 0)
    Sleep(200)

    #N0479
    NpcTalk(
        0x15,
        "少年",
        "#5P哼……太简单了。\x02",
    )

    CloseMessageWindow()
    OP_95(0x15, -250, 10000, 22830, 1500, 0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapObjFlags(0x2, 0x10)
    OP_68(50000, 1280, 51630, 0)
    MoveCamera(45, 24, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21000, 0)
    SetChrPos(0x15, 50000, 30, 51630, 0)
    SetChrPos(0x102, 56790, 1000, 55420, 0)
    SetChrPos(0x103, 57110, 1000, 54440, 0)
    SetChrPos(0x104, 49770, 0, 50440, 0)
    SetChrPos(0x101, 56790, 1000, 55420, 0)
    FadeToBright(1000, 0)
    OP_0D()

    #N0480
    NpcTalk(
        0x15,
        "少年",
        "#5P好，今天我一定要……\x02",
    )

    CloseMessageWindow()
    OP_93(0x15, 0x5A, 0x1F4)
    Sleep(400)
    OP_93(0x15, 0x0, 0x1F4)
    Sleep(200)

    #N0481
    NpcTalk(
        0x15,
        "少年",
        (
            "#5P呃，还是\x01",
            "这么脏乱啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_68(51840, 1280, 59480, 3000)
    OP_95(0x15, 50000, 1050, 57300, 1800, 0x0)

    #N0482
    NpcTalk(
        0x15,
        "少年",
        (
            "#5P唉呀，又喝了\x01",
            "这么多。\x02",
        )
    )

    CloseMessageWindow()

    #N0483
    NpcTalk(
        0x15,
        "少年",
        (
            "#5P……看到这么脏乱的房间，\x01",
            "连偷东西的心情都没了。\x01",
            "真是的……\x02",
        )
    )

    CloseMessageWindow()
    OP_68(55300, 1280, 61530, 3000)
    OP_95(0x15, 53730, 1030, 57300, 1600, 0x0)
    OP_95(0x15, 54180, 1030, 60610, 1600, 0x0)
    OP_93(0x15, 0x10E, 0x1F4)

    #N0484
    NpcTalk(
        0x15,
        "少年",
        "#5P那么……该偷点什么好呢？\x02",
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1300)

    #N0485
    NpcTalk(
        0x15,
        "少年",
        (
            "#5P不，这种东西可不行。\x01",
            "……得找些更能让她着急的东西。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(56080, 1280, 62450, 1000)
    OP_95(0x15, 54710, 1030, 61820, 1600, 0x0)

    #N0486
    NpcTalk(
        0x15,
        "少年",
        (
            "#5P嘿，要不然，\x01",
            "干脆就撬开保险箱……\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x102, 0x80)
    ClearChrFlags(0x103, 0x80)
    ClearChrFlags(0x104, 0x80)

    #N0487
    NpcTalk(
        0x101,
        "声音",
        "#1P#4S──到此为止了！\x02",
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_9C(0x15, 0x0, 0x0, 0x0, 0x320, 0x2EE0)
    Sleep(500)
    TurnDirection(0x15, 0x102, 500)
    OP_68(55910, 2280, 60270, 1200)
    MoveCamera(68, 24, 0, 1200)
    OP_6E(440, 1200)
    SetCameraDistance(21000, 1200)

    def lambda_8492():
        OP_95(0xFE, 56540, 1030, 58700, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8492)

    def lambda_84AC():
        OP_95(0xFE, 55760, 1000, 57400, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_84AC)

    #N0488
    NpcTalk(
        0x15,
        "少年",
        "#5P什么……！？\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x102, 1)

    #C0489
    ChrTalk(
        0x102,
        (
            "#0105F想不到跟踪狂\x01",
            "竟然是这么一个普通的孩子……\x02",
        )
    )

    CloseMessageWindow()

    #C0490
    ChrTalk(
        0x103,
        (
            "#0200F不过，犯罪的事实是不会改变的，\x01",
            "请你乖乖地束手就擒吧。\x02",
        )
    )

    CloseMessageWindow()

    #N0491
    NpcTalk(
        0x15,
        "少年",
        (
            "#5P居、居然有埋伏……\x01",
            "可恶，大意了……！！\x02",
        )
    )

    CloseMessageWindow()

    #N0492
    NpcTalk(
        0x104,
        "青年的声音",
        "哦哦，别想逃跑哟。\x02",
    )

    CloseMessageWindow()
    OP_93(0x15, 0xE1, 0x1F4)
    OP_68(51490, 880, 55350, 1500)
    MoveCamera(47, 24, 0, 1500)
    OP_6E(440, 1500)
    SetCameraDistance(21000, 1500)
    OP_95(0x104, 49860, 30, 52710, 1800, 0x0)

    #C0493
    ChrTalk(
        0x104,
        (
            "#0300F#12P此路不通。\x01",
            "你就乖乖投降吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(55210, 1280, 61550, 0)
    MoveCamera(47, 24, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(23500, 0)
    OP_0D()
    StopBGM(0xBB8)

    #N0494
    NpcTalk(
        0x15,
        "少年",
        "#5P可恶……我才不会被你们抓住呢！\x02",
    )

    CloseMessageWindow()

    #N0495
    NpcTalk(
        0x15,
        "少年",
        "#5P怎么能被你们这些人……\x02",
    )

    CloseMessageWindow()

    #N0496
    NpcTalk(
        0x15,
        "少年",
        (
            "#5P我最讨厌\x01",
            "你们这种人了！！\x02",
        )
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7401", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x191), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(49830, 1950, 54370, 3000)
    MoveCamera(50, 19, 0, 3000)
    SetCameraDistance(24490, 3000)

    def lambda_870D():
        OP_93(0x102, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_870D)

    def lambda_871A():
        OP_93(0x103, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_871A)
    OP_95(0x15, 52040, 1030, 62670, 6000, 0x1)
    OP_95(0x15, 51770, 1000, 58240, 6000, 0x1)
    SetChrChip(0x0, 0x15, 0x32, 0x12C)
    Sleep(100)
    SetChrFlags(0x15, 0x4)
    OP_9D(0x15, 0xCA6C, 0x8FC, 0xD9DA, 0x578, 0x1388)
    Sound(804, 0, 100, 0)
    Sleep(200)
    OP_9D(0x15, 0xCAB2, 0x0, 0xC88C, 0x64, 0x1388)
    SetChrFlags(0x15, 0x4)
    Sound(814, 0, 100, 0)
    OP_95(0x15, 49910, 30, 51420, 7000, 0x0)

    def lambda_87B5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_87B5)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_95(0x15, 49740, 0, 46610, 7000, 0x0)

    #C0497
    ChrTalk(
        0x104,
        "#12P#0305F什么……！？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x15, 500)
    Sleep(400)
    BeginChrThread(0x102, 1, 0, 27)
    BeginChrThread(0x103, 1, 0, 28)

    #C0498
    ChrTalk(
        0x104,
        (
            "#6P#0301F混蛋……\x01",
            "动作倒是挺快啊。\x02",
        )
    )

    CloseMessageWindow()
    SetChrChip(0x1, 0x15, 0x0, 0x0)

    #C0499
    ChrTalk(
        0x103,
        "#11P#0201F兰迪前辈……！\x02",
    )

    CloseMessageWindow()

    #C0500
    ChrTalk(
        0x102,
        "#5P#0101F兰迪，快追！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x102, 500)
    Sleep(200)

    #C0501
    ChrTalk(
        0x104,
        "#0307F#12P好！\x02",
    )

    CloseMessageWindow()
    OP_93(0x104, 0xB4, 0x0)
    OP_93(0x102, 0xB4, 0x0)
    OP_93(0x103, 0xB4, 0x0)

    def lambda_88C0():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_88C0)

    def lambda_88D5():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_88D5)

    def lambda_88EA():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_88EA)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-270, 11270, 18770, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(20500, 0)
    SetChrPos(0x15, -200, 10000, 22910, 0)
    OP_A7(0x15, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    ClearMapObjFlags(0x2, 0x10)
    OP_70(0x2, 0xA)

    def lambda_895E():
        OP_95(0xFE, -200, 10000, 18300, 7000, 0x1)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_895E)
    OP_82(0xC8, 0x64, 0xBB8, 0x12C)
    Sound(103, 0, 100, 0)
    Sound(121, 0, 100, 0)
    Sound(818, 0, 80, 0)
    FadeToBright(250, 0)
    OP_0D()
    WaitChrThread(0x15, 1)
    OP_95(0x15, 7690, 10000, 18300, 7000, 0x0)

    def lambda_89BD():
        OP_95(0xFE, 9100, 10030, 15930, 7000, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_89BD)
    Fade(300)
    OP_68(-3140, 1250, 4150, 0)
    OP_68(-60, 1250, 1780, 1000)
    EndChrThread(0x15, 0x1)
    SetChrPos(0x15, -3510, 30, 3820, 135)
    OP_95(0x15, -310, 0, 620, 7000, 0x0)
    OP_93(0x15, 0xB4, 0x1F4)
    Sleep(400)
    Sound(103, 0, 100, 0)
    Sound(121, 0, 100, 0)
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0502
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "少年打开了房门。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()

    #N0503
    NpcTalk(
        0x15,
        "少年",
        (
            "#11P哼，这些笨蛋。\x01",
            "到这边找去吧……！\x02",
        )
    )

    CloseMessageWindow()
    OP_95(0x15, -5860, 0, 6840, 7000, 0x0)
    OP_95(0x15, -5860, 200, 12240, 7000, 0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x5C, 2)
    NewScene("c020C", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_25_7DD2 end

    def Function_26_8AD8(): pass

    label("Function_26_8AD8")

    OP_95(0x8, 9010, 10020, 15730, 2100, 0x0)
    OP_95(0x8, 8610, 7500, 10850, 2100, 0x0)
    OP_95(0x8, 1970, 5000, 10850, 2300, 0x0)
    OP_95(0x8, -2860, 5000, 17000, 2300, 0x0)
    SetChrFlags(0x8, 0x80)
    Return()

    # Function_26_8AD8 end

    def Function_27_8B2E(): pass

    label("Function_27_8B2E")

    OP_95(0x102, 49750, 1050, 57720, 5000, 0x0)
    OP_93(0x102, 0xB4, 0x1F4)
    Return()

    # Function_27_8B2E end

    def Function_28_8B4A(): pass

    label("Function_28_8B4A")

    OP_95(0x103, 50510, 1000, 56870, 5000, 0x0)
    OP_93(0x103, 0xB4, 0x1F4)
    Return()

    # Function_28_8B4A end

    def Function_29_8B66(): pass

    label("Function_29_8B66")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch10100.itc", 0x1E)
    LoadChrToIndex("chr/ch05100.itc", 0x1F)
    OP_68(48420, 2250, 52020, 0)
    MoveCamera(43, 12, 0, 0)
    OP_6E(540, 0)
    SetCameraDistance(16100, 0)
    OP_68(48360, 2250, 51810, 0)
    MoveCamera(43, 12, 0, 0)
    OP_6E(540, 0)
    SetCameraDistance(16100, 0)
    SetChrChipByIndex(0x15, 0x1E)
    SetChrSubChip(0x15, 0x0)
    SetChrChipByIndex(0x12, 0x1F)
    SetChrSubChip(0x12, 0x0)
    SetChrPos(0x101, 49320, 0, 50740, 0)
    SetChrPos(0x102, 52190, 0, 53090, 270)
    SetChrPos(0x104, 52150, 0, 51670, 270)
    SetChrPos(0x103, 50770, 0, 50780, 0)
    SetChrPos(0x12, 49730, 1000, 55910, 180)
    SetChrPos(0x14, 50950, 1000, 55970, 225)
    SetChrPos(0x15, 49800, 30, 52560, 0)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x12, 0x4)
    OP_4B(0x12, 0xFF)
    OP_4B(0x14, 0xFF)
    OP_4B(0x15, 0xFF)
    SetChrName("")

    #A0504
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德等人与伊莉娅进行联络，\x01",
            "告知犯人已经被逮捕了。\x02",
        )
    )

    CloseMessageWindow()

    #A0505
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "少年虽然做了短时间的挣扎，\x01",
            "但最终还是放弃抵抗，安静了下来。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    PlayBGM("ed7111", 0)
    SetCameraDistance(15100, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x10)
    Sleep(300)

    #C0506
    ChrTalk(
        0x12,
        (
            "#5P#1705F哎……这么说，\x01",
            "你就是那个跟踪狂吗？\x02\x03",

            "#1700F个头比我想象中的还要小呢……\x01",
            "你不是克洛斯贝尔本地人吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0507
    ChrTalk(
        0x101,
        (
            "#12P#0006F是的，似乎出身于\x01",
            "边境的贫民区。\x02\x03",

            "#0001F只是，别说是事情的经过，\x01",
            "他连自己的名字也不肯说呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0508
    ChrTalk(
        0x12,
        (
            "#5P#1703F啊，是这样啊。\x02\x03",

            "#1700F……我说你啊，为什么\x01",
            "要缠着我呢？\x02\x03",

            "你是有什么想要的东西吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x15, 0x13B, 0x190)
    Sleep(300)

    #N0509
    NpcTalk(
        0x15,
        "少年",
        "#6P哼，才没有……\x02",
    )

    CloseMessageWindow()

    #N0510
    NpcTalk(
        0x15,
        "少年",
        (
            "#6P我只是想\x01",
            "惹你生气而已。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x12, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(3)
    OP_63(0x14, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(5)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(4)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0511
    ChrTalk(
        0x14,
        "#1805F#11P惹人生气……？\x02",
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    OP_93(0x15, 0x0, 0x1F4)
    Sleep(300)

    #N0512
    NpcTalk(
        0x15,
        "少年",
        "#6P你们这群人懂什么……\x02",
    )

    CloseMessageWindow()

    #N0513
    NpcTalk(
        0x15,
        "少年",
        (
            "#6P住在这么好的地方，\x01",
            "每天都吃着美味的食物……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    OP_82(0x96, 0x0, 0xBB8, 0x320)

    #N0514
    NpcTalk(
        0x15,
        "少年",
        (
            "#6P#4S#N像你们这样的人，\x01",
            "又怎么能理解我这种住在垃圾堆一样的贫民区，\x01",
            "连温饱都成问题的穷人的心情！！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)

    #C0515
    ChrTalk(
        0x101,
        "#12P#0005F…………………………！？\x02",
    )

    CloseMessageWindow()

    #C0516
    ChrTalk(
        0x102,
        "#0108F…………………………\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    OP_93(0x15, 0x13B, 0x190)
    PlayBGM("ed7005", 0)
    Sleep(300)

    #N0517
    NpcTalk(
        0x15,
        "少年",
        (
            "#6P……自从我来到克洛斯贝尔市之后，\x01",
            "就一直将这些事情看在眼里。\x02",
        )
    )

    CloseMessageWindow()

    #N0518
    NpcTalk(
        0x15,
        "少年",
        (
            "#6P住在这里的都是些有钱人，\x01",
            "每天晚上挥霍着大把金钱，游玩享乐。\x02",
        )
    )

    CloseMessageWindow()

    #N0519
    NpcTalk(
        0x15,
        "少年",
        (
            "#6P哈，随他们便吧。\x01",
            "反正我最讨厌那种人了。\x02",
        )
    )

    CloseMessageWindow()

    #N0520
    NpcTalk(
        0x15,
        "少年",
        (
            "#6P……但是，那些家伙都说，\x01",
            "最高级的娱乐就是去看彩虹剧团的演出……\x01",
            "所以我就潜入了一次。\x02",
        )
    )

    CloseMessageWindow()

    #C0521
    ChrTalk(
        0x12,
        "#1705F#5P………哎……………？\x02",
    )

    CloseMessageWindow()

    #C0522
    ChrTalk(
        0x103,
        (
            "#11P#0200F你看了彩虹剧团的……\x01",
            "伊莉娅小姐的\x01",
            "表演了吗……？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x15, 0x0, 0x1F4)
    Sleep(200)

    #N0523
    NpcTalk(
        0x15,
        "少年",
        (
            "#6P我讨厌那些没有危机感，\x01",
            "整天悠哉度日的家伙。\x02",
        )
    )

    CloseMessageWindow()

    #N0524
    NpcTalk(
        0x15,
        "少年",
        (
            "#6P在这其中，我最讨厌的……\x01",
            "#4S就是你了！！\x02",
        )
    )

    CloseMessageWindow()

    #N0525
    NpcTalk(
        0x15,
        "少年",
        (
            "#6P站在那么美丽的舞台上，\x01",
            "演绎着那么动人的世界……\x02",
        )
    )

    CloseMessageWindow()

    #N0526
    NpcTalk(
        0x15,
        "少年",
        (
            "#6P在谁都无法碰触到的地方，\x01",
            "散发着那么耀眼的光芒。\x02",
        )
    )

    CloseMessageWindow()

    #N0527
    NpcTalk(
        0x15,
        "少年",
        (
            "#6P我就算一直拼搏到死，\x01",
            "也绝对无法触及得到……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1500)

    #N0528
    NpcTalk(
        0x15,
        "少年",
        (
            "#6P我就算努力工作，直到累死，\x01",
            "赚到的钱也不够买一张门票。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    OP_82(0x96, 0x64, 0xBB8, 0x320)

    #N0529
    NpcTalk(
        0x15,
        "少年",
        (
            "#6P#4S#N──没错吧！？\x01",
            "那种世界……就算我拼命到死，\x01",
            "也不可能靠近一步啊！！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_63(0x0, 0x0, 2000, 0x18, 0x1B, 0x190, 0x0)
    OP_63(0x1, 0x0, 2000, 0x18, 0x1B, 0x190, 0x0)
    OP_63(0x2, 0x0, 2000, 0x18, 0x1B, 0x190, 0x0)
    OP_63(0x3, 0x0, 2000, 0x18, 0x1B, 0x190, 0x0)
    OP_63(0x12, 0x0, 2000, 0x18, 0x1B, 0x190, 0x0)
    OP_63(0x14, 0x0, 2000, 0x18, 0x1B, 0x190, 0x0)
    Sleep(3200)
    OP_64(0x0)
    OP_64(0x1)
    OP_64(0x2)
    OP_64(0x3)
    OP_64(0x12)
    OP_64(0x14)
    Sleep(500)

    #C0530
    ChrTalk(
        0x104,
        (
            "#11P#0303F………………………………\x01",
            "原来是这么回事啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0531
    ChrTalk(
        0x101,
        (
            "#12P#0008F来到克洛斯贝尔市……\x01",
            "看了伊莉娅小姐的表演……\x02\x03",

            "#0006F的确有可能会产生\x01",
            "这样的冲击呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0532
    ChrTalk(
        0x14,
        (
            "#1803F#11P……说得也是啊……\x02\x03",

            "#1808F克洛斯贝尔市的确\x01",
            "有着这样的一面。\x02\x03",

            "#1801F大都市的黑暗面……\x01",
            "有时会让人感觉绝望而无力……\x02",
        )
    )

    CloseMessageWindow()

    #C0533
    ChrTalk(
        0x12,
        (
            "#1703F#5P………………………………\x02\x03",

            "#1700F算啦，不管怎么样，\x01",
            "也得把事情做个了结啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x14, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_9670():

        label("loc_9670")

        TurnDirection(0xFE, 0x12, 500)
        Yield()
        Jump("loc_9670")

    QueueWorkItem2(0x0, 1, lambda_9670)

    def lambda_9682():

        label("loc_9682")

        TurnDirection(0xFE, 0x12, 500)
        Yield()
        Jump("loc_9682")

    QueueWorkItem2(0x1, 1, lambda_9682)

    def lambda_9694():

        label("loc_9694")

        TurnDirection(0xFE, 0x12, 500)
        Yield()
        Jump("loc_9694")

    QueueWorkItem2(0x2, 1, lambda_9694)

    def lambda_96A6():

        label("loc_96A6")

        TurnDirection(0xFE, 0x12, 500)
        Yield()
        Jump("loc_96A6")

    QueueWorkItem2(0x3, 1, lambda_96A6)

    def lambda_96B8():

        label("loc_96B8")

        TurnDirection(0xFE, 0x12, 500)
        Yield()
        Jump("loc_96B8")

    QueueWorkItem2(0x14, 1, lambda_96B8)
    OP_68(48800, 2250, 51320, 2000)

    def lambda_96DB():
        OP_95(0xFE, 49730, 0, 54230, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_96DB)

    #C0534
    ChrTalk(
        0x102,
        "#11P#0105F伊莉娅小姐……？\x02",
    )

    CloseMessageWindow()

    #C0535
    ChrTalk(
        0x101,
        "#12P#0011F那个，您打算……\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x12, 1)

    #C0536
    ChrTalk(
        0x12,
        (
            "#5P#1701F我叫伊莉娅·普拉提耶。\x01",
            "……你叫什么名字？\x02",
        )
    )

    CloseMessageWindow()

    #N0537
    NpcTalk(
        0x15,
        "少年",
        (
            "#6P……………………………\x01",
            "……修利。\x02",
        )
    )

    CloseMessageWindow()

    #C0538
    ChrTalk(
        0x12,
        (
            "#5P#1703F修利啊，我记住了。\x02\x03",

            "#1701F修利，你就暂时在\x01",
            "剧团里打杂吧。\x02\x03",

            "因为这种事用钱来赔偿\x01",
            "会很麻烦。\x01",
            "所以你就给我好好干活吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(12)
    OP_63(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(18)
    OP_63(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(12)
    OP_63(0x3, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0539
    ChrTalk(
        0x15,
        "#6P……………什么…………\x02",
    )

    CloseMessageWindow()

    #C0540
    ChrTalk(
        0x101,
        "#12P#0005F伊、伊莉娅小姐，您的意思是……？\x02",
    )

    CloseMessageWindow()
    OP_93(0x12, 0x87, 0x190)
    Sleep(200)

    #C0541
    ChrTalk(
        0x12,
        (
            "#5P#1706F抱歉哦，\x01",
            "虽然你们好不容易才抓到他。\x02\x03",

            "#1700F不过，这孩子暂时\x01",
            "就交给我收留吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0542
    ChrTalk(
        0x104,
        "#11P#0302F也就是说，无罪释放吗？\x02",
    )

    CloseMessageWindow()

    #C0543
    ChrTalk(
        0x103,
        (
            "#11P#0202F哎呀呀，真是的。\x01",
            "……算了，既然伊莉娅小姐\x01",
            "都这么说了……\x02",
        )
    )

    CloseMessageWindow()

    #C0544
    ChrTalk(
        0x12,
        "#5P#1704F呵呵，还有啊。\x02",
    )

    CloseMessageWindow()
    OP_93(0x12, 0xB4, 0x190)
    OP_95(0x12, 49900, 0, 53370, 1000, 0x0)
    Sleep(200)
    EndChrThread(0x0, 0x1)
    EndChrThread(0x1, 0x1)
    EndChrThread(0x2, 0x1)
    EndChrThread(0x3, 0x1)
    EndChrThread(0x14, 0x1)
    Sound(819, 0, 100, 0)
    OP_A6(0x15, 0x0, 0xF, 0xC8, 0xBB8)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0545
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "伊莉娅拍了拍少年的肩膀。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    BeginChrThread(0x15, 1, 0, 30)

    #C0546
    ChrTalk(
        0x15,
        "#6P你……你干什么！？\x02",
    )

    CloseMessageWindow()

    #C0547
    ChrTalk(
        0x12,
        (
            "#5P#1709F嗯，跟我想的一样呢。\x02\x03",

            "#1700F不过，要是再长点\x01",
            "肌肉就更好了……\x02",
        )
    )

    CloseMessageWindow()
    EndChrThread(0x15, 0x1)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9B06")
    OP_93(0x15, 0x10E, 0x190)

    label("loc_9B06")

    Sleep(400)
    OP_93(0x15, 0x0, 0x1F4)
    Sleep(200)

    #C0548
    ChrTalk(
        0x12,
        (
            "#5P#1702F修利，其实你\x01",
            "很有资质呢。\x02\x03",

            "#1709F如果努力锻炼的话，或许就能成为\x01",
            "与我和莉夏并驾齐驱的演员哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_63(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0549
    ChrTalk(
        0x15,
        "#6P咦……\x02",
    )

    CloseMessageWindow()
    OP_82(0x96, 0x0, 0xBB8, 0x12C)

    #C0550
    ChrTalk(
        0x15,
        "#6P#4S咦咦咦……！？\x02",
    )

    CloseMessageWindow()

    #C0551
    ChrTalk(
        0x15,
        "#6P为、为什么我要……！？\x02",
    )

    CloseMessageWindow()

    #C0552
    ChrTalk(
        0x102,
        (
            "#11P#0102F这么一说……\x01",
            "这孩子的动作确实很敏捷呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0553
    ChrTalk(
        0x104,
        (
            "#11P#0300F是啊，步子轻盈得\x01",
            "令人惊讶。\x02\x03",

            "#0304F……原来如此，在这方面\x01",
            "很有素质啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0554
    ChrTalk(
        0x12,
        (
            "#5P#1702F嗯，就是这样啦。\x01",
            "总之，你就加入我们剧团吧。\x02\x03",

            "#1709F你是没有选择权的！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    #C0555
    ChrTalk(
        0x15,
        (
            "#6P我、我……\x01",
            "……可是，那个…………\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Sleep(700)
    OP_64(0x15)
    BeginChrThread(0x12, 2, 0, 31)
    Sleep(700)
    BeginChrThread(0x15, 2, 0, 31)
    Sleep(500)

    #C0556
    ChrTalk(
        0x14,
        (
            "#1809F#5P呵呵……\x01",
            "真像伊莉娅小姐的行事风格。\x02\x03",

            "#1810F……我当时也是一样，\x01",
            "被这么强拉硬拽地招揽进了剧团。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    def lambda_9D9C():
        OP_93(0xFE, 0x0, 0x15E)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9D9C)
    Sleep(20)

    def lambda_9DAC():
        OP_93(0xFE, 0x0, 0x15E)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_9DAC)
    Sleep(400)

    #C0557
    ChrTalk(
        0x101,
        (
            "#12P#0002F是、是这样吗……\x02\x03",

            "#0004F不过，多亏了伊莉娅小姐，\x01",
            "事情似乎圆满收场了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0558
    ChrTalk(
        0x103,
        "#11P#0202F是啊。\x02",
    )

    CloseMessageWindow()

    def lambda_9E29():
        OP_93(0xFE, 0x10E, 0x15E)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9E29)
    Sleep(20)

    def lambda_9E39():
        OP_93(0xFE, 0x10E, 0x15E)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_9E39)
    Sleep(800)
    EndChrThread(0x12, 0x2)
    EndChrThread(0x15, 0x2)
    OP_64(0x12)
    OP_64(0x15)

    #C0559
    ChrTalk(
        0x12,
        "#1709F#5P好啦！不许反对～！\x02",
    )

    CloseMessageWindow()

    #C0560
    ChrTalk(
        0x15,
        (
            "#6P我、我还没有\x01",
            "同意吧！？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1900, 0x2C, 0x2F, 0x96, 0x1)
    Sound(25, 0, 100, 0)
    Sleep(200)
    BeginChrThread(0x12, 2, 0, 31)
    Sleep(600)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    EndChrThread(0x12, 0x2)
    OP_64(0x12)
    OP_68(-950, 11250, 18010, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(22750, 0)
    SetChrPos(0x101, -660, 10000, 17460, 0)
    SetChrPos(0x102, 390, 10000, 17460, 0)
    SetChrPos(0x103, -660, 10000, 16030, 0)
    SetChrPos(0x104, 390, 10000, 16030, 0)
    SetChrPos(0x12, -730, 10030, 19740, 180)
    SetChrPos(0x14, 530, 10020, 19600, 180)
    SetChrPos(0x15, -280, 10020, 19200, 180)
    SetChrFlags(0x103, 0x4)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7106", 0)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x6A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    OP_0D()

    #C0561
    ChrTalk(
        0x12,
        (
            "#5P#1705F这就要走了吗？\x01",
            "可以先喝杯茶再走嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0562
    ChrTalk(
        0x101,
        (
            "#0004F#6P不必了，\x01",
            "我们还有其它的工作。\x02\x03",

            "#0005F啊，对了。\x01",
            "钥匙得还给您。\x02",
        )
    )

    CloseMessageWindow()
    OP_95(0x101, -640, 10000, 18640, 1200, 0x0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0563
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x347),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "归还了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    SubItemNumber('红莲钩', 1)
    OP_96(0x101, 0xFFFFFD6C, 0x2710, 0x44FC, 0x4B0, 0x0)

    #C0564
    ChrTalk(
        0x12,
        (
            "#5P#1704F好，我收到了。\x02\x03",

            "#1700F这次真是麻烦你们啦，警察弟弟。\x01",
            "回去的路上要注意安全哦～\x02",
        )
    )

    CloseMessageWindow()

    #C0565
    ChrTalk(
        0x14,
        (
            "#11P#1809F我也要向各位表示谢意。\x01",
            "真是谢谢大家了。\x02",
        )
    )

    CloseMessageWindow()

    #C0566
    ChrTalk(
        0x104,
        (
            "#12P#0309F嗯，再见啦，\x01",
            "小莉夏！\x02",
        )
    )

    CloseMessageWindow()

    #C0567
    ChrTalk(
        0x102,
        (
            "#12P#0102F伊莉娅小姐、莉夏小姐，\x01",
            "修利就麻烦两位照顾了。\x02",
        )
    )

    CloseMessageWindow()

    #C0568
    ChrTalk(
        0x103,
        (
            "#12P#0204F虽然事件已经解决了，\x01",
            "但还是要注意门户安全啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0569
    ChrTalk(
        0x101,
        (
            "#0014F#6P哈哈……如果再有什么事，\x01",
            "欢迎来找我们支援科。\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 1)
    Sleep(200)

    def lambda_A1FC():

        label("loc_A1FC")

        TurnDirection(0xFE, 0x101, 300)
        Yield()
        Jump("loc_A1FC")

    QueueWorkItem2(0x12, 1, lambda_A1FC)

    def lambda_A20E():

        label("loc_A20E")

        TurnDirection(0xFE, 0x101, 300)
        Yield()
        Jump("loc_A20E")

    QueueWorkItem2(0x14, 1, lambda_A20E)
    OP_95(0x101, -600, 10000, 18360, 1000, 0x0)
    OP_93(0x101, 0x2D, 0x190)
    OP_93(0x15, 0xE1, 0x190)
    Sleep(300)

    #C0570
    ChrTalk(
        0x101,
        (
            "#0000F#6P……那么告辞了。\x02\x03",

            "#0002F以后别再做这种事了哦。\x01",
            "是男人的话，就得学会知恩图报啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_68(930, 11250, 17540, 2800)

    def lambda_A2C6():

        label("loc_A2C6")

        TurnDirection(0xFE, 0x101, 300)
        Yield()
        Jump("loc_A2C6")

    QueueWorkItem2(0x15, 1, lambda_A2C6)

    def lambda_A2D8():
        OP_9B(0x0, 0xFE, 0x5A, 0xA28, 0x2BC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A2D8)

    def lambda_A2ED():
        OP_9B(0x0, 0xFE, 0x5A, 0xA28, 0x2BC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A2ED)

    def lambda_A302():
        OP_9B(0x0, 0xFE, 0x5A, 0xA28, 0x2BC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A302)

    def lambda_A317():
        OP_95(0xFE, 1870, 10000, 17460, 700, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A317)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x103, 1)
    OP_64(0x15)

    #C0571
    ChrTalk(
        0x15,
        (
            "#5P……我果然……\x01",
            "还是很讨厌你。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x12, 0x1)
    EndChrThread(0x14, 0x1)
    EndChrThread(0x15, 0x1)

    def lambda_A389():
        TurnDirection(0xFE, 0x15, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_A389)
    Sleep(12)

    def lambda_A399():
        TurnDirection(0xFE, 0x15, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_A399)

    def lambda_A3A6():
        TurnDirection(0xFE, 0x15, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_A3A6)
    Sleep(10)

    def lambda_A3B6():
        TurnDirection(0xFE, 0x15, 400)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_A3B6)
    Sleep(300)

    #C0572
    ChrTalk(
        0x101,
        "#11P#0005F哎……\x02",
    )

    CloseMessageWindow()
    OP_68(930, 11050, 18160, 2000)
    MoveCamera(349, 25, 0, 2000)
    Sleep(500)
    OP_95(0x15, 460, 10000, 18630, 3000, 0x0)
    OP_6F(0x79)
    Sleep(100)
    Fade(250)
    SetChrChipByIndex(0x15, 0xC)
    SetChrSubChip(0x15, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()
    Sleep(300)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    #C0573
    ChrTalk(
        0x15,
        "#5P#4S……我明明是女的啊！！\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x12C, 0x0, 0xBB8, 0x1F4)

    #C0574
    ChrTalk(
        0x15,
        (
            "#5P#4S你到底想耍我\x01",
            "到什么时候！！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x101)
    OP_64(0x104)
    OP_64(0x102)
    Sleep(300)
    OP_82(0xC8, 0x0, 0x7D0, 0x12C)

    #C0575
    ChrTalk(
        0x101,
        "#6P#0011F啊，#4S哎哎哎哎哎哎哎哎哎……！？\x02",
    )

    CloseMessageWindow()

    #C0576
    ChrTalk(
        0x104,
        (
            "#12P#0305F是、是这样吗……！？\x02\x03",

            "#0301F唔，这么一说才发现，\x01",
            "长得的确很可爱啊……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x104, 500)
    Sleep(200)

    #C0577
    ChrTalk(
        0x103,
        (
            "#6P#0205F哎，兰迪前辈\x01",
            "现在才注意到吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x14, 0x104, 500)

    #C0578
    ChrTalk(
        0x14,
        (
            "#5P#1809F不管怎么看，\x01",
            "修利也都是个\x01",
            "女孩子啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0579
    ChrTalk(
        0x101,
        (
            "#6P#0011F…………………………\x02\x03",

            "#0012F那个，抓你的时候，\x01",
            "我没有想到，所以就用了全力……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x12, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x14, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(800)

    def lambda_A69D():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A69D)

    def lambda_A6AA():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A6AA)

    def lambda_A6B7():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_A6B7)

    #C0580
    ChrTalk(
        0x104,
        "#12P#0307F罗伊德，你……\x02",
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_93(0x15, 0xE1, 0x190)
    Sleep(300)

    #C0581
    ChrTalk(
        0x15,
        (
            "#11P所、所以都说了让你赶快放手啊！\x01",
            "你这个笨蛋……！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 500)
    Sleep(500)

    def lambda_A741():
        TurnDirection(0xFE, 0x12, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A741)
    OP_64(0x15)

    #C0582
    ChrTalk(
        0x101,
        (
            "#6P#0011F可是，那个……抓她时的那种手感，\x01",
            "明明是个男的啊……！\x02",
        )
    )

    CloseMessageWindow()

    #C0583
    ChrTalk(
        0x102,
        (
            "#11P#0111F哼……\x01",
            "连手感都还记得啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0584
    ChrTalk(
        0x103,
        "#6P#0211F罗伊德前辈，你说了不该说的话哦。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)
    Sleep(300)

    def lambda_A7F7():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A7F7)

    #C0585
    ChrTalk(
        0x101,
        "#5P#0012F哇啊啊，我不是这个意思……！\x02",
    )

    CloseMessageWindow()

    #C0586
    ChrTalk(
        0x12,
        (
            "#5P#1709F啊哈哈，只是摸一摸而已啦，\x01",
            "没什么大不了的！\x02",
        )
    )

    CloseMessageWindow()

    #C0587
    ChrTalk(
        0x14,
        "#5P#1806F罗伊德警官……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    BeginChrThread(0x101, 1, 0, 32)

    #C0588
    ChrTalk(
        0x101,
        (
            "#6P#0011F不、不是的！\x01",
            "我根本就没有打算要……！！\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(21750, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0589
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【调查跟踪狂！！】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_64(0x101)
    EndChrThread(0x101, 0x1)
    SetChrPos(0x0, -280, 10020, 19290, 180)
    ClearChrFlags(0x103, 0x4)
    SetChrPos(0x12, 52530, 1050, 60070, 270)
    SetChrPos(0x14, 58290, 1030, 62500, 0)
    SetChrPos(0x15, 51930, 1050, 60970, 135)
    SetChrChipByIndex(0x12, 0xD)
    SetChrSubChip(0x12, 0x0)
    OP_4C(0x12, 0xFF)
    OP_4C(0x14, 0xFF)
    OP_4C(0x15, 0xFF)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    SetMapObjFrame(0xFF, "huku_nugippa", 0x0, 0x1)
    SetMapObjFrame(0xFF, "model5", 0x0, 0x1)
    OP_1B(0x8, 0xFF, 0xFFFF)
    OP_65(0x1, 0x1)
    OP_65(0x2, 0x1)
    OP_29(0x1D, 0x4, 0x10)
    OP_29(0x1D, 0x1, 0xA)
    OP_C7(0x1, 0x1000)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_29_8B66 end

    def Function_30_A9E3(): pass

    label("Function_30_A9E3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_AA0F")
    OP_93(0xFE, 0x10E, 0x190)
    OP_93(0xFE, 0xB4, 0x190)
    OP_93(0xFE, 0x5A, 0x190)
    OP_93(0xFE, 0x0, 0x190)
    Jump("Function_30_A9E3")

    label("loc_AA0F")

    Return()

    # Function_30_A9E3 end

    def Function_31_AA10(): pass

    label("Function_31_AA10")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_AA35")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    Jump("Function_31_AA10")

    label("loc_AA35")

    Return()

    # Function_31_AA10 end

    def Function_32_AA36(): pass

    label("Function_32_AA36")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_AA64")
    TurnDirection(0xFE, 0x12, 500)
    Sleep(500)
    TurnDirection(0xFE, 0x102, 500)
    Sleep(500)
    TurnDirection(0xFE, 0x103, 500)
    Sleep(800)
    Jump("Function_32_AA36")

    label("loc_AA64")

    Return()

    # Function_32_AA36 end

    def Function_33_AA65(): pass

    label("Function_33_AA65")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x3)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AA8B")
    Call(0, 23)
    Jump("loc_AAB0")

    label("loc_AA8B")

    TalkBegin(0xFF)
    Sound(810, 0, 100, 0)

    #A0590
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "似乎上了锁。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)

    label("loc_AAB0")

    Return()

    # Function_33_AA65 end

    def Function_34_AAB1(): pass

    label("Function_34_AAB1")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AC29")
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0591
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "葡萄酒瓶和酒杯\x01",
            "随意乱放在桌子上。\x02",
        )
    )

    CloseMessageWindow()

    #A0592
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "酒瓶里的酒喝得几乎见底了……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0593
    ChrTalk(
        0x101,
        (
            "#0012F看样子，昨晚好像是\x01",
            "办了场酒会吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0594
    ChrTalk(
        0x104,
        (
            "#0300F不，伊莉娅·普拉提耶\x01",
            "的酒量似乎相当强。\x02\x03",

            "她平时就能\x01",
            "一个人喝这么多吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0595
    ChrTalk(
        0x101,
        "#0005F呃，是这样吗……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_AC8E")

    label("loc_AC29")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0596
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "葡萄酒瓶和酒杯\x01",
            "随意乱放在桌子上。\x02",
        )
    )

    CloseMessageWindow()

    #A0597
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "酒瓶里的酒喝得几乎见底了……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()

    label("loc_AC8E")

    TalkEnd(0xFF)
    Return()

    # Function_34_AAB1 end

    def Function_35_AC92(): pass

    label("Function_35_AC92")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AD9E")
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0598
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "床上散乱堆放着\x01",
            "各种衣服……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()

    #C0599
    ChrTalk(
        0x102,
        "#0106F这件明明是名牌……\x02",
    )

    CloseMessageWindow()

    #C0600
    ChrTalk(
        0x103,
        "#0200F真是太乱了。\x02",
    )

    CloseMessageWindow()

    #C0601
    ChrTalk(
        0x104,
        (
            "#0303F大概是早上要出门时，慌慌张张从衣橱里\x01",
            "拿出来挑选，然后就直接乱扔在这里的吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0602
    ChrTalk(
        0x101,
        (
            "#0000F简直都能想象出\x01",
            "她临出门时的样子了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_ADD9")

    label("loc_AD9E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0603
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "床上散乱堆放着\x01",
            "各种衣服……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()

    label("loc_ADD9")

    TalkEnd(0xFF)
    Return()

    # Function_35_AC92 end

    def Function_36_ADDD(): pass

    label("Function_36_ADDD")

    EventBegin(0x1)

    #C0604
    ChrTalk(
        0x101,
        (
            "#0000F现在还是专心调查\x01",
            "跟踪狂的事吧。\x02\x03",

            "毕竟伊莉娅小姐\x01",
            "连钥匙都交给我们了。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -160, 30, 1350, 0)
    EventEnd(0x4)
    Return()

    # Function_36_ADDD end

    SaveToFile()

Try(main)
