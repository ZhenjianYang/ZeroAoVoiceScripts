from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "サミィ",                 # 1
        "キンドール",             # 2
        "キンドール",             # 3
        "ブリジッタ",             # 4
        "ルーヴィック老人",       # 5
        "ルーヴィック老人",       # 6
        "オリガ夫人",             # 7
        "オリガ夫人",             # 8
        "捜査官",                 # 9
        "捜査官",                 # 10
        "イリア",                 # 11
        "イリア",                 # 12
        "リーシャ",               # 13
        "シュリ",                 # 14
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
        "Function_9_24F2",         # 09, 9
        "Function_10_2633",        # 0A, 10
        "Function_11_3AAB",        # 0B, 11
        "Function_12_4A53",        # 0C, 12
        "Function_13_5BCB",        # 0D, 13
        "Function_14_5D68",        # 0E, 14
        "Function_15_5E2C",        # 0F, 15
        "Function_16_615D",        # 10, 16
        "Function_17_6E75",        # 11, 17
        "Function_18_7137",        # 12, 18
        "Function_19_727E",        # 13, 19
        "Function_20_776C",        # 14, 20
        "Function_21_7A7A",        # 15, 21
        "Function_22_7CD4",        # 16, 22
        "Function_23_7EF7",        # 17, 23
        "Function_24_88C8",        # 18, 24
        "Function_25_8C49",        # 19, 25
        "Function_26_9A03",        # 1A, 26
        "Function_27_9A59",        # 1B, 27
        "Function_28_9A75",        # 1C, 28
        "Function_29_9A91",        # 1D, 29
        "Function_30_BAD2",        # 1E, 30
        "Function_31_BAFF",        # 1F, 31
        "Function_32_BB25",        # 20, 32
        "Function_33_BB54",        # 21, 33
        "Function_34_BBAC",        # 22, 34
        "Function_35_BDC3",        # 23, 35
        "Function_36_BF14",        # 24, 36
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x3)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_102D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F91")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BDC")

    #C0001
    ChrTalk(
        0x101,
        (
            "#0001F（よし、聞き込みをしてみよう。）\x02\x03",

            "#0000Fすみません、\x01",
            "少しよろしいですか？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BDC")

    SetScenarioFlags(0x1, 2)
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイド達はストーカーについて\x01",
            "心当たりを尋ねてみた。\x02",
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
            "……例のストーカーの話ね。\x01",
            "雇われ管理人として\x01",
            "私も警戒しているわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x102,
        (
            "#0100Fストーカーを実際に\x01",
            "見かけた事はありますか？\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        (
            "私はここに\x01",
            "毎日顔を出しているけど、\x01",
            "実はほとんど無いわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        "でも先日、ちらっとだけ見たわ。\x02",
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "帽子を深くかぶった少年だったけど\x01",
            "すぐに消えてしまったから\x01",
            "詳しい事は判らないわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x103,
        "#0200F他に思い出せる特徴などは？\x02",
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        "そうね……\x02",
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        (
            "あえて言えば、\x01",
            "特に特徴が無いのが特徴ね。\x02",
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
            "地味な格好だったのかしら。\x01",
            "さっぱり記憶に無いわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x104,
        "#0303Fふむ、そう来るか……\x02",
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x101,
        (
            "#0000Fでもリーシャから聞いた情報に\x01",
            "間違いはなさそうだな……\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x1D, 0x1, 0x4)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x5)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x6)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x7)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F8C")

    #C0014
    ChrTalk(
        0x101,
        (
            "#0000Fよし、下調べはこんな所だな。\x02\x03",

            "一旦イリアさんの部屋に戻って\x01",
            "整理してみよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x104,
        "#0300F了解、そろそろ作戦を考えるか！\x02",
    )

    CloseMessageWindow()
    ModifyEventFlags(1, 0, 0x80)
    OP_29(0x1D, 0x1, 0x9)

    label("loc_F8C")

    Jump("loc_1028")

    label("loc_F91")


    #C0016
    ChrTalk(
        0xFE,
        (
            "私が見たのは\x01",
            "帽子を深くかぶった少年ね。\x01",
            "人相までは判らなかったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        (
            "あとは、結構\x01",
            "地味な格好だったと思うわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        "特に記憶に残っていないもの。\x02",
    )

    CloseMessageWindow()

    label("loc_1028")

    Jump("loc_24EE")

    label("loc_102D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_1138")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10CA")

    #C0019
    ChrTalk(
        0xFE,
        "さー、仕事仕事……\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        (
            "これもお給料を溜めて\x01",
            "イリア様の舞台を見るため……\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        (
            "来月辺りのチケットが\x01",
            "確保できるといいわね～。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1133")

    label("loc_10CA")


    #C0022
    ChrTalk(
        0xFE,
        (
            "ゴミの分別も排水溝の掃除も、\x01",
            "すべてはイリア様にお会いするため……\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        "さー、もう少し頑張りますか。\x02",
    )

    CloseMessageWindow()

    label("loc_1133")

    Jump("loc_24EE")

    label("loc_1138")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1281")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1206")

    #C0024
    ChrTalk(
        0xFE,
        (
            "３階の人、この前\x01",
            "ようやく後姿を拝めたわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xFE,
        (
            "出かけていく所だったから\x01",
            "よく見えなかったけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xFE,
        (
            "ま、どこにでもいそうな\x01",
            "普通の人だったわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xFE,
        "金髪は綺麗だったけど。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_127C")

    label("loc_1206")


    #C0028
    ChrTalk(
        0xFE,
        (
            "ま、ファッションを嗜む女性なら\x01",
            "あのくらい決めてて普通よね。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        (
            "うん、後姿からして\x01",
            "意外と普通っぽい人だったわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_127C")

    Jump("loc_24EE")

    label("loc_1281")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_135B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1316")

    #C0030
    ChrTalk(
        0xFE,
        "さ、仕事仕事……\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        (
            "またお給料を溜めて\x01",
            "アルカンシェルを見に行くのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xFE,
        (
            "そのために\x01",
            "わき目も振らず仕事に励むの！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1356")

    label("loc_1316")


    #C0033
    ChrTalk(
        0xFE,
        "これも全てイリア様に会うため……\x02",
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        "今日も仕事、仕事よ！\x02",
    )

    CloseMessageWindow()

    label("loc_1356")

    Jump("loc_24EE")

    label("loc_135B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_14FE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_148C")

    #C0035
    ChrTalk(
        0xFE,
        (
            "３階の人、最近部屋に\x01",
            "子供を泊めているみたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xFE,
        (
            "３階の人には会った事が無いけど、\x01",
            "その子は時々見かけるわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        (
            "帽子を被った１３、４歳くらいの\x01",
            "ちょっと美形な子なのよね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    #C0038
    ChrTalk(
        0xFE,
        (
            "…………あら？\x01",
            "そういえばあの子、前にどこかで\x01",
            "見たような気がするけど……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_14F9")

    label("loc_148C")


    #C0039
    ChrTalk(
        0xFE,
        (
            "ん～、あの子どこかで\x01",
            "見た事がある気が……\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xFE,
        (
            "……ま、いいわ。\x01",
            "管理人が詮索するのも\x01",
            "ヤボってものよね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14F9")

    Jump("loc_24EE")

    label("loc_14FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_16D2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15D1")

    #C0041
    ChrTalk(
        0xFE,
        "くぅ～……っ！！\x02",
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xFE,
        "イリア様、素晴らしかったわ！\x02",
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xFE,
        (
            "それに……あの競演の\x01",
            "《月の姫》役の子も凄かったわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xFE,
        (
            "新人アーティストって聞いてるけど\x01",
            "一気にファンになっちゃったわ！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_16CD")

    label("loc_15D1")


    #C0045
    ChrTalk(
        0xFE,
        (
            "それにしても……イリア様って\x01",
            "どこに住んでらっしゃるのかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xFE,
        (
            "住所さえ判明すれば\x01",
            "私は地の果てまで追っかけをするわよ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBF, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_16CD")
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0047
    ChrTalk(
        0x101,
        (
            "#0005F（イリアさんのこと、\x01",
            "  気付いてないんだ……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16CD")

    Jump("loc_24EE")

    label("loc_16D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_16E0")
    Jump("loc_24EE")

    label("loc_16E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_17BE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_174E")

    #C0048
    ChrTalk(
        0xFE,
        (
            "最近のパレードって\x01",
            "導力車が走るのねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xFE,
        "世の中ハイカラになったものだわ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_17B9")

    label("loc_174E")


    #C0050
    ChrTalk(
        0xFE,
        (
            "私の小さい頃はパレードって言えば\x01",
            "山車#4Rだ し#だったのにね。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xFE,
        (
            "……何だか\x01",
            "歳を感じてムカつくわね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17B9")

    Jump("loc_24EE")

    label("loc_17BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_18EC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1871")

    #C0052
    ChrTalk(
        0xFE,
        (
            "今日は住人の皆さんも\x01",
            "ほとんど出払ってるみたいねえ……\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xFE,
        "まあいいわ、その方が好都合よ。\x02",
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xFE,
        (
            "うっかり新作公演の\x01",
            "感想でも聞いちゃったら事だもの。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_18E7")

    label("loc_1871")


    #C0055
    ChrTalk(
        0xFE,
        (
            "私、明日は\x01",
            "アルカンシェルの新作を見に行くの。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xFE,
        (
            "それまでネタバレは絶対禁止よ。\x01",
            "まっさらな状態で楽しみたいの！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18E7")

    Jump("loc_24EE")

    label("loc_18EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_19CA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_198E")

    #C0057
    ChrTalk(
        0xFE,
        (
            "人が浮かれていようが、\x01",
            "私は管理人としての仕事を全うするわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xFE,
        (
            "最終日はお休みを取って\x01",
            "アルカンシェルの公演を\x01",
            "見に行くんだもの。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_19C5")

    label("loc_198E")


    #C0059
    ChrTalk(
        0xFE,
        (
            "さっさっ、掃除掃除……\x01",
            "これも最終日までの辛抱ね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19C5")

    Jump("loc_24EE")

    label("loc_19CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1B0C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AB3")

    #C0060
    ChrTalk(
        0xFE,
        (
            "いよいよアルカンシェルの\x01",
            "新作が公開されたわね……\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xFE,
        (
            "私のゲットしたチケット、\x01",
            "記念祭の最終日なの。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xFE,
        (
            "だからそれまで\x01",
            "誰とも口を利かないわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xFE,
        (
            "だってお話の筋書きを\x01",
            "聞いちゃったら魅力半減だもの。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1B07")

    label("loc_1AB3")

    OP_63(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0064
    ChrTalk(
        0xFE,
        (
            "おっと、それ以上話しかけないで！\x01",
            "ネタバレ厳禁よっ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B07")

    Jump("loc_24EE")

    label("loc_1B0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_1CCA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C26")

    #C0065
    ChrTalk(
        0xFE,
        (
            "ドキドキ、ドキドキ……\x01",
            "ああ、今から胸が高鳴るわ……\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xFE,
        (
            "もうすぐ記念祭……\x01",
            "そしてイリア様の輝かしいお姿……！\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xFE,
        (
            "今年も舞台で会えますわね、\x01",
            "イリア様……㈱㈱㈱\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xFE,
        (
            "…………あら、何か用かしら？\x01",
            "用事なら、この雇われ管理人サミィに\x01",
            "言ってちょうだい。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1CC5")

    label("loc_1C26")


    #C0069
    ChrTalk(
        0xFE,
        (
            "それにしても、３階に来ている人たち\x01",
            "まだ居座ってるのかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xFE,
        (
            "３階を借りている人なら今日も留守よ。\x01",
            "私も会った事がないくらい\x01",
            "お留守ばっかりなんだから。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CC5")

    Jump("loc_24EE")

    label("loc_1CCA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1E31")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DA1")

    #C0071
    ChrTalk(
        0xFE,
        (
            "３階の部屋に\x01",
            "朝からお客さんが来ているの。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xFE,
        (
            "……でも、何だか変な感じよ。\x01",
            "エラソーな雰囲気で、管理人の私も\x01",
            "部屋に近づけさせないの。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xFE,
        (
            "あれってもしかして\x01",
            "警察の人じゃないかしら。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1E2C")

    label("loc_1DA1")


    #C0074
    ChrTalk(
        0xFE,
        (
            "……実は私、前から\x01",
            "３階の人って怪しいんじゃないかと\x01",
            "思ってたのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xFE,
        (
            "だって日中はいつも留守で、\x01",
            "一度も顔を見たことないんだもの。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E2C")

    Jump("loc_24EE")

    label("loc_1E31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_1FA9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F0F")

    #C0076
    ChrTalk(
        0xFE,
        "３階の人、今日も留守なのよねぇ。\x02",
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xFE,
        (
            "まあいいか……\x01",
            "明日は掃除に入らせてもらう日だし。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xFE,
        (
            "３階の人には、月に一度\x01",
            "部屋を掃除するように頼まれているのよ。\x01",
            "高級アパートならではのサービスね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1FA4")

    label("loc_1F0F")


    #C0079
    ChrTalk(
        0xFE,
        (
            "３階の人に関して\x01",
            "私が知っている事は少ないわ……\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xFE,
        (
            "とりあえず、\x01",
            "若い女の人であることは確かね。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xFE,
        (
            "だっていつも\x01",
            "下着出しっぱなしなんだもの。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FA4")

    Jump("loc_24EE")

    label("loc_1FA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2092")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2044")

    #C0082
    ChrTalk(
        0xFE,
        (
            "アルカンシェルのチケット、\x01",
            "何とか来月分をゲットしたわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xFE,
        "Ｂ席だけどね！\x02",
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xFE,
        (
            "んもうすっごい\x01",
            "取り合いだったんだから～。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_208D")

    label("loc_2044")


    #C0085
    ChrTalk(
        0xFE,
        (
            "でもこれでイリア様に会えるわ～。\x01",
            "うふふ、今から待ちきれないかも～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_208D")

    Jump("loc_24EE")

    label("loc_2092")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_20F3")

    #C0086
    ChrTalk(
        0xFE,
        (
            "３階の人、今日も\x01",
            "朝早くから出かけたみたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0xFE,
        "ホントに何者なのかしら～。\x02",
    )

    CloseMessageWindow()
    Jump("loc_24EE")

    label("loc_20F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_2214")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21C5")

    #C0088
    ChrTalk(
        0xFE,
        (
            "私はゴミ出しにはうるさいの。\x01",
            "ちゃんと分別して出さなくちゃね。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xFE,
        "でも……市の回収って適当みたい。\x02",
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0xFE,
        (
            "時々分別したゴミを\x01",
            "一緒にして持っていっちゃうのよ。\x01",
            "あったま来ちゃうわ！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_220F")

    label("loc_21C5")


    #C0091
    ChrTalk(
        0xFE,
        "私はゴミ出しにはうるさいの。\x02",
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0xFE,
        "あなた達もちゃんと分別しなさいよ？\x02",
    )

    CloseMessageWindow()

    label("loc_220F")

    Jump("loc_24EE")

    label("loc_2214")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_234E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22D1")

    #C0093
    ChrTalk(
        0xFE,
        "ねぇねぇ、聞いた？\x02",
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xFE,
        (
            "もうすぐアルカンシェルの\x01",
            "新作公演チケットが発売されるそうよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xFE,
        (
            "待ちに待ったイリア様の勇姿……㈱\x01",
            "うーん、絶対手に入れなくっちゃ！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2349")

    label("loc_22D1")


    #C0096
    ChrTalk(
        0xFE,
        (
            "もうすぐアルカンシェルの\x01",
            "新作公演チケットが発売されるの。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0xFE,
        (
            "イリアに会うためなら\x01",
            "徹夜して並んででも買うわよ～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2349")

    Jump("loc_24EE")

    label("loc_234E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_2462")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2416")

    #C0098
    ChrTalk(
        0xFE,
        "３階の人はいつもお出かけ中なの。\x02",
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xFE,
        (
            "朝早くに出勤して\x01",
            "夜遅くに帰ってくるみたいで……\x01",
            "私も一度も見かけた事がないわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xFE,
        (
            "ちゃんと毎月の\x01",
            "ミラの振込みはあるんだけどね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_245D")

    label("loc_2416")


    #C0101
    ChrTalk(
        0xFE,
        (
            "３階の人はいつもお出かけ中なのよ。\x01",
            "私も一度も見かけた事がないわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_245D")

    Jump("loc_24EE")

    label("loc_2462")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_24EE")

    #C0102
    ChrTalk(
        0xFE,
        (
            "あらこんにちは。\x01",
            "雇われ管理人のサミィよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xFE,
        (
            "どなたかにご用？\x01",
            "ルーヴィックさんなら１階、\x01",
            "キンドールさんなら２階のお部屋よ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24EE")

    TalkEnd(0xFE)
    Return()

    # Function_8_B4F end

    def Function_9_24F2(): pass

    label("Function_9_24F2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_2503")
    Jump("loc_262F")

    label("loc_2503")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2511")
    Jump("loc_262F")

    label("loc_2511")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_251F")
    Jump("loc_262F")

    label("loc_251F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_252D")
    Jump("loc_262F")

    label("loc_252D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_253B")
    Jump("loc_262F")

    label("loc_253B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2549")
    Jump("loc_262F")

    label("loc_2549")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_25A8")

    #C0104
    ChrTalk(
        0xFE,
        "……なかなか見事だった。\x02",
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xFE,
        (
            "今年のパレードは\x01",
            "賞賛されてしかるべきだろう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_262F")

    label("loc_25A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_262F")

    #C0106
    ChrTalk(
        0xFE,
        (
            "手持ちの仕事が片付いたのでね、\x01",
            "妻とパレードを見に行くのだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xFE,
        (
            "クロスベルのための祭りだ。\x01",
            "私達も少しは楽しまないとな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_262F")

    TalkEnd(0xFE)
    Return()

    # Function_9_24F2 end

    def Function_10_2633(): pass

    label("Function_10_2633")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_26C7")
    Jump("loc_2711")

    label("loc_26C7")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_26E7")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2711")

    label("loc_26E7")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2707")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2711")

    label("loc_2707")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2711")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x3)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2B6B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x5)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AB2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27C0")

    #C0108
    ChrTalk(
        0x101,
        (
            "#0001F（よし、聞き込みをしてみよう。）\x02\x03",

            "#0000Fすみません、\x01",
            "少しよろしいですか？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27C0")

    SetScenarioFlags(0x1, 2)
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0109
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイド達はストーカーについて\x01",
            "心当たりを尋ねてみた。\x02",
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
            "ストーカーか……\x01",
            "そういった噂も聞いている。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0xFE,
        (
            "私は普段は家にいるから\x01",
            "姿を見た事はないが、\x01",
            "妙な物音を聞いた事があるな。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0xFE,
        (
            "上の階から\x01",
            "ゴソゴソと音がするのだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xFE,
        (
            "たしか日中は\x01",
            "３階の人は留守なはずなんだが。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x101,
        "#0000Fそれはいつ頃からですか？\x02",
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0xFE,
        "記念祭に入ってすぐくらいだよ。\x02",
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0xFE,
        "ここ２、３日、といった所だな。\x02",
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x102,
        (
            "#0108F（イリアさんの部屋に入って\x01",
            "  何をしていたのかしら。）\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x101,
        (
            "#0001F（……そうだな。\x01",
            "  部屋に荒らされた形跡は\x01",
            "  無かったと思うけど……）\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x1D, 0x1, 0x5)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x5)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x6)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x7)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2AAD")

    #C0119
    ChrTalk(
        0x101,
        (
            "#0000Fよし、下調べはこんな所だな。\x02\x03",

            "一旦イリアさんの部屋に戻って\x01",
            "整理してみよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x104,
        "#0300F了解、そろそろ作戦を考えるか！\x02",
    )

    CloseMessageWindow()
    ModifyEventFlags(1, 0, 0x80)
    OP_29(0x1D, 0x1, 0x9)

    label("loc_2AAD")

    Jump("loc_2B66")

    label("loc_2AB2")


    #C0121
    ChrTalk(
        0xFE,
        (
            "上の階から妙な物音がするんだ。\x01",
            "ここ２、３日のことだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0xFE,
        (
            "てっきり上の階の人が\x01",
            "記念祭で在宅しているのかと\x01",
            "思っていたんだが。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0xFE,
        (
            "もしや……あれが\x01",
            "ストーカーだったのかな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B66")

    Jump("loc_3AA3")

    label("loc_2B6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_2C0A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BD0")

    #C0124
    ChrTalk(
        0xFE,
        "……クロスベルの議員どもめ……\x02",
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0xFE,
        "けしからん、まったく許せないな！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2C05")

    label("loc_2BD0")


    #C0126
    ChrTalk(
        0xFE,
        (
            "無能な議員など、\x01",
            "全員首にしてしまえばいいのだ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C05")

    Jump("loc_3AA3")

    label("loc_2C0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2C9D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C7C")

    #C0127
    ChrTalk(
        0xFE,
        "くそっ、凝り過ぎたデザインだと……？\x02",
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0xFE,
        (
            "この芸術性が\x01",
            "何故分からないんだっ……！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2C98")

    label("loc_2C7C")


    #C0129
    ChrTalk(
        0xFE,
        "帝国派議員どもめ……！\x02",
    )

    CloseMessageWindow()

    label("loc_2C98")

    Jump("loc_3AA3")

    label("loc_2C9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_2DC6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D59")

    #C0130
    ChrTalk(
        0xFE,
        (
            "新しい市庁舎ビルの建設は\x01",
            "目下予算が凍結されているのだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xFE,
        (
            "……工事の発注をめぐって\x01",
            "議員たちがもめていてな……\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xFE,
        (
            "本年度こそ\x01",
            "再開できればいいんだが……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2DC1")

    label("loc_2D59")


    #C0133
    ChrTalk(
        0xFE,
        (
            "あのビルには私にも\x01",
            "拘りがあるのだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xFE,
        (
            "あの件の予算審議は今日の予定……\x01",
            "こちらまで緊張するな……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DC1")

    Jump("loc_3AA3")

    label("loc_2DC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2EC0")
    SetChrSubChip(0xFE, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E49")

    #C0135
    ChrTalk(
        0xFE,
        (
            "この建物の完成を\x01",
            "市長選までに、か……\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xFE,
        (
            "最近のクライアントは\x01",
            "随分と無茶を言ってくれるな……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2EBB")

    label("loc_2E49")


    #C0137
    ChrTalk(
        0xFE,
        (
            "確かに４ヵ月後の市長選は\x01",
            "落成式典に絶好のタイミングだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xFE,
        (
            "さすがに無理だな。\x01",
            "文句を言ってやらねば……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EBB")

    Jump("loc_3AA3")

    label("loc_2EC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_2FC2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F66")

    #C0139
    ChrTalk(
        0xFE,
        (
            "記念祭からこちら\x01",
            "仕事が続々と舞い込んでいるのだ……\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xFE,
        (
            "私の設計したビルを\x01",
            "使ってくれるのは嬉しいが、\x01",
            "これでは忙しくて敵わないな……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2FBD")

    label("loc_2F66")


    #C0141
    ChrTalk(
        0xFE,
        "私は絶対に妥協などしない。\x02",
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xFE,
        (
            "悪いが……これ以上の\x01",
            "順番待ちは断らせてもらうぞ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FBD")

    Jump("loc_3AA3")

    label("loc_2FC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_30BA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3078")

    #C0143
    ChrTalk(
        0xFE,
        (
            "おっと、邪魔を\x01",
            "しないでくれたまえよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0xFE,
        (
            "今日は残りの仕事を\x01",
            "片付けてしまうつもりなんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0xFE,
        (
            "……手早く済ませれば\x01",
            "夕方には時間が作れそうなのでな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_30B5")

    label("loc_3078")


    #C0146
    ChrTalk(
        0xFE,
        (
            "……仕事を片付けて、夕方からは\x01",
            "妻に付き合うとしようか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30B5")

    Jump("loc_3AA3")

    label("loc_30BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_3129")

    #C0147
    ChrTalk(
        0xFE,
        "おや、何か用事かね？\x02",
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0xFE,
        (
            "生憎設計の仕事が残っていてね、\x01",
            "あまり構っている余裕が無いんだが。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AA3")

    label("loc_3129")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_3137")
    Jump("loc_3AA3")

    label("loc_3137")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_3145")
    Jump("loc_3AA3")

    label("loc_3145")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_31A4")

    #C0149
    ChrTalk(
        0xFE,
        "まだ仕事が残っているんだ。\x02",
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xFE,
        (
            "……妻には悪いが、\x01",
            "今は手が離せないのだよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AA3")

    label("loc_31A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_31F6")

    #C0151
    ChrTalk(
        0xFE,
        "ううむ、表が騒がしいな……\x02",
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xFE,
        "これでは仕事に集中できないぞ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3AA3")

    label("loc_31F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_326A")

    #C0153
    ChrTalk(
        0xFE,
        (
            "よし、あと一息で\x01",
            "このビルの設計も完成だ……\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0xFE,
        (
            "一日でも早くクライアントに\x01",
            "お見せしなくてはな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AA3")

    label("loc_326A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3320")

    #C0155
    ChrTalk(
        0xFE,
        (
            "私の父も祖父も\x01",
            "有名な建築家だったのだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xFE,
        (
            "クロスベル市庁舎は\x01",
            "私の祖父の設計だよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xFE,
        (
            "そういえばあの建物も\x01",
            "もう築６０年になるんだな……\x01",
            "感慨深いものがあるよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AA3")

    label("loc_3320")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_344A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33E7")

    #C0158
    ChrTalk(
        0xFE,
        (
            "マフィア・ルバーチェの連中は\x01",
            "地上げもやっていると聞く……\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xFE,
        (
            "地上げとは、住民を強引に立ち退かせて\x01",
            "建設用地を違法に確保する行為だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0xFE,
        "まったくタチの悪い連中だよ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3445")

    label("loc_33E7")


    #C0161
    ChrTalk(
        0xFE,
        (
            "ルバーチェの連中は\x01",
            "地上げもやっていると聞く。\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0xFE,
        (
            "警察も何とか\x01",
            "取り締まれないものかな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3445")

    Jump("loc_3AA3")

    label("loc_344A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_35A5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_353E")

    #C0163
    ChrTalk(
        0xFE,
        (
            "来月に向けて、クロスベル中のビル建設が\x01",
            "急ピッチで進められているのだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xFE,
        (
            "なにせ来月は７０周年の創立記念祭……\x01",
            "各国からも大いに注目が集まるときだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0xFE,
        (
            "ビルのオーナーとしても\x01",
            "最高のアピールタイミングだからな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_35A0")

    label("loc_353E")


    #C0166
    ChrTalk(
        0xFE,
        (
            "来月には多くのビルが\x01",
            "落成式典を迎えるだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0xFE,
        (
            "まさに繁栄ここに\x01",
            "極まれりといった感だな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35A0")

    Jump("loc_3AA3")

    label("loc_35A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_35B3")
    Jump("loc_3AA3")

    label("loc_35B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_371F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3696")

    #C0168
    ChrTalk(
        0xFE,
        (
            "ミシュラムにテーマパークが\x01",
            "開園したのは知っているだろう？\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0xFE,
        (
            "あのテーマパーク本体は\x01",
            "ＩＢＣ事業部が手がけていてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0xFE,
        (
            "最新の建築技術なども\x01",
            "取り入れているらしい……\x01",
            "私も一度見てみたい所だな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_371A")

    label("loc_3696")


    #C0171
    ChrTalk(
        0xFE,
        (
            "私もいくつかホテルを設計したのだが、\x01",
            "まだテーマパークには行った事がない。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0xFE,
        (
            "うむ……一度彼らの\x01",
            "仕事振りを見てみたい所だな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_371A")

    Jump("loc_3AA3")

    label("loc_371F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_37B3")

    #C0173
    ChrTalk(
        0xFE,
        (
            "ふう、設計に取り組んでいたら\x01",
            "徹夜になってしまったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0xFE,
        (
            "しかしこれなら先方も満足するだろう。\x01",
            "ふふ、明日の説明会が楽しみだよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AA3")

    label("loc_37B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_3913")
    SetChrSubChip(0xFE, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38BB")

    #C0175
    ChrTalk(
        0xFE,
        (
            "しかし……あの連中には困った物だ。\x01",
            "私が引いた設計図を\x01",
            "ことごとく無視しおって……\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0xFE,
        (
            "だいたい新市庁舎ビルのデザインを\x01",
            "発注したのはそちらではないか！\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0xFE,
        (
            "抗議してやる……\x01",
            "勝手にデザインを改変するなど\x01",
            "……私は絶対に認めないぞ！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_390E")

    label("loc_38BB")


    #C0178
    ChrTalk(
        0xFE,
        (
            "くそっ、これのどこが\x01",
            "改善案だというのだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0xFE,
        "くだらない、全くくだらないっ！\x02",
    )

    CloseMessageWindow()

    label("loc_390E")

    Jump("loc_3AA3")

    label("loc_3913")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_3AA3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A23")

    #C0180
    ChrTalk(
        0xFE,
        (
            "建設中の新市庁舎ビルは\x01",
            "地上４０階建てという超高層建造物だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0xFE,
        (
            "これまでにない斬新なアイデアを\x01",
            "いくつも盛り込んだ、\x01",
            "まさに時代の最先端を行く建物だな。\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xFE,
        (
            "私は外観やオフィススペースの\x01",
            "デザインを手がけたのだよ。\x01",
            "ふふ、完成が待ち遠しいな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3AA3")

    label("loc_3A23")


    #C0183
    ChrTalk(
        0xFE,
        (
            "新市庁舎ビルは地上４０階建ての\x01",
            "超高層建造物なのだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0xFE,
        (
            "あのデザインは中々の大仕事だった……\x01",
            "私も完成する日が楽しみだよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3AA3")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_10_2633 end

    def Function_11_3AAB(): pass

    label("Function_11_3AAB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x3)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3E12")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x6)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DB2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B38")

    #C0185
    ChrTalk(
        0x101,
        (
            "#0001F（よし、聞き込みをしてみよう。）\x02\x03",

            "#0000Fすみません、\x01",
            "少しよろしいですか？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B38")

    SetScenarioFlags(0x1, 2)
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0186
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイド達はストーカーについて\x01",
            "心当たりを尋ねてみた。\x02",
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
            "ストーカーですか？\x01",
            "怖いですね……\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0xFE,
        (
            "でも私は見かけた事はありません。\x01",
            "よくお買い物なんかには\x01",
            "出かけるのですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0x103,
        (
            "#0200Fお買い物……\x01",
            "時間帯はお昼前や夕方ですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0xFE,
        (
            "ええ、そうですね。\x01",
            "大体いつも決まった時間です。\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0x102,
        "#0105F（丁度人通りの多い時間帯ね。）\x02",
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0x101,
        (
            "#0001F（ああ、その頃には\x01",
            "  現れないらしい……）\x02\x03",

            "（用心深いやつみたいだな。）\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x1D, 0x1, 0x6)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x5)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x6)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x7)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3DAD")

    #C0193
    ChrTalk(
        0x101,
        (
            "#0000Fよし、下調べはこんな所だな。\x02\x03",

            "一旦イリアさんの部屋に戻って\x01",
            "整理してみよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0x104,
        "#0300F了解、そろそろ作戦を考えるか！\x02",
    )

    CloseMessageWindow()
    ModifyEventFlags(1, 0, 0x80)
    OP_29(0x1D, 0x1, 0x9)

    label("loc_3DAD")

    Jump("loc_3E0D")

    label("loc_3DB2")


    #C0195
    ChrTalk(
        0xFE,
        "ストーカーなんて怖いですね。\x02",
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0xFE,
        (
            "私がお買い物にいく時間には\x01",
            "見た事はないですけど……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E0D")

    Jump("loc_4A4F")

    label("loc_3E12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_3E75")

    #C0197
    ChrTalk(
        0xFE,
        "今日は紅茶を淹れてあげましょう。\x02",
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0xFE,
        (
            "少しは落ち着いて\x01",
            "くれるかもしれませんし。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A4F")

    label("loc_3E75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3F73")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F35")

    #C0199
    ChrTalk(
        0xFE,
        (
            "新しい市庁舎ビルの予算は\x01",
            "結局再開されなかったみたいです。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0xFE,
        (
            "議員の質疑応答で\x01",
            "費用が無駄にかかりすぎると\x01",
            "取りざたされてしまって……\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0xFE,
        "主人は怒り心頭です。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3F6E")

    label("loc_3F35")


    #C0202
    ChrTalk(
        0xFE,
        (
            "困りましたね……\x01",
            "主人は仕事に妥協しない人なので……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F6E")

    Jump("loc_4A4F")

    label("loc_3F73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_3F81")
    Jump("loc_4A4F")

    label("loc_3F81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_3FD8")

    #C0203
    ChrTalk(
        0xFE,
        (
            "最近お仕事が\x01",
            "沢山舞い込んでいるんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0xFE,
        "書類の整理も大変です。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4A4F")

    label("loc_3FD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_40C9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4059")

    #C0205
    ChrTalk(
        0xFE,
        (
            "主人は最近仕事が\x01",
            "とても忙しいらしいんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0xFE,
        (
            "……会話が減ってしまったので\x01",
            "少し寂しいですね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_40C4")

    label("loc_4059")


    #C0207
    ChrTalk(
        0xFE,
        "あっと、こんな事じゃいけませんね。\x02",
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0xFE,
        (
            "主人の仕事がはかどるように\x01",
            "熱い紅茶でも淹れてあげましょうか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_40C4")

    Jump("loc_4A4F")

    label("loc_40C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_4145")

    #C0209
    ChrTalk(
        0xFE,
        (
            "今夜のお料理はとびきりの\x01",
            "ご馳走にするつもりなんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0xFE,
        (
            "ふふ、張り切って\x01",
            "支度をしないといけませんね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A4F")

    label("loc_4145")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_420F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_41A4")

    #C0211
    ChrTalk(
        0xFE,
        "小さな男の子……ですか？\x02",
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0xFE,
        "さあ、心当たりはありませんね……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_420A")

    label("loc_41A4")


    #C0213
    ChrTalk(
        0xFE,
        (
            "私たちもパレードは\x01",
            "見ていましたけれど……\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0xFE,
        (
            "ごめんなさい、今ひとつ\x01",
            "心当たりはないみたいです。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_420A")

    Jump("loc_4A4F")

    label("loc_420F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_4270")

    #C0215
    ChrTalk(
        0xFE,
        (
            "ふふ、今年のパレードは\x01",
            "とっても楽しかったです。\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0xFE,
        "いい思い出ができました。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4A4F")

    label("loc_4270")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_430D")
    OP_4B(0x9, 0xFF)
    TurnDirection(0xB, 0x9, 0)

    #C0217
    ChrTalk(
        0x9,
        "コホン、それでは行こうか。\x02",
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0x9,
        (
            "パレードを見逃しては\x01",
            "取引先との話題にも事欠くからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0xFE,
        (
            "ふふ……\x01",
            "ええ、行きましょうか。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    Jump("loc_4A4F")

    label("loc_430D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_4372")

    #C0220
    ChrTalk(
        0xFE,
        "主人は仕事人間なの。\x02",
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0xFE,
        (
            "私は構わないですけど、\x01",
            "たまには息抜きして欲しいですね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A4F")

    label("loc_4372")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_43D9")

    #C0222
    ChrTalk(
        0xFE,
        (
            "あら、いらっしゃい。\x01",
            "こちらキンドール設計事務所です。\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0xFE,
        "今日も営業していますよ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4A4F")

    label("loc_43D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_43E7")
    Jump("loc_4A4F")

    label("loc_43E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_4522")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_44C6")

    #C0224
    ChrTalk(
        0xFE,
        (
            "ＩＢＣグループの建設会社は\x01",
            "うちのお馴染みさんなんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0xFE,
        (
            "現場主任さんは\x01",
            "何度も遊びに来てくださって、\x01",
            "主人とは親友の仲なんですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0xFE,
        (
            "でもお酒の付き合いも\x01",
            "多いですから、体が心配ですね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_451D")

    label("loc_44C6")


    #C0227
    ChrTalk(
        0xFE,
        (
            "建設会社の方とは\x01",
            "お酒の付き合いが多いんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0xFE,
        "体には気をつけて欲しいですね。\x02",
    )

    CloseMessageWindow()

    label("loc_451D")

    Jump("loc_4A4F")

    label("loc_4522")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_4592")

    #C0229
    ChrTalk(
        0xFE,
        (
            "今日は主人の好物、\x01",
            "ビーフシチューの予定なんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0xFE,
        (
            "ふふ、下ごしらえを\x01",
            "しておかなくちゃ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A4F")

    label("loc_4592")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_4623")

    #C0231
    ChrTalk(
        0xFE,
        (
            "アルカンシェルのイリアさんって\x01",
            "とても人気だそうですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0xFE,
        (
            "サミィさんが\x01",
            "いつもお話しているから\x01",
            "すっかり覚えてしまいました。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A4F")

    label("loc_4623")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_4728")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_46EE")

    #C0233
    ChrTalk(
        0xFE,
        (
            "主人が居ない間に\x01",
            "掃除をしておかないといけません。\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0xFE,
        (
            "主人は……今ごろ\x01",
            "中央広場のレストランで\x01",
            "打ち合わせをしている頃かしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0xFE,
        (
            "ふふ……気難しい上に\x01",
            "忙しい人なんです。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4723")

    label("loc_46EE")


    #C0236
    ChrTalk(
        0xFE,
        (
            "さて、鬼の居ない間に\x01",
            "掃除をしておかなくっちゃ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4723")

    Jump("loc_4A4F")

    label("loc_4728")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_4736")
    Jump("loc_4A4F")

    label("loc_4736")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_4837")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_47F1")

    #C0237
    ChrTalk(
        0xFE,
        (
            "あの人ったらまた徹夜したんですね。\x01",
            "新しいビルの設計になると\x01",
            "いつもこうなんだから……\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0xFE,
        (
            "ふふ、困った人。\x01",
            "仕方がないので熱い紅茶でも\x01",
            "淹れてあげましょう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4832")

    label("loc_47F1")


    #C0239
    ChrTalk(
        0xFE,
        (
            "主人は大の紅茶好きなの。\x01",
            "徹夜明けにはいつもねだるんですよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4832")

    Jump("loc_4A4F")

    label("loc_4837")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_492C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48D7")

    #C0240
    ChrTalk(
        0xFE,
        (
            "主人は集中すると\x01",
            "周りの事が見えなくなります。\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0xFE,
        (
            "ですから突然大声を\x01",
            "上げる事もありますけど……\x01",
            "どうか気を悪くなさらないでね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4927")

    label("loc_48D7")


    #C0242
    ChrTalk(
        0xFE,
        (
            "主人は集中すると\x01",
            "周りの事が見えなくなるの。\x01",
            "どうか気を悪くなさらないでね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4927")

    Jump("loc_4A4F")

    label("loc_492C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_4A4F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A01")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0243
    ChrTalk(
        0xFE,
        (
            "あ……すみません。\x01",
            "お料理をしていたもので。\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0xFE,
        (
            "こちらキンドール設計事務所です。\x01",
            "ご依頼でしたら\x01",
            "主人に仰ってくださいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0xFE,
        "丁度手が空いているみたいですし。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4A4F")

    label("loc_4A01")


    #C0246
    ChrTalk(
        0xFE,
        (
            "こちらキンドール設計事務所です。\x01",
            "ご依頼でしたら\x01",
            "主人に仰ってくださいね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A4F")

    TalkEnd(0xFE)
    Return()

    # Function_11_3AAB end

    def Function_12_4A53(): pass

    label("Function_12_4A53")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x3)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_50E0")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x7)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_505E")
    OP_4B(0xC, 0xFF)
    OP_4B(0xE, 0xFF)

    #C0247
    ChrTalk(
        0xC,
        (
            "やれやれ、昼くらい\x01",
            "外食にしたいものじゃが。\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0xE,
        (
            "朝に作り置きしてしまったのだから\x01",
            "仕方ないでしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0xE,
        "グダグダ言わないでくださいな。\x02",
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0x101,
        (
            "#0003F（何だか険悪なムードだ……）\x02\x03",

            "#0000Fす、すみません。\x01",
            "少しよろしいですか？\x02",
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
            "ロイド達はストーカーについて\x01",
            "心当たりを尋ねてみた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()

    #C0252
    ChrTalk(
        0xC,
        "ほう、ストーカー？\x02",
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0xC,
        (
            "ほほほ、それは怖いな。\x01",
            "警察に相談せねばな。\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0xE,
        (
            "遊撃士の方がいいんじゃないかしら？\x01",
            "警察は腰が重いもの。\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x101,
        (
            "#0000Fえ、ええと……\x01",
            "お心当たりはないんですね？\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0xE,
        "ええ、そうねぇ……\x02",
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0xE,
        (
            "私はよく玄関のソファーで\x01",
            "寛いでいるけれど。\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0xE,
        (
            "怪しい人間なんて\x01",
            "見かけた事はないわね。\x01",
            "何かの気のせいじゃないかしら。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E36")
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
            "#0003F（玄関から入ってくるのを\x01",
            "  見たことがない……）\x02\x03",

            "（一体どういうことだろう。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4F88")

    label("loc_4E36")

    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    #C0261
    ChrTalk(
        0x104,
        "#0305F……そうきたか………！\x02",
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0x102,
        (
            "#0103F（玄関から入ってくるのを\x01",
            "  見たことがない……）\x02\x03",

            "（やっぱりあのルートを\x01",
            "  使っているのかしら。）\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0x103,
        (
            "#0200F（裏口のルートですね。\x01",
            "  可能性は高そうです。）\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0x101,
        (
            "#0001F（……作戦を立てるときの\x01",
            "  要になりそうだな。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xBD, 4)

    label("loc_4F88")

    OP_29(0x1D, 0x1, 0x7)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x5)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x6)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x7)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5047")

    #C0265
    ChrTalk(
        0x101,
        (
            "#0000Fよし、下調べはこんな所だな。\x02\x03",

            "一旦イリアさんの部屋に戻って\x01",
            "整理してみよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0x104,
        "#0300F了解、そろそろ作戦を考えるか！\x02",
    )

    CloseMessageWindow()
    ModifyEventFlags(1, 0, 0x80)
    OP_29(0x1D, 0x1, 0x9)

    label("loc_5047")

    OP_4C(0xC, 0xFF)
    OP_4C(0xE, 0xFF)
    ClearChrFlags(0xC, 0x10)
    ClearChrFlags(0xE, 0x10)
    Jump("loc_50DB")

    label("loc_505E")


    #C0267
    ChrTalk(
        0xFE,
        "ほほ、ストーカーとは怖いのう。\x02",
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0xFE,
        "早く警察に相談せんとな。\x02",
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0x101,
        (
            "#0001F（この人はまるで\x01",
            "  心当たりが無いみたいだ……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_50DB")

    Jump("loc_5BC7")

    label("loc_50E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_50EE")
    Jump("loc_5BC7")

    label("loc_50EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_51E7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_51A1")

    #C0270
    ChrTalk(
        0xFE,
        (
            "裏通りにあるアンティークショップで\x01",
            "よい品を見つけたんじゃよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0xFE,
        "確かそろそろ結婚記念日だったはず。\x02",
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0xFE,
        (
            "ほほほ、婆さんの\x01",
            "ご機嫌も取れたかのう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_51E2")

    label("loc_51A1")


    #C0273
    ChrTalk(
        0xFE,
        (
            "家内はあの通りの性格じゃから\x01",
            "機嫌をとるのも大変なんじゃよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_51E2")

    Jump("loc_5BC7")

    label("loc_51E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_52FE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_52C0")

    #C0274
    ChrTalk(
        0xFE,
        (
            "こうして静かに暮らしていけるのも\x01",
            "わしが現役時代に働いたお陰。\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0xFE,
        (
            "リッチな議員年金の\x01",
            "お陰なんじゃよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0xFE,
        (
            "しかし婆さんは頭が固い。\x01",
            "アレを買おうとしても\x01",
            "うんとは言わんじゃろうなぁ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_52F9")

    label("loc_52C0")


    #C0277
    ChrTalk(
        0xFE,
        (
            "ふうむ、困ったのう。\x01",
            "婆さんはあの通り頑固じゃし……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_52F9")

    Jump("loc_5BC7")

    label("loc_52FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_53E6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_53AE")

    #C0278
    ChrTalk(
        0xFE,
        (
            "家内が内装をいじるのは\x01",
            "やめろと言うんじゃよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0xFE,
        (
            "お前が面倒がるから\x01",
            "代わりにわしが\x01",
            "やっとるんじゃあないか……\x02",
        )
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0xFE,
        "本当に自分勝手な奴じゃよ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_53E1")

    label("loc_53AE")


    #C0281
    ChrTalk(
        0xFE,
        (
            "フン、家内はズボラな上に\x01",
            "自分勝手な奴じゃよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_53E1")

    Jump("loc_5BC7")

    label("loc_53E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_54DA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_546D")
    TurnDirection(0xFE, 0x153, 0)

    #C0282
    ChrTalk(
        0xFE,
        "おや、可愛らしい女の子じゃないか。\x02",
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0xFE,
        (
            "西通りに越してきたのかね？\x01",
            "まあゆっくりしていきたまえ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_54D5")

    label("loc_546D")


    #C0284
    ChrTalk(
        0xFE,
        (
            "また少し内装を\x01",
            "模様替えしたんじゃよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0xFE,
        (
            "うむ、記念祭明けにふさわしい\x01",
            "明るい色でまとまったのう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_54D5")

    Jump("loc_5BC7")

    label("loc_54DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_54E8")
    Jump("loc_5BC7")

    label("loc_54E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_54F6")
    Jump("loc_5BC7")

    label("loc_54F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_5504")
    Jump("loc_5BC7")

    label("loc_5504")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_5512")
    Jump("loc_5BC7")

    label("loc_5512")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_5520")
    Jump("loc_5BC7")

    label("loc_5520")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_552E")
    Jump("loc_5BC7")

    label("loc_552E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_55C5")

    #C0286
    ChrTalk(
        0xFE,
        (
            "さて、部屋も片付いたし……\x01",
            "お茶でも淹れるとするかのう。\x02",
        )
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0xFE,
        (
            "家内は趣味にふけってばかりじゃ。\x01",
            "わしが気を利かせるしか\x01",
            "ないんじゃよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5BC7")

    label("loc_55C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_5636")

    #C0288
    ChrTalk(
        0xFE,
        (
            "クローゼットの掃除をしておったら\x01",
            "物が落ちてきてなぁ……\x02",
        )
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0xFE,
        "やれやれ、後片付けが大変じゃよ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5BC7")

    label("loc_5636")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_5727")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_56CE")

    #C0290
    ChrTalk(
        0xFE,
        (
            "記念祭が近いと\x01",
            "楽しくなってくるのう……\x02",
        )
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0xFE,
        (
            "わしもじっとはしておれんわい。\x01",
            "カーペットの張替えでも\x01",
            "してしまおうかのう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5722")

    label("loc_56CE")


    #C0292
    ChrTalk(
        0xFE,
        (
            "やはり記念祭は\x01",
            "良い気分で迎えたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0xFE,
        (
            "部屋を掃除するのも\x01",
            "悪くはなかろうて。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5722")

    Jump("loc_5BC7")

    label("loc_5727")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_5866")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_57EB")

    #C0294
    ChrTalk(
        0xFE,
        (
            "調度品の配置を見直した時に、\x01",
            "コンロのサビに気づいてのう。\x02",
        )
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0xFE,
        (
            "元の寸法に合わせて\x01",
            "コンロを買い換えたんじゃよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0xFE,
        (
            "ちょうどよい大きさのものが\x01",
            "あってよかったわい。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5861")

    label("loc_57EB")


    #C0297
    ChrTalk(
        0xFE,
        (
            "ちなみに……店員の説明では\x01",
            "新型で火力倍増だそうじゃよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0xFE,
        (
            "気になるヨゴレもなくなったし\x01",
            "ほほほ、よかったわい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5861")

    Jump("loc_5BC7")

    label("loc_5866")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_5938")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_58EE")

    #C0299
    ChrTalk(
        0xFE,
        (
            "テーブルが部屋の\x01",
            "真ん中からずれておったんじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0xFE,
        (
            "いかんいかん……\x01",
            "きちんと寸法を\x01",
            "計りなおさんとな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5933")

    label("loc_58EE")


    #C0301
    ChrTalk(
        0xFE,
        (
            "テーブルの位置が気になったのでな。\x01",
            "少し移動させておるんじゃよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5933")

    Jump("loc_5BC7")

    label("loc_5938")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_5A11")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_59BD")

    #C0302
    ChrTalk(
        0xFE,
        "おお、今朝はよく晴れたか。\x02",
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0xFE,
        (
            "次の自治州議会も\x01",
            "これくらい爽やかな議論を\x01",
            "見せてくれるとよいがのう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5A0C")

    label("loc_59BD")


    #C0304
    ChrTalk(
        0xFE,
        "さて、植木に水でもやるかのう。\x02",
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0xFE,
        (
            "家内はその辺りが\x01",
            "ズボラじゃからのう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A0C")

    Jump("loc_5BC7")

    label("loc_5A11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_5AFD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5AAF")

    #C0306
    ChrTalk(
        0xFE,
        (
            "家内は朝から晩まで\x01",
            "趣味の手芸をしておってな。\x01",
            "ちっとも家事をせんのじゃよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0xFE,
        (
            "やれやれ、妻ともあろう者が\x01",
            "嘆かわしいのう……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5AF8")

    label("loc_5AAF")


    #C0308
    ChrTalk(
        0xFE,
        (
            "家内は趣味ばかり\x01",
            "しておるんじゃよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0xFE,
        "昔から我が侭なやつじゃて。\x02",
    )

    CloseMessageWindow()

    label("loc_5AF8")

    Jump("loc_5BC7")

    label("loc_5AFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_5BC7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B75")

    #C0310
    ChrTalk(
        0xFE,
        (
            "ふむふむ、気分転換に\x01",
            "高級家具に新調してみたんじゃよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0xFE,
        "レイアウトはこんな所かのう。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5BC7")

    label("loc_5B75")


    #C0312
    ChrTalk(
        0xFE,
        (
            "ウチは内装を\x01",
            "替えてみた所なんじゃよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0xFE,
        (
            "茶でも飲んでいくかの？\x01",
            "ほほほ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5BC7")

    TalkEnd(0xFE)
    Return()

    # Function_12_4A53 end

    def Function_13_5BCB(): pass

    label("Function_13_5BCB")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5C5F")
    Jump("loc_5CA9")

    label("loc_5C5F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5C7F")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5CA9")

    label("loc_5C7F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5C9F")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5CA9")

    label("loc_5C9F")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5CA9")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_5D60")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5CE9")
    Call(0, 14)
    Jump("loc_5D60")

    label("loc_5CE9")


    #C0314
    ChrTalk(
        0xFE,
        (
            "こうして裕福な暮らしが\x01",
            "送れているのも、\x01",
            "全てわしの年金のおかげ……\x02",
        )
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0xFE,
        (
            "婆さんや、それを\x01",
            "忘れてはおるまいな……？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5D60")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_13_5BCB end

    def Function_14_5D68(): pass

    label("Function_14_5D68")

    SetChrSubChip(0xD, 0x0)
    SetChrSubChip(0xF, 0x0)

    #C0316
    ChrTalk(
        0xF,
        (
            "……アナタ、紅茶の\x01",
            "淹れ方は知っていて？\x02",
        )
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0xD,
        (
            "湯に茶葉を浸すのじゃろう？\x01",
            "この通り、できとるじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0xF,
        (
            "マズイわ。\x01",
            "飲めたものじゃないわね。\x02",
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

    # Function_14_5D68 end

    def Function_15_5E2C(): pass

    label("Function_15_5E2C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x3)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6006")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x7)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E63")
    Call(0, 12)
    Return()

    label("loc_5E63")


    #C0320
    ChrTalk(
        0xFE,
        (
            "私はよく玄関のソファーで\x01",
            "寛いでいるのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0xFE,
        (
            "でも怪しい人間なんて\x01",
            "見かけた事はないわ。\x01",
            "何かの気のせいじゃないかしら。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x8)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBD, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6001")

    #C0322
    ChrTalk(
        0x104,
        "#0303F（……なるほど、そうきたか。）\x02",
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0x102,
        (
            "#0100F（玄関から入ってくるのを\x01",
            "  見たことがない……）\x02\x03",

            "（やっぱりあのルートを\x01",
            "  使っているのかしら。）\x02",
        )
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0x103,
        (
            "#0200F（裏口のルートですね。\x01",
            "  可能性は高そうです。）\x02",
        )
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0x101,
        (
            "#0001F（……作戦を立てるときの\x01",
            "  要になりそうだな。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xBD, 4)

    label("loc_6001")

    Jump("loc_6159")

    label("loc_6006")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_6142")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_60DE")

    #C0326
    ChrTalk(
        0xFE,
        (
            "主人は５年ほど前まで\x01",
            "議員をやっていたのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0xFE,
        (
            "他の議員達の応酬を\x01",
            "ぼーっと聞いているだけの\x01",
            "日和見議員ですけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0xFE,
        (
            "まあ……年金を\x01",
            "たっぷり入れる所だけは\x01",
            "褒めてあげてもいいわね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_613D")

    label("loc_60DE")


    #C0329
    ChrTalk(
        0xFE,
        (
            "主人も議員の端くれ。\x01",
            "年金だけは大したものなのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0xFE,
        "それだけは褒めてあげてもいいわね。\x02",
    )

    CloseMessageWindow()

    label("loc_613D")

    Jump("loc_6159")

    label("loc_6142")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_6150")
    Jump("loc_6159")

    label("loc_6150")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_6159")

    label("loc_6159")

    TalkEnd(0xFE)
    Return()

    # Function_15_5E2C end

    def Function_16_615D(): pass

    label("Function_16_615D")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_61F1")
    Jump("loc_623B")

    label("loc_61F1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6211")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_623B")

    label("loc_6211")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6231")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_623B")

    label("loc_6231")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_623B")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_6329")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_62F5")

    #C0331
    ChrTalk(
        0xFE,
        (
            "主人が導力車を\x01",
            "買ったらしいのよ……\x02",
        )
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0xFE,
        "また私に無断で……！\x02",
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0xFE,
        (
            "本当に自分勝手な人ね。\x01",
            "あきれて声も出ないわ……！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_6324")

    label("loc_62F5")


    #C0334
    ChrTalk(
        0xFE,
        (
            "主人の浪費癖には\x01",
            "呆れて声も出ないわ……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6324")

    Jump("loc_6E6D")

    label("loc_6329")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_6445")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_63E8")

    #C0335
    ChrTalk(
        0xFE,
        (
            "主人が結婚記念日に\x01",
            "ペンダントを贈ってくれたの。\x02",
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
            "まあ、あの人にも\x01",
            "良い所はあるのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0xFE,
        "一応私が認めた男なんですから。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_6440")

    label("loc_63E8")


    #C0339
    ChrTalk(
        0xFE,
        (
            "昔はあれで\x01",
            "中々の好青年だったのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0xFE,
        (
            "ふふ、その面影も\x01",
            "少しは残っているようね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6440")

    Jump("loc_6E6D")

    label("loc_6445")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_6513")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_64D7")

    #C0341
    ChrTalk(
        0xFE,
        (
            "主人が何か大きな買い物を\x01",
            "企んでいるらしいのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0xFE,
        (
            "まったく……\x01",
            "今度はシャンデリアでも\x01",
            "買ってくるつもりかしら。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_650E")

    label("loc_64D7")


    #C0343
    ChrTalk(
        0xFE,
        (
            "あの人の下らない\x01",
            "リフォーム癖には困ったものだわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_650E")

    Jump("loc_6E6D")

    label("loc_6513")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_660B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_65CF")

    #C0344
    ChrTalk(
        0xFE,
        (
            "自治州議会が\x01",
            "また長引いているそうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0xFE,
        (
            "……主人が現役の頃から\x01",
            "何も変わっていないわねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0xFE,
        (
            "周りに迷惑ばかり掛けて、\x01",
            "自分勝手な議論ばかりなんだから。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_6606")

    label("loc_65CF")


    #C0347
    ChrTalk(
        0xFE,
        (
            "主人のあの性格も\x01",
            "きっと議員生活が長かったせいね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6606")

    Jump("loc_6E6D")

    label("loc_660B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_674E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_66DB")

    #C0348
    ChrTalk(
        0xFE,
        (
            "クロスベルの上流階級には\x01",
            "手芸をたしなむ方が多かったのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0xFE,
        (
            "マクダエル市長の奥様も\x01",
            "手芸がとてもお上手だったのだから。\x02",
        )
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0xFE,
        (
            "私がこの趣味をはじめたのも\x01",
            "あの方の影響かしらね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_6749")

    label("loc_66DB")


    #C0351
    ChrTalk(
        0xFE,
        (
            "マクダエル市長の奥様は\x01",
            "手芸がとてもお上手だったのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0352
    ChrTalk(
        0xFE,
        (
            "大分前にお亡くなりに\x01",
            "なってしまったけれどね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6749")

    Jump("loc_6E6D")

    label("loc_674E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_675C")
    Jump("loc_6E6D")

    label("loc_675C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_676A")
    Jump("loc_6E6D")

    label("loc_676A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_6778")
    Jump("loc_6E6D")

    label("loc_6778")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_6786")
    Jump("loc_6E6D")

    label("loc_6786")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_6794")
    Jump("loc_6E6D")

    label("loc_6794")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_680A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_67AF")
    Call(0, 14)
    Jump("loc_6805")

    label("loc_67AF")


    #C0353
    ChrTalk(
        0xFE,
        (
            "紅茶の淹れ方も\x01",
            "ろくに知らないのね。\x02",
        )
    )

    CloseMessageWindow()

    #C0354
    ChrTalk(
        0xFE,
        (
            "家事ができないくせに\x01",
            "よくやるものだわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6805")

    Jump("loc_6E6D")

    label("loc_680A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_692B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_68C2")

    #C0355
    ChrTalk(
        0xFE,
        (
            "今朝から男の人たちが\x01",
            "訪ねてきているみたいなのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0xFE,
        (
            "無言のまま３階に\x01",
            "上がって行ったけれど……\x02",
        )
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0xFE,
        (
            "只者ではない雰囲気だったわ。\x01",
            "一体何の御用かしら。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_6926")

    label("loc_68C2")


    #C0358
    ChrTalk(
        0xFE,
        (
            "あの男の人たち、\x01",
            "アパートに遊びに来たという\x01",
            "雰囲気じゃなかったわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0xFE,
        "一体何者なのかしら。\x02",
    )

    CloseMessageWindow()

    label("loc_6926")

    Jump("loc_6E6D")

    label("loc_692B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_6A07")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_69D3")

    #C0360
    ChrTalk(
        0xFE,
        (
            "主人たらまた\x01",
            "余計なことをして……\x02",
        )
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0xFE,
        (
            "掃除ならサミィさんに\x01",
            "任せておけばいいでしょうに。\x02",
        )
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0xFE,
        (
            "フン、慣れない事を\x01",
            "するからそうなるのよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_6A02")

    label("loc_69D3")


    #C0363
    ChrTalk(
        0xFE,
        (
            "あの人の余計な行動癖には\x01",
            "呆れてしまうわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6A02")

    Jump("loc_6E6D")

    label("loc_6A07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_6AFB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6AA8")

    #C0364
    ChrTalk(
        0xFE,
        (
            "私はね、毎年記念祭にあわせて\x01",
            "コースターを作っているのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0xFE,
        "これでかれこれ２０年ね。\x02",
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0xFE,
        (
            "ここまで続けると\x01",
            "感慨深いものだわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_6AF6")

    label("loc_6AA8")


    #C0367
    ChrTalk(
        0xFE,
        (
            "クロスベルも\x01",
            "今年で７０周年ね。\x02",
        )
    )

    CloseMessageWindow()

    #C0368
    ChrTalk(
        0xFE,
        (
            "毎年歳を重ねて……\x01",
            "感慨深いものね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6AF6")

    Jump("loc_6E6D")

    label("loc_6AFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_6B8A")

    #C0369
    ChrTalk(
        0xFE,
        (
            "主人はオーバルストアで\x01",
            "新しい導力コンロを買ってきたのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0xFE,
        "また私に内緒で散財して……\x02",
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0xFE,
        "他にやる事がないのかしらね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_6E6D")

    label("loc_6B8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_6C35")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6C01")

    #C0372
    ChrTalk(
        0xFE,
        (
            "やれやれ……\x01",
            "また主人の悪いくせが始まったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0xFE,
        (
            "これじゃ食事の\x01",
            "支度もできないわね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_6C30")

    label("loc_6C01")


    #C0374
    ChrTalk(
        0xFE,
        (
            "ふう、今日も外食で\x01",
            "済ませちゃおうかしら。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6C30")

    Jump("loc_6E6D")

    label("loc_6C35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_6C43")
    Jump("loc_6E6D")

    label("loc_6C43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_6D67")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6D14")

    #C0375
    ChrTalk(
        0xFE,
        (
            "ここのアパートは\x01",
            "管理人さんに家事を頼める\x01",
            "サービスがあるのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0376
    ChrTalk(
        0xFE,
        (
            "ウチもお掃除やクリーニングは\x01",
            "サミィさんにお願いしているわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0377
    ChrTalk(
        0xFE,
        (
            "おかげでたっぷり\x01",
            "趣味の時間が取れるのよね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_6D62")

    label("loc_6D14")


    #C0378
    ChrTalk(
        0xFE,
        (
            "最近ではお買い物も\x01",
            "配達サービスがあるし……\x01",
            "本当に暮らしが楽になったわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6D62")

    Jump("loc_6E6D")

    label("loc_6D67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_6E6D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6E13")

    #C0379
    ChrTalk(
        0xFE,
        (
            "主人はまた内装の\x01",
            "模様替えを始めたのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0380
    ChrTalk(
        0xFE,
        (
            "そのたびに私を\x01",
            "部屋の外に追い出すのよね……\x02",
        )
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0xFE,
        (
            "まったく、おちおち\x01",
            "手芸も楽しめないじゃない。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_6E6D")

    label("loc_6E13")


    #C0382
    ChrTalk(
        0xFE,
        (
            "主人は退職してから\x01",
            "暇で仕方ないらしいのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0383
    ChrTalk(
        0xFE,
        (
            "ミラの掛かる趣味で\x01",
            "困ったものだわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6E6D")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_16_615D end

    def Function_17_6E75(): pass

    label("Function_17_6E75")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8F, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6FFE")

    #C0384
    ChrTalk(
        0xFE,
        (
            "フム、ダドリーの\x01",
            "言っていた連中か…………\x02",
        )
    )

    CloseMessageWindow()

    #C0385
    ChrTalk(
        0xFE,
        (
            "……警護の邪魔になる。\x01",
            "早々に立ち去るがいい。\x02",
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
        "#0005Fえ……？\x02",
    )

    CloseMessageWindow()

    #C0387
    ChrTalk(
        0xFE,
        (
            "……ここは\x01",
            "イリア・プラティエの自宅だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0388
    ChrTalk(
        0xFE,
        (
            "彼女の身辺警護は\x01",
            "我々一課に任せてもらおう。\x02",
        )
    )

    CloseMessageWindow()

    #C0389
    ChrTalk(
        0x104,
        (
            "#0305F（捜査一課……\x01",
            "  早速動いてやがんのか。）\x02",
        )
    )

    CloseMessageWindow()

    #C0390
    ChrTalk(
        0x101,
        "#0003F（さ、流石だな……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x8F, 1)
    Jump("loc_7133")

    label("loc_6FFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_700C")
    Jump("loc_7133")

    label("loc_700C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_707E")

    #C0391
    ChrTalk(
        0xFE,
        (
            "……イリア・プラティエの\x01",
            "身辺警護は我々一課が担う。\x02",
        )
    )

    CloseMessageWindow()

    #C0392
    ChrTalk(
        0xFE,
        (
            "特務支援課、\x01",
            "余計な邪魔立てはするな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7133")

    label("loc_707E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_7133")

    #C0393
    ChrTalk(
        0xFE,
        (
            "……脅迫状の文面からするに、\x01",
            "イリア・プラティエが狙われるのは\x01",
            "舞台上である可能性が高い。\x02",
        )
    )

    CloseMessageWindow()

    #C0394
    ChrTalk(
        0xFE,
        (
            "だが、それ以外が安全とは言えん。\x01",
            "一課はあくまで\x01",
            "完璧な警護を行う予定だ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7133")

    TalkEnd(0xFE)
    Return()

    # Function_17_6E75 end

    def Function_18_7137(): pass

    label("Function_18_7137")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_7148")
    Jump("loc_727A")

    label("loc_7148")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_71BC")

    #C0395
    ChrTalk(
        0xFE,
        (
            "フム、屋外から……\x01",
            "狙撃される可能性もあるな。\x02",
        )
    )

    CloseMessageWindow()

    #C0396
    ChrTalk(
        0xFE,
        (
            "イリア嬢が戻る前に\x01",
            "周辺を洗っておくとしよう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_727A")

    label("loc_71BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_727A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7218")

    #C0397
    ChrTalk(
        0xFE,
        "盗聴器の類はナシ……\x02",
    )

    CloseMessageWindow()

    #C0398
    ChrTalk(
        0xFE,
        (
            "取りあえずは\x01",
            "クリーンな部屋だな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_727A")

    label("loc_7218")

    TurnDirection(0xFE, 0x0, 0)

    #C0399
    ChrTalk(
        0xFE,
        "……特務支援課、だな？\x02",
    )

    CloseMessageWindow()

    #C0400
    ChrTalk(
        0xFE,
        (
            "フン、イリア嬢の身辺警護なら\x01",
            "我々捜査一課に任せたまえよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_727A")

    TalkEnd(0xFE)
    Return()

    # Function_18_7137 end

    def Function_19_727E(): pass

    label("Function_19_727E")

    TalkBegin(0x12)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_7611")
    OP_64(0x12)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_736C")

    #C0401
    ChrTalk(
        0x12,
        (
            "ぐかーっ……ぐかーっ……\x02\x03",

            "ンンッ……ン～……！\x02",
        )
    )

    CloseMessageWindow()

    #C0402
    ChrTalk(
        0x153,
        (
            "#1110Fキレイなお姉さんだけど\x01",
            "すごいイビキー！\x02",
        )
    )

    CloseMessageWindow()

    #C0403
    ChrTalk(
        0x101,
        "#0006F（微妙に色っぽくて困るな……）\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7367")

    #C0404
    ChrTalk(
        0x104,
        "#0309F（やっぱ今日は超ラッキーだぜ……！）\x02",
    )

    CloseMessageWindow()

    label("loc_7367")

    Jump("loc_75FA")

    label("loc_736C")


    #C0405
    ChrTalk(
        0x12,
        "ぐかーっ……ぐかーっ……\x02",
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
            "#1110Fわー。\x01",
            "すごいイビキだねー！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_7442")

    #C0407
    ChrTalk(
        0x101,
        (
            "#0006Fしかも相変わらず\x01",
            "部屋が散らかってるし……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7477")

    label("loc_7442")


    #C0408
    ChrTalk(
        0x101,
        (
            "#0006Fしかもこの部屋、\x01",
            "すごく散らかってるし……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7477")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_74C7")

    #C0409
    ChrTalk(
        0x102,
        (
            "#0100F公演の時の張り詰めた\x01",
            "雰囲気とは天地の差よね……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_75F4")

    label("loc_74C7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_750F")

    #C0410
    ChrTalk(
        0x103,
        (
            "#0200F相変わらず微妙に\x01",
            "オジサン臭い人ですね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_75F4")

    label("loc_750F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_75F4")

    #C0411
    ChrTalk(
        0x104,
        (
            "#0304Fフ……それでこそ\x01",
            "天下無敵のイリア・プラティエだぜ。\x02\x03",

            "#0309Fそしてまさか寝顔まで\x01",
            "拝めるとは、今日は超ラッキー！\x02",
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
        "#0003Fいや、キーアは判らなくてもいいよ。\x02",
    )

    CloseMessageWindow()

    label("loc_75F4")

    SetScenarioFlags(0xBF, 3)
    SetScenarioFlags(0x0, 6)

    label("loc_75FA")

    OP_63(0x12, 0x0, 2000, 0x1C, 0x21, 0xFA, 0x0)
    Jump("loc_7768")

    label("loc_7611")

    OP_4B(0x15, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_76C6")

    #C0414
    ChrTalk(
        0x12,
        (
            "#1700Fうっし、シュリ。\x01",
            "まずは稽古の\x01",
            "しきたりから始めるわよ？\x02\x03",

            "#1709F朝５時前に\x01",
            "あたしを起こすこと！\x02\x03",

            "#1705Fあ……ベッドないし一緒に寝る？\x02",
        )
    )

    CloseMessageWindow()

    #C0415
    ChrTalk(
        0x15,
        "いらん！！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_7764")

    label("loc_76C6")


    #C0416
    ChrTalk(
        0x15,
        (
            "それより舞台の話、してくれ。\x01",
            "あの新しい劇の話……\x02",
        )
    )

    CloseMessageWindow()

    #C0417
    ChrTalk(
        0x12,
        (
            "#1702Fああ、舞台の話ね？\x01",
            "オッケー、話したげる！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    #C0418
    ChrTalk(
        0x15,
        "………………！（コクコク）\x02",
    )

    CloseMessageWindow()

    label("loc_7764")

    OP_4C(0x15, 0xFF)

    label("loc_7768")

    TalkEnd(0x12)
    Return()

    # Function_19_727E end

    def Function_20_776C(): pass

    label("Function_20_776C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB8, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7961")

    #C0419
    ChrTalk(
        0x14,
        (
            "#1802F皆さん、今回は色々と\x01",
            "ご迷惑を掛けてしまって……\x02\x03",

            "#1809Fでもありがとうございました。\x01",
            "丸く収まって本当に良かったです。\x02",
        )
    )

    CloseMessageWindow()

    #C0420
    ChrTalk(
        0x102,
        (
            "#0109Fこんな展開になるなんて\x01",
            "私たちも予想してなかったけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0421
    ChrTalk(
        0x14,
        (
            "#1804Fはい……\x02\x03",

            "#1810F……あの子の気持ち、\x01",
            "少し分かるんです。\x02\x03",

            "私もイリアさんに会うまでは\x01",
            "道を見失っていたから……\x02",
        )
    )

    CloseMessageWindow()

    #C0422
    ChrTalk(
        0x101,
        "#0005Fリーシャ……？\x02",
    )

    CloseMessageWindow()

    #C0423
    ChrTalk(
        0x14,
        (
            "#1804Fあ、いえ……\x01",
            "なんでもありません。\x02\x03",

            "#1802Fシュリちゃんはイリアさんと\x01",
            "暮らす事になるみたいです。\x01",
            "また会いに来てあげてくださいね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB8, 4)
    Jump("loc_7A76")

    label("loc_7961")


    #C0424
    ChrTalk(
        0x14,
        (
            "#1808Fシュリちゃんも\x01",
            "色々とあったみたいですから、\x01",
            "すぐには馴染めないかもしれません。\x02\x03",

            "#1802Fでも私も協力しますから……\x01",
            "きっと大丈夫です。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7A73")

    #C0425
    ChrTalk(
        0x101,
        (
            "#0000Fそうか……\x01",
            "それじゃ２人の事は\x01",
            "よろしく頼むよ、リーシャ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x14, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    #C0426
    ChrTalk(
        0x14,
        "#1809Fはい、もちろんです！\x02",
    )

    CloseMessageWindow()

    label("loc_7A73")

    SetScenarioFlags(0x0, 7)

    label("loc_7A76")

    TalkEnd(0xFE)
    Return()

    # Function_20_776C end

    def Function_21_7A7A(): pass

    label("Function_21_7A7A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0xC)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7C5B")

    #C0427
    ChrTalk(
        0x101,
        (
            "#0002Fどうやら\x01",
            "上手くやってるみたいだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0428
    ChrTalk(
        0xFE,
        "フン、べつに……\x02",
    )

    CloseMessageWindow()

    #C0429
    ChrTalk(
        0xFE,
        (
            "ただ色々話してるだけだ。\x01",
            "舞台の話はキラキラしてて\x01",
            "……聞いてて面白いから。\x02",
        )
    )

    CloseMessageWindow()

    #C0430
    ChrTalk(
        0x102,
        (
            "#0100F（やっぱり舞台に\x01",
            "  興味あるみたいね。）\x02",
        )
    )

    CloseMessageWindow()

    #C0431
    ChrTalk(
        0x104,
        (
            "#0304F（結構女の子っぽい所も\x01",
            "  あるじゃねえか。）\x02",
        )
    )

    CloseMessageWindow()

    #C0432
    ChrTalk(
        0x103,
        "#0202F（ですね。）\x02",
    )

    CloseMessageWindow()

    #C0433
    ChrTalk(
        0xFE,
        "あ、それと……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x15, 0x101, 500)

    #C0434
    ChrTalk(
        0xFE,
        (
            "ロイドだっけ？\x01",
            "お前ぜってー覚えとけよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0435
    ChrTalk(
        0xFE,
        (
            "オレは恨みは\x01",
            "ぜってー忘れないからな！\x02",
        )
    )

    CloseMessageWindow()

    #C0436
    ChrTalk(
        0x101,
        (
            "#0012Fう……あの事か。\x01",
            "（もう忘れて欲しいんだが……）\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x1D, 0x1, 0xC)
    Jump("loc_7CD0")

    label("loc_7C5B")


    #C0437
    ChrTalk(
        0xFE,
        (
            "イリア……さんは、\x01",
            "話はすごく面白いんだ。\x01",
            "聞いててワクワクする……\x02",
        )
    )

    CloseMessageWindow()

    #C0438
    ChrTalk(
        0xFE,
        (
            "……普段はすげー\x01",
            "だらしない人だけどな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7CD0")

    TalkEnd(0xFE)
    Return()

    # Function_21_7A7A end

    def Function_22_7CD4(): pass

    label("Function_22_7CD4")

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

    def lambda_7D5E():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_7D5E)

    def lambda_7D73():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_7D73)

    def lambda_7D88():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_7D88)

    def lambda_7D9D():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_7D9D)
    OP_68(50, 1280, 1520, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(2000)

    #C0439
    ChrTalk(
        0x101,
        (
            "#5P#0005F《ヴィラ・レザン》の\x01",
            "最上階、と……\x02",
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
            "#0000Fあそこが\x01",
            "イリアさんの部屋だな。\x02",
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
            "#6P#0200Fまずは部屋の中を\x01",
            "確かめてみましょうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0442
    ChrTalk(
        0x101,
        "#5P#0000Fああ、行ってみよう。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 10, 30, 990, 0)
    OP_29(0x1D, 0x1, 0x2)
    OP_C7(0x0, 0x1000)
    EventEnd(0x5)
    Return()

    # Function_22_7CD4 end

    def Function_23_7EF7(): pass

    label("Function_23_7EF7")

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
            "扉には鍵がかかっている。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0444
    ChrTalk(
        0x101,
        "#5P#0000Fよし、鍵は、と……\x02",
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
        "#12P#0305Fロイド、どうかしたのか？\x02",
    )

    CloseMessageWindow()

    #C0446
    ChrTalk(
        0x101,
        "#11P#0005Fあ、ああ……\x02",
    )

    CloseMessageWindow()
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1300)

    #C0447
    ChrTalk(
        0x101,
        "#11P#0001Fピッキングの跡だ。\x02",
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
            "#11P#0003F鍵穴の僅かな傷……\x01",
            "相当腕のいい奴が開けているな。\x02",
        )
    )

    CloseMessageWindow()

    #C0449
    ChrTalk(
        0x103,
        (
            "#6P#0200F部屋に入ってるのは\x01",
            "間違いなさそうですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0450
    ChrTalk(
        0x102,
        (
            "#12P#0101Fやっぱり……\x01",
            "早く捕まえないと駄目ね。\x02",
        )
    )

    CloseMessageWindow()

    #C0451
    ChrTalk(
        0x101,
        (
            "#5P#0001Fああ、でないと\x01",
            "ストーカー本人のためにも\x01",
            "ならない……\x02",
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
            "#5P#0001Fみんな、気合を入れて\x01",
            "捜査を進めよう！\x02",
        )
    )

    CloseMessageWindow()

    #C0453
    ChrTalk(
        0x104,
        "#12P#0300Fおうよ！\x02",
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

    def lambda_82C0():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_82C0)

    def lambda_82D5():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_82D5)

    def lambda_82EA():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_82EA)

    def lambda_82FF():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_82FF)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(2000)

    #C0454
    ChrTalk(
        0x104,
        (
            "#12P#0300F高級アパートの最上階、\x01",
            "さすがにいい部屋だなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0455
    ChrTalk(
        0x101,
        (
            "#5P#0000Fああ、こんな広い部屋に\x01",
            "一人暮らしなんて\x01",
            "さすがイリアさんだ……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    #C0456
    ChrTalk(
        0x101,
        (
            "#5P#0005Fあれ、でもなんだか\x01",
            "ちょっと散らかってる？\x02",
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
            "#0200Fワイングラスに\x01",
            "脱ぎ捨てた服……\x02\x03",

            "#0203Fこれはストーカーではなく\x01",
            "ご本人の所業かと。\x02",
        )
    )

    CloseMessageWindow()

    #C0458
    ChrTalk(
        0x102,
        (
            "#0100Fそういえばイリアさんは\x01",
            "女傑な所があるし……\x01",
            "むしろイメージ通りかもしれないわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0459
    ChrTalk(
        0x104,
        (
            "#0306Fま、ファンとしちゃ\x01",
            "ビミョーな所だなぁ……\x02",
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

    def lambda_8590():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8590)

    def lambda_859D():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_859D)

    def lambda_85AA():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_85AA)

    def lambda_85B7():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_85B7)
    Sleep(300)

    #C0460
    ChrTalk(
        0x101,
        (
            "#5P#0001Fともかくまずは\x01",
            "犯人について調べてみよう。\x02\x03",

            "#0003F今回は犯人を捕まえて\x01",
            "イリアさんの元に突き出すのが\x01",
            "目的だけど……\x02\x03",

            "#0001F下調べは慎重にした方が\x01",
            "いいと思う。\x02",
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
            "#11P#0103F今回みたいなストーカー事件は\x01",
            "あいまいな目撃情報しか残らないわ。\x02\x03",

            "#0100F現場を取り押さえないと\x01",
            "シラを切られてしまうでしょう？\x02",
        )
    )

    CloseMessageWindow()

    #C0462
    ChrTalk(
        0x104,
        (
            "#12P#0306Fなるほどな、\x01",
            "ちょいと面倒だぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0463
    ChrTalk(
        0x103,
        (
            "#6P#0200F確実に捕らえるには\x01",
            "犯人像や行動パターン、侵入経路は\x01",
            "調べておきたい所ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0464
    ChrTalk(
        0x101,
        (
            "#5P#0000Fああ、アパートの人たちに\x01",
            "一通り聞き込みしてみよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0465
    ChrTalk(
        0x104,
        (
            "#12P#0300Fついでにアパートの\x01",
            "構造把握もやっておかねえとな。\x02\x03",

            "聞き込みをしながら\x01",
            "一通り回ってみようぜ。\x02",
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

    # Function_23_7EF7 end

    def Function_24_88C8(): pass

    label("Function_24_88C8")

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
            "#5P#0003F犯人像、侵入ルート……\x01",
            "大体見えてきたかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0467
    ChrTalk(
        0x103,
        (
            "#6P#0200Fそうですね。\x02\x03",

            "犯人は帽子を被った少年で、\x01",
            "かなり慎重に行動しているようです。\x02",
        )
    )

    CloseMessageWindow()

    #C0468
    ChrTalk(
        0x102,
        (
            "#11P#0101F最近はこの部屋にも\x01",
            "複数回入っているみたいね。\x02\x03",

            "#0103F……イリアさんから聞いた限りでは\x01",
            "盗られた物はなさそうだったけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0469
    ChrTalk(
        0x104,
        (
            "#12P#0306Fまあ意味もなく侵入してくんのが\x01",
            "ストーカーなんじゃねえか？\x02\x03",

            "#0301Fあと分かってる情報は……\x01",
            "侵入経路は恐らく\x01",
            "アパートの裏口って所か。\x02",
        )
    )

    CloseMessageWindow()

    #C0470
    ChrTalk(
        0x101,
        (
            "#5P#0003Fよし、以上の情報を元に\x01",
            "待ち伏せしてみよう。\x02\x03",

            "#0000Fみんな、耳を貸してくれるか？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8B65():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8B65)
    Sleep(10)

    def lambda_8B75():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8B75)
    Sleep(300)

    #C0471
    ChrTalk(
        0x103,
        (
            "#12P#0205Fロイドさん、また何か\x01",
            "考えがあるみたいですね？\x02",
        )
    )

    CloseMessageWindow()

    #C0472
    ChrTalk(
        0x101,
        (
            "#0000F相手は少年とはいえ\x01",
            "油断ならない相手みたいだ。\x02\x03",

            "確実に捕まえられるよう、\x01",
            "段取りをとろうと思ってさ。\x02",
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

    # Function_24_88C8 end

    def Function_25_8C49(): pass

    label("Function_25_8C49")

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
            "#5Pさてと、廊下の掃除は\x01",
            "こんな所かしらね。\x02",
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
            "#5Pいけない、明日はパレードだから\x01",
            "ゴミ出しの時間が\x01",
            "変更になってるんだったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0475
    ChrTalk(
        0x8,
        (
            "#5Pキンドールさんのお宅に\x01",
            "一言言っておかなくちゃ。\x02",
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

    def lambda_8EAC():
        OP_95(0xFE, -9430, 1150, 6880, 1900, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_8EAC)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-270, 11270, 18770, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(20500, 0)
    SetChrPos(0x15, 2800, 10000, 18580, 270)

    def lambda_8F10():
        OP_95(0xFE, -250, 10000, 18580, 1700, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_8F10)
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
            "少年は針金を取り出し、\x01",
            "素早く鍵穴へ差し込んだ。\x02",
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
        "#5Pフン……ちょろいもんだ。\x02",
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
        "#5Pさてと、今日こそは……\x02",
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
            "#5Pって、相変わらず\x01",
            "汚ったねえ散らかしようだな……\x02",
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
            "#5Pあーあ、また\x01",
            "こんなに飲みやがって。\x02",
        )
    )

    CloseMessageWindow()

    #N0483
    NpcTalk(
        0x15,
        "少年",
        (
            "#5P……こう汚いと\x01",
            "盗る気失せるんだよな。\x01",
            "ったく……\x02",
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
        "#5Pさてと……何を盗んでやるか。\x02",
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1300)

    #N0485
    NpcTalk(
        0x15,
        "少年",
        (
            "#5Pいや、こんなモンじゃねえ。\x01",
            "もっとあいつが慌てそうな……\x02",
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
            "#5Pへっ、いっそのこと\x01",
            "金庫でも破って……\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x102, 0x80)
    ClearChrFlags(0x103, 0x80)
    ClearChrFlags(0x104, 0x80)

    #N0487
    NpcTalk(
        0x101,
        "声",
        "#1P#4S──そこまでよ！\x02",
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

    def lambda_9373():
        OP_95(0xFE, 56540, 1030, 58700, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9373)

    def lambda_938D():
        OP_95(0xFE, 55760, 1000, 57400, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_938D)

    #N0488
    NpcTalk(
        0x15,
        "少年",
        "#5Pなっ……！？\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x102, 1)

    #C0489
    ChrTalk(
        0x102,
        (
            "#0105Fストーカーって言うから\x01",
            "どんな子かと思ったけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0490
    ChrTalk(
        0x103,
        (
            "#0200Fまあ犯罪には違いありません。\x01",
            "大人しくしてもらいましょう。\x02",
        )
    )

    CloseMessageWindow()

    #N0491
    NpcTalk(
        0x15,
        "少年",
        (
            "#5Pま、待ち伏せ……\x01",
            "くそっ、しくじった……！！\x02",
        )
    )

    CloseMessageWindow()

    #N0492
    NpcTalk(
        0x104,
        "青年の声",
        "おっと、逃げられねえぜ？\x02",
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
            "#0300F#12Pこっちは行き止まりだ。\x01",
            "諦めて降参しろや。\x02",
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
        "#5Pくっ……捕まるものか！\x02",
    )

    CloseMessageWindow()

    #N0495
    NpcTalk(
        0x15,
        "少年",
        "#5Pお前らなんか……\x02",
    )

    CloseMessageWindow()

    #N0496
    NpcTalk(
        0x15,
        "少年",
        (
            "#5Pお前らみたいな連中は\x01",
            "大嫌いなんだよ！！\x02",
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

    def lambda_9610():
        OP_93(0x102, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9610)

    def lambda_961D():
        OP_93(0x103, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_961D)
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

    def lambda_96B8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_96B8)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_95(0x15, 49740, 0, 46610, 7000, 0x0)

    #C0497
    ChrTalk(
        0x104,
        "#12P#0305Fな……！？\x02",
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
            "#6P#0301Fヤロォ……\x01",
            "いい動きすんじゃねーか。\x02",
        )
    )

    CloseMessageWindow()
    SetChrChip(0x1, 0x15, 0x0, 0x0)

    #C0499
    ChrTalk(
        0x103,
        "#11P#0201Fランディさん……！\x02",
    )

    CloseMessageWindow()

    #C0500
    ChrTalk(
        0x102,
        "#5P#0101Fランディ、追うわよ！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x102, 500)
    Sleep(200)

    #C0501
    ChrTalk(
        0x104,
        "#0307F#12Pおうよ！\x02",
    )

    CloseMessageWindow()
    OP_93(0x104, 0xB4, 0x0)
    OP_93(0x102, 0xB4, 0x0)
    OP_93(0x103, 0xB4, 0x0)

    def lambda_97DB():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_97DB)

    def lambda_97F0():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_97F0)

    def lambda_9805():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_9805)
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

    def lambda_9879():
        OP_95(0xFE, -200, 10000, 18300, 7000, 0x1)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_9879)
    OP_82(0xC8, 0x64, 0xBB8, 0x12C)
    Sound(103, 0, 100, 0)
    Sound(121, 0, 100, 0)
    Sound(818, 0, 80, 0)
    FadeToBright(250, 0)
    OP_0D()
    WaitChrThread(0x15, 1)
    OP_95(0x15, 7690, 10000, 18300, 7000, 0x0)

    def lambda_98D8():
        OP_95(0xFE, 9100, 10030, 15930, 7000, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_98D8)
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
            "少年は扉を開け放した。\x02",
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
            "#11Pへっ、マヌケども。\x01",
            "こっちでも探してろ……！\x02",
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

    # Function_25_8C49 end

    def Function_26_9A03(): pass

    label("Function_26_9A03")

    OP_95(0x8, 9010, 10020, 15730, 2100, 0x0)
    OP_95(0x8, 8610, 7500, 10850, 2100, 0x0)
    OP_95(0x8, 1970, 5000, 10850, 2300, 0x0)
    OP_95(0x8, -2860, 5000, 17000, 2300, 0x0)
    SetChrFlags(0x8, 0x80)
    Return()

    # Function_26_9A03 end

    def Function_27_9A59(): pass

    label("Function_27_9A59")

    OP_95(0x102, 49750, 1050, 57720, 5000, 0x0)
    OP_93(0x102, 0xB4, 0x1F4)
    Return()

    # Function_27_9A59 end

    def Function_28_9A75(): pass

    label("Function_28_9A75")

    OP_95(0x103, 50510, 1000, 56870, 5000, 0x0)
    OP_93(0x103, 0xB4, 0x1F4)
    Return()

    # Function_28_9A75 end

    def Function_29_9A91(): pass

    label("Function_29_9A91")

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
            "ロイド達はイリアに連絡を入れ\x01",
            "犯人逮捕の報を告げた。\x02",
        )
    )

    CloseMessageWindow()

    #A0505
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "少年はなおも暴れたが、\x01",
            "やがて観念し大人しくなったのだった。\x02",
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
            "#5P#1705Fへえ……それで君が\x01",
            "ストーカーだったわけか。\x02\x03",

            "#1700F思ってたより小柄な子だけど……\x01",
            "クロスベルの出身じゃ無さそうね？\x02",
        )
    )

    CloseMessageWindow()

    #C0507
    ChrTalk(
        0x101,
        (
            "#12P#0006Fええ、どうも辺境の\x01",
            "スラム出身者らしくて。\x02\x03",

            "#0001Fただ、事情はおろか\x01",
            "名前も喋らないんですよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0508
    ChrTalk(
        0x12,
        (
            "#5P#1703Fふむ、そっかそっか。\x02\x03",

            "#1700F……キミ、どうして\x01",
            "あたしに付きまとってたの？\x02\x03",

            "何か欲しいものでもあったわけ？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x15, 0x13B, 0x190)
    Sleep(300)

    #N0509
    NpcTalk(
        0x15,
        "少年",
        "#6Pフン、別に……\x02",
    )

    CloseMessageWindow()

    #N0510
    NpcTalk(
        0x15,
        "少年",
        (
            "#6Pただ嫌がらせしてやろうと\x01",
            "思っただけだ。\x02",
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
        "#1805F#11P嫌がらせ……？\x02",
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    OP_93(0x15, 0x0, 0x1F4)
    Sleep(300)

    #N0512
    NpcTalk(
        0x15,
        "少年",
        "#6Pお前らなんかに何が判る……\x02",
    )

    CloseMessageWindow()

    #N0513
    NpcTalk(
        0x15,
        "少年",
        (
            "#6Pこんないい所に住んで\x01",
            "毎日うまいもん食って……\x02",
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
            "#6P#4S#Nそんな連中に\x01",
            "ゴミ溜めみたいな街で生きてきた\x01",
            "オレの何が判るってんだよッ！！\x02",
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
            "#6P……クロスベルに来てから\x01",
            "ずっと見てた。\x02",
        )
    )

    CloseMessageWindow()

    #N0518
    NpcTalk(
        0x15,
        "少年",
        (
            "#6Pここの連中は金持ちばっかで\x01",
            "毎晩大金使って遊んでやがる。\x02",
        )
    )

    CloseMessageWindow()

    #N0519
    NpcTalk(
        0x15,
        "少年",
        (
            "#6Pハッ、好きにしろってんだ。\x01",
            "オレはそんな連中、嫌いだからよ。\x02",
        )
    )

    CloseMessageWindow()

    #N0520
    NpcTalk(
        0x15,
        "少年",
        (
            "#6P……でも、そいつらが最高の娯楽は\x01",
            "アルカンシェルだって言うから……\x01",
            "一度だけ忍び込んでやったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0521
    ChrTalk(
        0x12,
        "#1705F#5P………え……………？\x02",
    )

    CloseMessageWindow()

    #C0522
    ChrTalk(
        0x103,
        (
            "#11P#0200Fアルカンシェルの……\x01",
            "イリアさんの舞台を\x01",
            "見たのですか……？\x02",
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
            "#6P何の心配もなく\x01",
            "のらくら暮らしてやがる連中は嫌いだ。\x02",
        )
    )

    CloseMessageWindow()

    #N0524
    NpcTalk(
        0x15,
        "少年",
        (
            "#6Pでも、あんたは……\x01",
            "#4Sもっと大嫌いだ！！\x02",
        )
    )

    CloseMessageWindow()

    #N0525
    NpcTalk(
        0x15,
        "少年",
        (
            "#6Pあんな綺麗な舞台に立って、\x01",
            "すごい世界を演じて……\x02",
        )
    )

    CloseMessageWindow()

    #N0526
    NpcTalk(
        0x15,
        "少年",
        (
            "#6P絶対届かない場所にいて、\x01",
            "あんなに輝いてるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #N0527
    NpcTalk(
        0x15,
        "少年",
        (
            "#6Pオレには死ぬまで掛かったって\x01",
            "絶対届かない……\x02",
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
            "#6Pオレが死ぬまで働いたって\x01",
            "チケット一枚分も稼げねえ。\x02",
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
            "#6P#4S#N──そうだろ！？\x01",
            "オレには死ぬまで掛かったって\x01",
            "絶対届かないんだ！！\x02",
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
            "そういう事だったか……\x02",
        )
    )

    CloseMessageWindow()

    #C0531
    ChrTalk(
        0x101,
        (
            "#12P#0008Fクロスベルに来て……\x01",
            "イリアさんの舞台を見て……\x02\x03",

            "#0006F確かにショックだったかも\x01",
            "しれないな。\x02",
        )
    )

    CloseMessageWindow()

    #C0532
    ChrTalk(
        0x14,
        (
            "#1803F#11P……そう、ですね……\x02\x03",

            "#1808F確かにクロスベルには\x01",
            "そういった面があります。\x02\x03",

            "#1801F大都市の持つ闇の面……\x01",
            "時に人を惨めにするような力が……\x02",
        )
    )

    CloseMessageWindow()

    #C0533
    ChrTalk(
        0x12,
        (
            "#1703F#5P………………………………\x02\x03",

            "#1700Fま、いずれにせよ\x01",
            "ケジメは付けてもらわないとね。\x02",
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

    def lambda_A611():

        label("loc_A611")

        TurnDirection(0xFE, 0x12, 500)
        Yield()
        Jump("loc_A611")

    QueueWorkItem2(0x0, 1, lambda_A611)

    def lambda_A623():

        label("loc_A623")

        TurnDirection(0xFE, 0x12, 500)
        Yield()
        Jump("loc_A623")

    QueueWorkItem2(0x1, 1, lambda_A623)

    def lambda_A635():

        label("loc_A635")

        TurnDirection(0xFE, 0x12, 500)
        Yield()
        Jump("loc_A635")

    QueueWorkItem2(0x2, 1, lambda_A635)

    def lambda_A647():

        label("loc_A647")

        TurnDirection(0xFE, 0x12, 500)
        Yield()
        Jump("loc_A647")

    QueueWorkItem2(0x3, 1, lambda_A647)

    def lambda_A659():

        label("loc_A659")

        TurnDirection(0xFE, 0x12, 500)
        Yield()
        Jump("loc_A659")

    QueueWorkItem2(0x14, 1, lambda_A659)
    OP_68(48800, 2250, 51320, 2000)

    def lambda_A67C():
        OP_95(0xFE, 49730, 0, 54230, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_A67C)

    #C0534
    ChrTalk(
        0x102,
        "#11P#0105Fイリアさん……？\x02",
    )

    CloseMessageWindow()

    #C0535
    ChrTalk(
        0x101,
        "#12P#0011Fあの、何を……\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x12, 1)

    #C0536
    ChrTalk(
        0x12,
        (
            "#5P#1701Fあたしはイリア・プラティエ。\x01",
            "……あんた、名前は何ていうの？\x02",
        )
    )

    CloseMessageWindow()

    #N0537
    NpcTalk(
        0x15,
        "少年",
        (
            "#6P……………………………\x01",
            "……シュリだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0538
    ChrTalk(
        0x12,
        (
            "#5P#1703Fシュリね、了解。\x02\x03",

            "#1701Fシュリ、あんたはしばらく\x01",
            "劇団で下働きしなさい。\x02\x03",

            "その分じゃミラで償うって\x01",
            "わけにも行かないでしょ。\x01",
            "しっかり働いてもらうわよ？\x02",
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
        "#6P……………な…………\x02",
    )

    CloseMessageWindow()

    #C0540
    ChrTalk(
        0x101,
        "#12P#0005Fイ、イリアさん、それは……？\x02",
    )

    CloseMessageWindow()
    OP_93(0x12, 0x87, 0x190)
    Sleep(200)

    #C0541
    ChrTalk(
        0x12,
        (
            "#5P#1706Fごめんねー、せっかく\x01",
            "捕まえてもらったのに。\x02\x03",

            "#1700Fあたしがしばらく\x01",
            "預からせてもらうわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0542
    ChrTalk(
        0x104,
        "#11P#0302F無罪放免、ってワケっすか。\x02",
    )

    CloseMessageWindow()

    #C0543
    ChrTalk(
        0x103,
        (
            "#11P#0202Fやれやれですね。\x01",
            "……まあイリアさんが\x01",
            "そう仰るなら。\x02",
        )
    )

    CloseMessageWindow()

    #C0544
    ChrTalk(
        0x12,
        "#5P#1704Fフフン、それとね。\x02",
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
            "イリアは少年の肩を叩いた。\x02",
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
        "#6Pちょ……なにすんだよ！？\x02",
    )

    CloseMessageWindow()

    #C0547
    ChrTalk(
        0x12,
        (
            "#5P#1709Fうん、やっぱ思ったとおりね。\x02\x03",

            "#1700Fもうちょい筋肉が\x01",
            "欲しいとこだけど……\x02",
        )
    )

    CloseMessageWindow()
    EndChrThread(0x15, 0x1)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AAFB")
    OP_93(0x15, 0x10E, 0x190)

    label("loc_AAFB")

    Sleep(400)
    OP_93(0x15, 0x0, 0x1F4)
    Sleep(200)

    #C0548
    ChrTalk(
        0x12,
        (
            "#5P#1702Fシュリ、あんたは\x01",
            "中々素質がありそうだわ。\x02\x03",

            "#1709F鍛えれば、あたしやリーシャとも並ぶ\x01",
            "アーティストになれるかもよ？\x02",
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
        "#6Pえ……\x02",
    )

    CloseMessageWindow()
    OP_82(0x96, 0x0, 0xBB8, 0x12C)

    #C0550
    ChrTalk(
        0x15,
        "#6P#4Sえええっ……！？\x02",
    )

    CloseMessageWindow()

    #C0551
    ChrTalk(
        0x15,
        "#6Pな、なんでオレが……！？\x02",
    )

    CloseMessageWindow()

    #C0552
    ChrTalk(
        0x102,
        (
            "#11P#0102Fそういえば……\x01",
            "かなり身軽な子だったわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0553
    ChrTalk(
        0x104,
        (
            "#11P#0300Fああ、あのフットワークは\x01",
            "ちょいと驚いた。\x02\x03",

            "#0304F……なるほど、そっち方面の\x01",
            "素質があったのか。\x02",
        )
    )

    CloseMessageWindow()

    #C0554
    ChrTalk(
        0x12,
        (
            "#5P#1702Fま、そういうことだから\x01",
            "ウチに来てもらうわよ。\x02\x03",

            "#1709Fあんたに選択権はなーい！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    #C0555
    ChrTalk(
        0x15,
        (
            "#6Pオ、オレ……\x01",
            "……でもそんな…………\x02",
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
            "#1809F#5Pふふ……\x01",
            "イリアさんらしいです。\x02\x03",

            "#1810F……私の時も\x01",
            "まったく同じで、強引でしたから。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    def lambda_ADC3():
        OP_93(0xFE, 0x0, 0x15E)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_ADC3)
    Sleep(20)

    def lambda_ADD3():
        OP_93(0xFE, 0x0, 0x15E)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_ADD3)
    Sleep(400)

    #C0557
    ChrTalk(
        0x101,
        (
            "#12P#0002Fそ、そうだったのか。\x02\x03",

            "#0004Fでもまあ、イリアさんのお陰で\x01",
            "丸く収まったみたいだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0558
    ChrTalk(
        0x103,
        "#11P#0202Fそうですね。\x02",
    )

    CloseMessageWindow()

    def lambda_AE60():
        OP_93(0xFE, 0x10E, 0x15E)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_AE60)
    Sleep(20)

    def lambda_AE70():
        OP_93(0xFE, 0x10E, 0x15E)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_AE70)
    Sleep(800)
    EndChrThread(0x12, 0x2)
    EndChrThread(0x15, 0x2)
    OP_64(0x12)
    OP_64(0x15)

    #C0559
    ChrTalk(
        0x12,
        "#1709F#5Pビシッ！　文句言うな～！\x02",
    )

    CloseMessageWindow()

    #C0560
    ChrTalk(
        0x15,
        (
            "#6Pオ、オレはまだ\x01",
            "うんって言ったわけじゃねえぞ！？\x02",
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
            "#5P#1705Fもう帰っちゃうの？\x01",
            "お茶くらい飲んでいけばいいのに。\x02",
        )
    )

    CloseMessageWindow()

    #C0562
    ChrTalk(
        0x101,
        (
            "#0004F#6Pいえ、まだ仕事も\x01",
            "抱えていますし。\x02\x03",

            "#0005Fあ、そうだ。\x01",
            "鍵をお返ししておきますね。\x02",
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
            "を返した。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    SubItemNumber(0x347, 1)
    OP_96(0x101, 0xFFFFFD6C, 0x2710, 0x44FC, 0x4B0, 0x0)

    #C0564
    ChrTalk(
        0x12,
        (
            "#5P#1704Fうん、確かに。\x02\x03",

            "#1700F世話になったわね、弟君。\x01",
            "帰り道も気をつけてね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0565
    ChrTalk(
        0x14,
        (
            "#11P#1809F私からもお礼を言わせてください。\x01",
            "皆さん、ありがとうございました。\x02",
        )
    )

    CloseMessageWindow()

    #C0566
    ChrTalk(
        0x104,
        (
            "#12P#0309Fおう、またな\x01",
            "リーシャちゃん！\x02",
        )
    )

    CloseMessageWindow()

    #C0567
    ChrTalk(
        0x102,
        (
            "#12P#0102Fイリアさん、リーシャさん。\x01",
            "シュリ君の事はお任せしますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0568
    ChrTalk(
        0x103,
        (
            "#12P#0204F事件が解決したとはいえ\x01",
            "戸締りには気を付けてください。\x02",
        )
    )

    CloseMessageWindow()

    #C0569
    ChrTalk(
        0x101,
        (
            "#0014F#6Pはは……また何かあれば\x01",
            "支援課の方へどうぞ。\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 1)
    Sleep(200)

    def lambda_B2A3():

        label("loc_B2A3")

        TurnDirection(0xFE, 0x101, 300)
        Yield()
        Jump("loc_B2A3")

    QueueWorkItem2(0x12, 1, lambda_B2A3)

    def lambda_B2B5():

        label("loc_B2B5")

        TurnDirection(0xFE, 0x101, 300)
        Yield()
        Jump("loc_B2B5")

    QueueWorkItem2(0x14, 1, lambda_B2B5)
    OP_95(0x101, -600, 10000, 18360, 1000, 0x0)
    OP_93(0x101, 0x2D, 0x190)
    OP_93(0x15, 0xE1, 0x190)
    Sleep(300)

    #C0570
    ChrTalk(
        0x101,
        (
            "#0000F#6P……じゃあな。\x02\x03",

            "#0002Fもうこんな事はするなよ？\x01",
            "男だったら受けた恩は返さないとな。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_68(930, 11250, 17540, 2800)

    def lambda_B36F():

        label("loc_B36F")

        TurnDirection(0xFE, 0x101, 300)
        Yield()
        Jump("loc_B36F")

    QueueWorkItem2(0x15, 1, lambda_B36F)

    def lambda_B381():
        OP_9B(0x0, 0xFE, 0x5A, 0xA28, 0x2BC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B381)

    def lambda_B396():
        OP_9B(0x0, 0xFE, 0x5A, 0xA28, 0x2BC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B396)

    def lambda_B3AB():
        OP_9B(0x0, 0xFE, 0x5A, 0xA28, 0x2BC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B3AB)

    def lambda_B3C0():
        OP_95(0xFE, 1870, 10000, 17460, 700, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B3C0)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x103, 1)
    OP_64(0x15)

    #C0571
    ChrTalk(
        0x15,
        (
            "#5P……やっぱりお前……\x01",
            "気に入らない奴。\x02",
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

    def lambda_B43A():
        TurnDirection(0xFE, 0x15, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_B43A)
    Sleep(12)

    def lambda_B44A():
        TurnDirection(0xFE, 0x15, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_B44A)

    def lambda_B457():
        TurnDirection(0xFE, 0x15, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_B457)
    Sleep(10)

    def lambda_B467():
        TurnDirection(0xFE, 0x15, 400)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_B467)
    Sleep(300)

    #C0572
    ChrTalk(
        0x101,
        "#11P#0005Fへ……\x02",
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
        "#5P#4S……オレは女だ！！\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x12C, 0x0, 0xBB8, 0x1F4)

    #C0574
    ChrTalk(
        0x15,
        (
            "#5P#4Sいつまで\x01",
            "バカにするつもりだ！！\x02",
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
        "#6P#0011Fって、#4Sえええええええ……！？\x02",
    )

    CloseMessageWindow()

    #C0576
    ChrTalk(
        0x104,
        (
            "#12P#0305Fそうなのかよ……！？\x02\x03",

            "#0301Fむ、そういや可愛い顔を\x01",
            "してやがるが……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x104, 500)
    Sleep(200)

    #C0577
    ChrTalk(
        0x103,
        (
            "#6P#0205Fあれ、ランディさんは\x01",
            "今ごろ気付いたんですか？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x14, 0x104, 500)

    #C0578
    ChrTalk(
        0x14,
        (
            "#5P#1809Fシュリちゃんは\x01",
            "どこから見ても\x01",
            "女の子だと思いますけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0579
    ChrTalk(
        0x101,
        (
            "#6P#0011F…………………………\x02\x03",

            "#0012Fその、君を捕まえる時に\x01",
            "思いっきり、その……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x12, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x14, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(800)

    def lambda_B766():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B766)

    def lambda_B773():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B773)

    def lambda_B780():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_B780)

    #C0580
    ChrTalk(
        0x104,
        "#12P#0307Fロイド、お前……\x02",
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_93(0x15, 0xE1, 0x190)
    Sleep(300)

    #C0581
    ChrTalk(
        0x15,
        (
            "#11Pだ、だから離せって言ったんだ。\x01",
            "このバカ……！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 500)
    Sleep(500)

    def lambda_B80A():
        TurnDirection(0xFE, 0x12, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B80A)
    OP_64(0x15)

    #C0582
    ChrTalk(
        0x101,
        (
            "#6P#0011Fいやだって、どう考えても\x01",
            "男の感触っていうか……！\x02",
        )
    )

    CloseMessageWindow()

    #C0583
    ChrTalk(
        0x102,
        (
            "#11P#0111Fふうん……\x01",
            "感触まで覚えてるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0584
    ChrTalk(
        0x103,
        "#6P#0211Fロイドさん、問題発言ですね。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)
    Sleep(300)

    def lambda_B8C0():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B8C0)

    #C0585
    ChrTalk(
        0x101,
        "#5P#0012Fわああ、そういう意味じゃなくて……！\x02",
    )

    CloseMessageWindow()

    #C0586
    ChrTalk(
        0x12,
        (
            "#5P#1709Fあはは、お触りくらいなら\x01",
            "ギリオーケーでしょ！\x02",
        )
    )

    CloseMessageWindow()

    #C0587
    ChrTalk(
        0x14,
        "#5P#1806Fロイドさん……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    BeginChrThread(0x101, 1, 0, 32)

    #C0588
    ChrTalk(
        0x101,
        (
            "#6P#0011Fち、違うから！\x01",
            "そんなつもりじゃないから……！！\x02",
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
            "クエスト【ストーカーの捜査依頼！！】\x07\x00",
            "を達成した！\x02",
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

    # Function_29_9A91 end

    def Function_30_BAD2(): pass

    label("Function_30_BAD2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_BAFE")
    OP_93(0xFE, 0x10E, 0x190)
    OP_93(0xFE, 0xB4, 0x190)
    OP_93(0xFE, 0x5A, 0x190)
    OP_93(0xFE, 0x0, 0x190)
    Jump("Function_30_BAD2")

    label("loc_BAFE")

    Return()

    # Function_30_BAD2 end

    def Function_31_BAFF(): pass

    label("Function_31_BAFF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_BB24")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    Jump("Function_31_BAFF")

    label("loc_BB24")

    Return()

    # Function_31_BAFF end

    def Function_32_BB25(): pass

    label("Function_32_BB25")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_BB53")
    TurnDirection(0xFE, 0x12, 500)
    Sleep(500)
    TurnDirection(0xFE, 0x102, 500)
    Sleep(500)
    TurnDirection(0xFE, 0x103, 500)
    Sleep(800)
    Jump("Function_32_BB25")

    label("loc_BB53")

    Return()

    # Function_32_BB25 end

    def Function_33_BB54(): pass

    label("Function_33_BB54")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x3)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BB7A")
    Call(0, 23)
    Jump("loc_BBAB")

    label("loc_BB7A")

    TalkBegin(0xFF)
    Sound(810, 0, 100, 0)

    #A0590
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "鍵が掛かっているようだ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)

    label("loc_BBAB")

    Return()

    # Function_33_BB54 end

    def Function_34_BBAC(): pass

    label("Function_34_BBAC")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BD4C")
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0591
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ワイングラスやボトルが\x01",
            "乱雑に並べられている。\x02",
        )
    )

    CloseMessageWindow()

    #A0592
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ボトルはほとんど残っていない……\x02",
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
            "#0012F昨晩は酒盛りでも\x01",
            "してたのかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0594
    ChrTalk(
        0x104,
        (
            "#0300Fいや、イリア・プラティエは\x01",
            "かなりの酒豪らしいぜ。\x02\x03",

            "日常的にこのくらい\x01",
            "飲んでるんじゃねえか？\x02",
        )
    )

    CloseMessageWindow()

    #C0595
    ChrTalk(
        0x101,
        "#0005Fうっ、そうなのか……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_BDBF")

    label("loc_BD4C")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0596
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ワイングラスやボトルが\x01",
            "乱雑に並べられている。\x02",
        )
    )

    CloseMessageWindow()

    #A0597
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ボトルはほとんど残っていない。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()

    label("loc_BDBF")

    TalkEnd(0xFF)
    Return()

    # Function_34_BBAC end

    def Function_35_BDC3(): pass

    label("Function_35_BDC3")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BECB")
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0598
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ベッドの上には\x01",
            "洋服が散らばっている……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()

    #C0599
    ChrTalk(
        0x102,
        "#0106Fこれ、ブランド物なのに……\x02",
    )

    CloseMessageWindow()

    #C0600
    ChrTalk(
        0x103,
        "#0200F乱雑です。\x02",
    )

    CloseMessageWindow()

    #C0601
    ChrTalk(
        0x104,
        (
            "#0303F朝にクローゼットから\x01",
            "引き出したママって感じだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0602
    ChrTalk(
        0x101,
        (
            "#0000F出勤時間の光景が\x01",
            "目に浮かぶようだなぁ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_BF10")

    label("loc_BECB")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0603
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ベッドの上には\x01",
            "洋服が散らばっている。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()

    label("loc_BF10")

    TalkEnd(0xFF)
    Return()

    # Function_35_BDC3 end

    def Function_36_BF14(): pass

    label("Function_36_BF14")

    EventBegin(0x1)

    #C0604
    ChrTalk(
        0x101,
        (
            "#0000F今はストーカーの捜査に\x01",
            "専念しよう。\x02\x03",

            "イリアさんから鍵まで\x01",
            "預かってしまってるしな。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -160, 30, 1350, 0)
    EventEnd(0x4)
    Return()

    # Function_36_BF14 end

    SaveToFile()

Try(main)
